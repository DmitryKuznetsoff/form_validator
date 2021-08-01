# Web-приложение для определения заполненных форм

В базе данных хранится список шаблонов форм.

Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.

Пример шаблона формы:
```json
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```

Всего должно поддерживаться четыре типа данных полей:
  1. email
  2. телефон
  3. дата
  4. текст

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате ```+7 xxx xxx xx xx```, дата передается в формате ```DD.MM.YYYY``` или ```YYYY-MM-DD```.

На вход по урлу ```/get_form``` ```POST``` запросом передаются данные такого вида:
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
В ответ нужно вернуть имя шаблона формы, если она была найдена.
Чтобы найти подходящий шаблон, нужно выбрать тот, поля которого совпали с полями в присланной форме. 
Совпадающими считаются поля, у которых совпали имя и тип значения. 

Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим. 
Самое главное, чтобы все поля шаблона присутствовали в форме.

Если подходящей формы не нашлось, вернуть ответ в следующем формате:
```json
{
    "field1": "field_type",
    "field2": "field_type"
}
```
Где ```field_type``` это тип поля, выбранный на основе правил валидации.

#### Структура приложения:
1. ```app``` - модуль, в котором происходит инициализация и конфигурация приложения
2. ```db``` - модуль, предоставляющий инструменты для взаимодействия с ```mongodb```. В ```db/collections``` хранятся документы для последующей записи в ```mongo```
3. ```form_validator``` - модуль с валидацией форм
4. ```tests``` - ```pytest``` тесты и фикстуры

#### Собрать и запустить через docker-compose:
```shell
docker-compose up --build -d
```

#### Запустить тесты в контейнере:
```shell
docker exec -it form_validator_app pytest
```