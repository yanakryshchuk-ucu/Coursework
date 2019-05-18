Всі модулі програми містяться [тут](https://github.com/yana-miia/ali_analyzer), оскільки для спільної роботи над проектом було створено окремий репозиторій.

![image](https://github.com/yanakryshchuk-ucu/Coursework/blob/master/Images/IMG_20190515_220622_258-02.jpeg)

## Призначення та коротка характеристика програми
Тут  представлена курсова робота із дисципліни Основи Програмування. Суть проекту полягає у аналізі попиту на товари та оцінці доброчесності продавців в інтернет-магазинах, досліджуючи дані, які надає інтернет-магазин AliExpress.
Для роботи було отримано АРІ ключ, який дає доступ до всієї інформації, необхідної для роботи над проектом.

## Вхідні та вихідні дані програми
Користувач вводить своє ім'я й обирає роль (Покупець/Продавець) та отримує список команд із описом, які для нього доступні.

![image](https://github.com/yanakryshchuk-ucu/Coursework/blob/master/Images/console-example1.png)

Список команд Продавця:
* 1 - best products --> Show you the bestselling products.
* 2 - demand --> Show you market demand with orders.
* 3 - trend --> Return 'best products' in top category.
* 4 - sellers --> Gives you list of best sellers with their rating.
* 5 - statistic --> Show you statistic about product selling with their price, * number of orders and profit.
* 6 - recommendations --> Gives you expectations on each product.
----
Список команд Покупця:
* 1 - best products --> Show you the bestselling products.
* 2 - best sellers --> Gives you list of best sellers with their rating.
* 3 - worst sellers --> Gives you the list of worst sellers.
* 4 - best shipping --> Shows you the market with chosen product, where the speed of shipping is the highest.
* 5 - alternative --> Gives you options for buying alternative products.

![image](https://github.com/yanakryshchuk-ucu/Coursework/blob/master/Images/console-example2.png)


Програма видає результати, відповідно до опції, яку обрав користувач, що базуються на аналізі ринку.

## Структура програми з коротким описом модулів, функцій, класів та методів.
Програма складається із таких модулів:
* main.py - модуль для запуску програми:
* ali_request.py - у цьому модулі використовується API та містяться функції, що відповідають за стягнення необхідної для аналізу інформації.
* user.py - модуль, що містить клас User, який є батьківським для класів Seller та Buyer:
  * get_best_products() - метод для отримання найкращих продуктів у катеорії.
* buyer.py - містить клас Buyer з методами, що відповідають за функціонал команд Покупця:
  * get_best_sellers() - метод, що відповідає за одержання списку найкращих продавців.
  * get_worst_sellers() -  відповідає за одержання списку найгірших продавців.
  * get_alternative() - повертає список альтернатив обраному продукту.
  * find_best_shipping() - метод, що шукає найбільш вигідний спосіб доставки серед обраних товарів.
* seller.py - містить клас Seller з методами, що відповідають за функціонал команд Продавця:
  * find_demand() - метод, що шукає попит на товари кожної з категорій.
  * get_trend() - шукає найбільш популярні та затребувані товари по категоріях.
  * get_best_sellers() - відповідає за одержання списку найкращих продавців та їх рейтингу.
  * get_product_statistic() - повертає статистику про продукт.
  * filter_product() - отримує відфільтровані дані про продукти.
  * get_personal_recommendations() - аналізує успіх продажів внаслідок виходу певного продукту на ринок.

* product.py - містить класи Product та DetailedProduct - підклас Product.

## Коротка інструкція по користуванню програмою
При запуску програми користувач може обрати одну із двох ролей: Продавець(Seller) або покупець(Buyer).

Можливості, які надає програма для Покупця:
* Аналізувати ринок у певній категорії товарів.
* Отримати список найкращих продавців у категорії.
* Отримати список найгірших продавців у категорії.
* Отримати інформацію про найпопулярніші товари у категорії.
* Отримати результати аналізу щодо найвигіднішої покупки у вибраній категорії товарів.
* Отримати список альтернатив обраному товару.
* Вирахувати серед однакових товарів у різних продавцій той, що має найшвидшу доставку.
----
Можливості, які надає програма для Продавця:
* Аналізувати ринок у певній категорії товарів.
* Отримати список найуспішніших продавців у категорії, щоб мати змогу взяти з них приклад для розвинення свого бізнесу.
* Отримати список товарів з найкращими відгуками у категорії.
* Отримати список із найбільш затребуваними товарами у категорії.
* Отримати статистику про обраний продукт (ціна та кількість продажів).
* Отримати персональні рекомендації щодо виводу товарів на ринок.

## Встановлення та використання
```bash
git clone https://github.com/yana-miia/ali_analyzer.git

cd ali_analyzer/

python3 main.py
```

## Опис тестових прикладів для первірки працездатності програми
Тестові приклади містяться у модулі [tests.py](https://github.com/yana-miia/ali_analyzer/blob/master/tests.py).

Для запуску потрібно просто розкоментувати частину, яка Вас цікавить, адже через обмеження кількості запитів на API все одночасно не може бути виконано.

## Права власності
[Яна Крищук](https://github.com/yanakryshchuk-ucu/Coursework)

[Соломія Дубневич](https://github.com/rockqeen45/MarketAnalyzer1)
