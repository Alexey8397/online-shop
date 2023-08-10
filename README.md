# Online-shop

Интернет-магазин с использованием Django

## О проекте

Магазин выполненный на django версии 4.2.3, python 3.11. В качестве БД подключалась SQLite.
Магазин имеет такой функционал:
- список всех продуктов;
- список категорий;
- добавление названия к продукту;
- добавление описания к продукту;
- добавление изображения к продукту;
- добавление стоимости продукта;
- добавление наличия продукта;
- возможность добавлять, изменять количество товара и удалять из корзины;
- регистрация, аутентификация, авторизация пользователей;


## Установка

В виртуальном окружении (virtualenv) выполнить данную команду:
```
pip install -r requirements.txt
```
Далее запустить сервер командой:
```
python manage.py runserver
```
или
```
./manage.py runserver
```


Также использовался Django REST framework, ниже представлена краткая документация:

<!-- TRANSLATED by md-translate -->
# Django REST framework

![Logo by Jake 'Sid' Smith](https://github.com/encode/django-rest-framework/raw/master/docs/img/logo.png)

Django REST framework - это мощный и гибкий набор инструментов для создания Web API.

Некоторые причины, по которым вы можете захотеть использовать REST framework:

* [Просматриваемый API](https://restframework.herokuapp.com/) - огромный выигрыш в удобстве использования для ваших разработчиков.
* [Политики аутентификации](api-guide/authentication.md), включая пакеты для [OAuth1a](api-guide/authentication.md#django-rest-framework-oauth) и [OAuth2](api-guide/authentication.md#django-oauth-toolkit).
* [Сериализация](api-guide/serializers.md), поддерживающая как [ORM](api-guide/serializers.md#modelserializer), так и [non-ORM](api-guide/serializers.md#сериализаторы) источники данных.
* Настраивается все - просто используйте [обычные представления на основе функций](api-guide/views#Представления-на-основе-функций), если вам не нужны [более](api-guide/generic-views.md) [мощные](api-guide/viewsets.md) [возможности](api-guide/routers.md).
* Обширная документация и [отличная поддержка сообщества](https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework).
* Используется и пользуется доверием всемирно известных компаний, включая [Mozilla](https://www.mozilla.org/en-us/about/), [Red Hat](https://www.redhat.com/), [Heroku](https://www.heroku.com/) и [Eventbrite](https://www.eventbrite.co.uk/about/).

---

## Требования

REST framework требует следующего:

* Python (3.6, 3.7, 3.8, 3.9, 3.10, 3.11)
* Django (2.2, 3.0, 3.1, 3.2, 4.0, 4.1)

Мы **настоятельно рекомендуем** и официально поддерживаем только последние выпуски патчей каждой версии Python и Django.

Следующие пакеты являются необязательными:

* [PyYAML](https://pypi.org/project/pyyaml/), [uritemplate](https://pypi.org/project/uritemplate/) (5.1+, 3.0.0+) - Поддержка генерации схем.
* [Markdown](https://pypi.org/project/markdown/) (3.0.0+) - Поддержка Markdown для просматриваемого API.
* [Pygments](https://pypi.org/project/pygments/) (2.4.0+) - Добавление подсветки синтаксиса в обработку Markdown.
* [django-filter](https://pypi.org/project/django-filter/) (1.0.1+) - Поддержка фильтрации.
* [django-guardian](https://github.com/django-guardian/django-guardian) (1.1.1+) - Поддержка разрешений на уровне объектов.

## Установка

Установите с помощью `pip`, включая все дополнительные пакеты, которые вы хотите...

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```



Добавьте `'rest_framework'` в настройку `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Если вы планируете использовать просматриваемый API, вы, вероятно, также захотите добавить представления входа и выхода из системы REST framework. Добавьте следующее в ваш корневой файл `urls.py`.

```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```



## Быстрый старт

Не можете дождаться начала работы? Руководство [quickstart](quickstart.md) - это самый быстрый способ начать работу и создавать API с помощью REST framework.

## Руководство

Руководство проведет вас через все этапы настройки DRF. Это займет не очень много времени, однако вы получите полное понимание того, как все компоненты работают друг с другом и данное руководство крайне рекомендовано к прочтению.

* [Сериализация](tutorial/1-serialization.md)
* [Запросы-ответы](tutorial/2-requests-and-responses.md)
* [Представления-классы](tutorial/3-class-based-views.md)
* [Аутентификация/права доступа](tutorial/4-authentication-and-permissions.md)
* [Отношения и связи](tutorial/5-relationships-and-hyperlinked-apis.md)
* [Наборы представлений и роутеры](tutorial/6-viewsets-and-routers.md)

Так же есть пример работающего API законченного руководства для тестовых целей, [доступен здесь](http://restframework.herokuapp.com/).

## Навигатор по API

Навигатор по API - исчерпывающее руководство по всему функционалу, предоставляемому DRF.

* [Запросы](api-guide/requests.md)
* [Ответы](api-guide/responses.md)
* [Представления](api-guide/views.md)
* [Общие представления](api-guide/generic-views.md)
* [Viewsets](api-guide/viewsets.md)
* [Маршрутизаторы](api-guide/routers.md)
* [Парсеры](api-guide/parsers.md)
* [Рендереры](api-guide/renderers.md)
* [Сериализаторы](api-guide/serializers.md)
* [Поля сериализатора](api-guide/fields.md)
* [Отношения сериализаторов](api-guide/relations.md)
* [Валидаторы](api-guide/validators.md)
* [Аутентификация](api-guide/authentication.md)
* [Разрешения](api-guide/permissions.md)
* [Кэширование](api-guide/caching.md)
* [Дросселирование](api-guide/throttling.md)
* [Фильтрация](api-guide/filtering.md)
* [Пагинация](api-guide/pagination.md)
* [Версионирование](api-guide/versioning.md)
* [Согласование контента](api-guide/content-negotiation.md)
* [Метаданные](api-guide/metadata.md)
* [Schemas](api-guide/schemas.md)
* [Cуффиксы формата](api-guide/format-suffixes.md)
* [Возвращение URL-адресов](api-guide/reverse.md)
* [Исключения](api-guide/exceptions.md)
* [Коды состояния](api-guide/status-codes.md)
* [Тестирование](api-guide/testing.md)
* [Настройки](api-guide/settings.md)

## Статьи

Основные руководства для использующих DRF.

* [AJAX, CSRF & CORS](topics/ajax-csrf-cors.md)
* [The Browsable API](topics/browsable-api.md)
* [Улучшения в браузере](topics/browser-enhancements.md)
* [Документирование вашего API](topics/documenting-your-api.md)
* [HTML и формы](topics/html-and-forms.md)
* [Интернационализация](topics/internationalization.md)
* [REST, гипермедиа и HATEOAS](topics/rest-hypermedia-hateoas.md)
* [Вложенные сериализаторы с возможностью записи](topics/writable-nested-serializers.md)

## Разработка

Смотрите [руководство для разработчиков](https://www.django-rest-framework.org/community/contributing/) для получения информации о том, как клонировать репозиторий, запустить набор тестов и внести изменения в REST Framework.

## Поддержка

За поддержкой обращайтесь в [REST framework discussion group](https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework), попробуйте использовать канал `#restframework` на `irc.libera.chat`, или задайте вопрос на [Stack Overflow](https://stackoverflow.com/), обязательно указав тег ['django-rest-framework'](https://stackoverflow.com/questions/tagged/django-rest-framework).

Для получения приоритетной поддержки подпишитесь на [профессиональный или премиум спонсорский план](https://fund.django-rest-framework.org/topics/funding/).

## Безопасность

Вопросы безопасности решаются под руководством [Django security team](https://www.djangoproject.com/foundation/teams/#security-team).

**Пожалуйста, сообщайте о проблемах безопасности по электронной почте security@djangoproject.com**.

После этого сопровождающие проекта будут работать с вами над решением любых вопросов, если потребуется, до обнародования информации.

## Автор

* **Alexey Rezevskiy**