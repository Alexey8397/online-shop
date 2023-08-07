from decimal import Decimal
from django.conf import settings
from myshop.models import Product


class Basket(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:
            # сохраняем ПУСТУЮ корзину в сессии
            basket = self.session[settings.CART_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данных.
        """
        product_ids = self.basket.keys()
        # получаем товары и добавляем их в корзину
        products = Product.objects.filter(id__in=product_ids)

        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.basket.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, product):
        """
        Удаляем товар
        """
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.basket_SESSION_ID]
        self.save()