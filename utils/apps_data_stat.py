import numpy as np
import pandas as pd


def get_and_validate_app_data():
    with open(file='data/googleplaystore.csv', mode='r', encoding='utf-8') as apps_data:
        raw_apps_df = pd.read_csv(apps_data)
    # Удаляем строки если есть NaN в столбцах Rating, Content Rating, Type
    raw_apps_df.dropna(how='any', inplace=True, subset=['Rating', 'Content Rating', 'Type'])
    # Заменяем все Varies with device в столбце Size на NaN
    raw_apps_df['Size'].replace('Varies with device', np.nan, inplace=True)
    # Присваиваем строкам со значением NaN размер в 1 Mb (fillna)
    raw_apps_df['Size'] = raw_apps_df['Size'].fillna(1)
    # Через apply и lambda убираем M из значений Size в Mb
    raw_apps_df['Size'] = raw_apps_df['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    # Через apply и lambda убираем k из значений Size и приводим Kb к Mb
    raw_apps_df['Size'] = raw_apps_df['Size'] \
        .apply(lambda x: float(str(x).replace('k', '')) / 1_000 if 'k' in str(x) else x)
    raw_apps_df['Size'] = raw_apps_df['Size'].apply(lambda x: float(x))
    # Убираем '$' из цены приложений
    raw_apps_df['Price'] = raw_apps_df['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else x)
    raw_apps_df['Price'] = raw_apps_df['Price'].apply(lambda x: float(x))
    # Убираем '+' и ',' из кол-ва установок
    raw_apps_df['Installs'] = raw_apps_df['Installs'].apply(
        lambda x: str(x).replace(',', '') if ',' in str(x) else x
    )
    # Я не собираюсь импортировать регулярки ради одной строчки
    raw_apps_df['Installs'] = raw_apps_df['Installs'].apply(
        lambda x: str(x).replace('+', '') if '+' in str(x) else x
    )
    raw_apps_df['Installs'] = raw_apps_df['Installs'].apply(lambda x: float(x) / 100_000)
    validated_apps_df = raw_apps_df
    return validated_apps_df


apps_df = get_and_validate_app_data()


def get_data_overview() -> None:
    """
    Считает строки и стробцы в googleplaystore.csv
    Выводит на печать результат
    """
    rows, columns = apps_df.shape
    print(f'\nОбщий объем данных: {rows} строк, {columns} столбцов\n')


def get_all_categories() -> None:
    """
    Выводит список категорий приложений
    """
    number_of_categories = len(apps_df['Category'].unique())
    print(f'Всего в Playstore существует {number_of_categories} категорий приложений:')
    categories = apps_df['Category'].unique()
    counter = 0
    for number, a in enumerate(categories, start=1):
        if counter < 4:
            print(number, a.replace('_', ' '), end=' | ')
            counter += 1
        else:
            print(number, a.replace('_', ' '))
            counter = 0
    print('\n')


def get_all_genres() -> None:
    """
    Выводит список жанров приложений
    """
    # Отбрасываем субжанры, в которых всего 1-3 приложения
    # print(apps_df.Genres.value_counts().tail(20))
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    number_of_genres = len(apps_df['Genres'].unique())
    print(f'Всего в Playstore существует {number_of_genres} жанров приложений:')
    genres = apps_df['Genres'].unique()
    counter = 0
    for number, a in enumerate(genres, start=1):
        if counter < 4:
            print(number, a.replace('_', ' '), end=' | ')
            counter += 1
        else:
            print(number, a.replace('_', ' '))
            counter = 0
    print('\n')


def get_x_most_popular_genres():
    """
    Выводит X самых популярных жанров приложений
    """
    user_number = input('Выберете кол-во значений для вывода\n')
    try:
        user_number = int(user_number)
    except ValueError:
        print('Введите числовое значение')
        return
    if user_number == 0:
        print('Выбранно 0 значений')
        return
    elif user_number == 1:
        print(f'Самый популярный жанр:\n{apps_df["Genres"].value_counts().head(user_number).to_string()}')
    else:
        print(f'Самые популярные жанры:\n{apps_df["Genres"].value_counts().head(user_number).to_string()}')


def get_x_most_popular_apps():
    """
    Выводит X самых популярных приложений приложений из жанра на основании установок
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    user_number = input('Выберете кол-во значений для вывода\n')
    get_all_genres()
    user_genre = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    try:
        user_number = int(user_number)
    except ValueError:
        print('Введите числовое значение')
        return

    if user_number == 0:
        print('Выбранно 0 значений')
        return
    elif user_number == 1:
        if user_genre == 'All':
            print(f'Самое популярное приложение:\n{apps_df.nlargest(user_number, ["Installs"]).to_string()}')
            return
        elif user_genre in genres:
            print(f'Самое популярное приложение в жанре {user_genre}:\n'
                  f'{apps_df[(apps_df["Genres"] == user_genre)].nlargest(user_number, ["Genres"]).to_string()}'
                  )
            return
        else:
            print('Такого жанра не существует')
            return
    else:
        if user_genre == 'All':
            print(f'Самые популярные приложения:\n{apps_df.nlargest(user_number, ["Installs"]).to_string()}')
            return
        elif user_genre in genres:
            print(f'Самые популярные приложения в жанре {user_genre}:\n'
                  f'{apps_df[(apps_df["Genres"] == user_genre)].nlargest(user_number, ["Installs"]).to_string()}'
                  )
            return
        else:
            print('Такого жанра не существует')
            return


def get_mean_rating_size_price_installs() -> None:
    """
    Выводит средний рейтинг/размер/цену одного жанра приложений или всех приложений, в зависимости от ввода
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_genre = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    user_type = input('Введите число типа данных для вывода: \n1: Рейтинг\n2: Размер\n3: Цена\n4: Кол-во установок\n')
    try:
        user_type = int(user_type)
    except ValueError:
        print('Введите числовое значение')
        return
    if user_genre == 'All':
        if user_type == 1:
            rating_mean = apps_df['Rating'].describe().loc['mean']
            print(f'Средний рейтинг приложений равен:\n{rating_mean:.2f}')
        elif user_type == 2:
            size_mean = apps_df['Size'].describe().loc['mean']
            print(f'Средний вес приложения равен:\n{size_mean:.2f} MB')
        elif user_type == 3:
            price_mean = apps_df['Price'].describe().loc['mean']
            print(f'Средняя цена приложения равна:\n{price_mean:.2f}$')
        elif user_type == 4:
            installs_mean = apps_df['Installs'].describe().loc['mean']
            print(f'Среднее кол-во установок приложений равно:\n{installs_mean:.2f} сотен тыс.')
        else:
            print('Такого типа данных не существует')
            return
    elif user_genre in genres:
        if user_type == 1:
            rating_mean = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Rating'].describe().loc['mean']
            print(f'Средний рейтинг приложения в жанре {user_genre} равен:\n{rating_mean:.2f}')
        elif user_type == 2:
            size_mean = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Size'].describe().loc['mean']
            print(f'Средний вес приложения в жанре {user_genre} равен:\n{size_mean:.2f} MB')
        elif user_type == 3:
            price_mean = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Price'].describe().loc['mean']
            print(f'Средняя цена приложения в жанре {user_genre} равна:\n{price_mean:.2f}$')
        elif user_type == 4:
            installs_mean = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Price'].describe().loc['mean']
            print(f'Средее кол-во установок приложений в жанре {user_genre} равно:\n{installs_mean:.2f} сотен тыс.')
        else:
            print('Такого типа данных не существует')
            return
    else:
        print('Такого жанра не существует')


def get_median_rating_size_price_installs() -> None:
    """
    Выводит медианный рейтинг одного жанра приложений или всех приложений, в зависимости от ввода
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_genre = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    user_type = input('Введите число типа данных для вывода: \n1: Рейтинг\n2: Размер\n3: Цена\n4: Кол-во установок\n')
    try:
        user_type = int(user_type)
    except ValueError:
        print('Введите числовое значение')
        return
    if user_genre == 'All':
        if user_type == 1:
            rating_median = apps_df['Rating'].describe().loc['50%']
            print(f'Медианный рейтинг приложения равен:\n{rating_median}')
        elif user_type == 2:
            size_median = apps_df['Size'].describe().loc['50%']
            print(f'Медианный вес приложения равен:\n{size_median} MB')
        elif user_type == 3:
            price_median = apps_df['Price'].describe().loc['50%']
            print(f'Медианная цена приложения равна:\n{price_median}')
        elif user_type == 4:
            installs_median = apps_df['Installs'].describe().loc['50%']
            print(f'Медианное кол-во установок приложений равно:\n{installs_median} сотен тыс.')
        else:
            print('Такого типа данных не существует')
            return
    elif user_genre in genres:
        if user_type == 1:
            rating_median = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Rating'].describe().loc['50%']
            print(f'Медианный рейтинг приложения в жанре {user_genre} равен:\n{rating_median}')
        elif user_type == 2:
            size_median = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Size'].describe().loc['50%']
            print(f'Медианный вес приложения в жанре {user_genre} равен:\n{size_median} MB')
        elif user_type == 3:
            price_median = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Price'].describe().loc['50%']
            print(f'Медианная цена приложения в жанре {user_genre} равна:\n{price_median}')
        elif user_type == 4:
            installs_median = apps_df[(apps_df['Genres'] == f'{user_genre}')]['Price'].describe().loc['50%']
            print(f'Медианное кол-во установок приложений в жанре {user_genre} равно:\n{installs_median} сотен тыс.')
        else:
            print('Такого типа данных не существует')
            return
    else:
        print('Такого жанра не существует')
