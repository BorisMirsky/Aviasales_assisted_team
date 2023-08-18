# Aviasales_assisted_team
Тестовое задание Aviasales, отдел assisted_team ('Python')
https://github.com/KosyanMedia/test-tasks/tree/master/assisted_team

В папке два XML – это ответы на поисковые запросы, сделанные к одному из наших партнёров. 
В ответах лежат варианты перелётов (тег Flights) со всей необходимой информацией, 
чтобы отобразить билет на Aviasales.

На основе этих данных, нужно сделать вебсервис, в котором есть эндпоинты, 
отвечающие на следующие запросы:

Какие варианты перелёта из DXB в BKK мы получили?
Самый дорогой/дешёвый, быстрый/долгий и оптимальный варианты
В чём отличия между результатами двух запросов (изменение маршрутов/условий)?
Язык реализации: Go Формат ответа: json По возможности использовать стандартную библиотеку.

Язык реализации: python3 Формат ответа: json Используемые библиотеки и инструменты — всё на твой выбор.

Оценивать будем умение выполнять задачу имея неполные данные о ней, 
умение самостоятельно принимать решения и качество кода.



-----------------Как пользоваться-----------------------------

1. Предполагаем, что Python >=3.5 и библиотека virtualenv уже установлены. Затем надо склонировать проект в локальную папку. Перейти в папку проекта и создать виртуальное окружение 'python -m venv my_virt'. Зайти в my_virt\Scripts и запустить виртуальное окружение командой activate. Находясь в виртуальном окружении вызвать команду 'pip install -r requirments.txt'.

2. Запуск 'class_4.py' даст на вопросы 'варианты перелёта из DXB в BKK', 'цена перелёта', 'время в пути'и 'отличия результатов'. \
   Строки для запуска закоментированы в конце файла.

3. Из двух файлов с сотнями записей было только по одной, отвечающей условиям, не считая дубликатов. При сравнение - цена одинакова, время в пути различается на полчаса.





