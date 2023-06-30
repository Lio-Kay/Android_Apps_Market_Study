# PandasAndroidMarketStudy
Android market study with pandas, seaborn, mathplot, based on data from kaggle Google Play Store Apps

Dataset: https://www.kaggle.com/datasets/lava18/google-play-store-apps

This app can show the following data about Google Play Store Apps: •visualize categories •visualize genres •visualize rating per selected genre •visualize all ratings as boxenplot •visualize app size per genre •visualize % of free and paid apps per selected genre •visualize price of apps as scatterplot •visualize installs per selected genre •visualize optimal app size per selected genre

•show 'x' most popular genres •show 'x' most popular apps per selected genre •show mean rating/size/price/installs per selected genre •show median rating/size/price/installs per selected genre


# Исследование рынка Android приложений при помощи библиотеки Pandas

## Описание
CLI-программа на python для получения вакансий посредством API hh.ru и/или superjob.ru, с возможностью выбора основных параметров
поиска (ключевые слова в вакансии, регион поиска, тип занятости, ЗП, тип занятости, тип сортировки), возможностью
сохранения вакансий в .csv черный список и .json для дальнейшей работы и возможностью дальнейшей манипуляции с файлом
(сравнение по зп, удаление).

## Пример получения графика


## Описание структуры проекта
* data
  - googleplaystore.csv - датасет из +10.000 приложений Google Play
  - googleplaystore_user_reviews.csv - датасет из +60.000 отзывов пользователей на Google Play
* data_visualization - файл для вывода различных графиков и диаграмм
* utils
  - vacancies_get_functions.py - Файл с логикой для работы с файлом и сохраненными в него вакансиями
  - vacancies_search_functions.py - Файл с логикой для работы с поиском вакансий на разных платформах
* work_with_data
  - vacancies_classes.py - Файл для создания экземпляров класса для сравнения уже сохраненных вакансий
  - work_with_files.py - Файл с классами для работы с файлами в /data
- main.py - Меню и файл объединяющий всю логику
- manual_testing.py - Файл для получения 'инфодампа' т.к. корректность графиков можно контролировать только визуально

## Технологии в проекте
Библиотеки:
* os;
* pandas;
* numpy;
* matplotlib;
* seaborn.

Другие особенности:
* poetry вместо venv/pip;
* Написан на основе принципов SOLID;
* Отлов большинства ошибок взаимодействия пользователя с CLI.

## Возможные улучшения
* Написать unit-тесты на pytest;
* Сделать GUI;
* Добавить другие платформы;
* Расширить доступные фильтры.
