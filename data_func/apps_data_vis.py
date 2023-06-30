import matplotlib.pyplot as plt
import seaborn as sns

from data_func.apps_data_stat import get_and_validate_app_data, get_all_genres


sns.set_theme(style='dark')

apps_df = get_and_validate_app_data()


def visualize_categories() -> None:
    """
    Визуализирует распределение категории приложений.
    Сохраняет график в файл.
    """
    plt.figure(num=1)
    plt.grid()
    a = sns.countplot(x='Category', orient='h', data=apps_df, palette='muted')
    a.set_xticklabels(a.get_xticklabels(), size=15, rotation=70, ha='right')
    a.set_ylabel('Кол-во', size=20)
    a.set_title('Кол-во приложений в каждой категории', size=40)
    figure = a.get_figure()
    plt.show()
    figure.savefig("data_visualization/apps_categories.png")
    print(f'Визуализация данных находится в файле "data_visualization/apps_categories"')


def visualize_genres() -> None:
    """
    Визуализирует распределение жанров приложений.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    plt.figure(num=1)
    plt.grid()
    a = sns.countplot(x='Genres', orient='h', data=apps_df, palette='Set3')
    a.set_xticklabels(a.get_xticklabels(), size=15, rotation=70, ha='right')
    a.set_ylabel('Кол-во', size=20)
    a.set_title('Кол-во приложений в каждом жанре', size=40)
    figure = a.get_figure()
    plt.show()
    figure.savefig("data_visualization/apps_genres.png")
    print(f'Визуализация данных находится в файле "data_visualization/apps_genres"')


def visualize_rating_per_genre() -> None:
    """
    Визуализирует распределение рейтинга приложений.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_choice = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    plt.figure(num=2)
    plt.grid()
    print(genres)
    if user_choice == 'All':
        a = sns.kdeplot(data=apps_df['Rating'], color='Darkblue', fill=True)
    elif user_choice in genres:
        a = sns.kdeplot(data=apps_df[(apps_df['Genres'] == f'{user_choice}')]['Rating'], color='Darkblue', fill=True)
    else:
        print('Такого жанра не существует')
        return
    a.set_xlabel(xlabel='Частота', size=20)
    a.set_ylabel(ylabel='Рейтинг', size=20)
    a.set_title('Распределение рейтинга', size=40)
    plt.tight_layout()
    figure = a.get_figure()
    plt.show()
    figure.savefig(f'data_visualization/apps_ratings_{user_choice}.png')
    print(f'Визуализация данных находится в файле "data_visualization/apps_ratings_{user_choice}"')


def visualize_rating_as_boxenplot() -> None:
    """
    Визуализирует общее распределение рейтинга приложений в виде boxenplot.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    a = sns.catplot(data=apps_df, x='Genres', y='Rating', kind='boxen', height=10, palette='Set3')
    a.despine(left=True)
    a.set_xticklabels(rotation=70)
    a.set_ylabels('Рейтинг', size=20)
    a.set_xlabels('Жанр', size=20)
    plt.title('Общее распределение рейтинга по жанрам', size=40)
    plt.tight_layout()
    plt.show()
    figure = a.figure
    figure.savefig(f'data_visualization/app_rating_boxenplot.png')
    print(f'Визуализация данных находится в файле "data_visualization/app_rating_boxenplot"')


def visualize_size_per_genre() -> None:
    """
    Визуализирует распределение размера приложений.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_choice = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    plt.figure(num=3)
    plt.grid()
    if user_choice == 'All':
        a = sns.kdeplot(data=apps_df['Size'], color='Teal', fill=True)
        a.set_title(f'Распределение размеров приложений ', size=40)
    elif user_choice in genres:
        a = sns.kdeplot(data=apps_df[(apps_df['Genres'] == f'{user_choice}')]['Size'], color='Teal', fill=True)
        a.set_title(f'Распределение размеров приложений в жанре\n{user_choice}', size=40)
    else:
        print('Такого жанра не существует')
        return
    a.set_xlabel(xlabel='Размер, Мб', size=20)
    a.set_ylabel(ylabel='Частота', size=20)
    figure = a.get_figure()
    plt.show()
    figure.savefig(f'data_visualization/apps_sizes_{user_choice}.png')
    print(f'Визуализация данных находится в файле "data_visualization/apps_sizes_{user_choice}"')


def visualize_free_and_paid_per_genre() -> None:
    """
    Визуализирует % бесплатных приложений.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_choice = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    plt.figure(num=4)
    plt.grid()
    if user_choice == 'All':
        plt.pie(x=apps_df['Type'].value_counts(sort=True), explode=(0.2, 0),
                labels=apps_df['Type'].value_counts(sort=True).index, colors=['LightBlue', 'GhostWhite'],
                autopct='%1.2f%%', shadow=True, startangle=200)
        plt.title('Процент бесплатных приложений', size=40)
    elif user_choice in genres:
        plt.pie(x=apps_df[(apps_df['Genres'] == f'{user_choice}')]['Type'].value_counts(sort=True), explode=(0.2, 0),
                labels=apps_df['Type'].value_counts(sort=True).index, colors=['LightBlue', 'GhostWhite'],
                autopct='%1.2f%%', shadow=True, startangle=200)
        plt.title(f'Процент бесплатных приложений в жанре\n{user_choice}', size=40)
    else:
        print('Такого жанра не существует')
        return
    plt.savefig(fname=f'data_visualization/apps_free_and_paid_{user_choice}.png', bbox_inches='tight')
    plt.show()
    print(f'Визуализация данных находится в файле "data_visualization/apps_free_and_paid_{user_choice}"')


def visualize_price_as_scatterplot() -> None:
    """
    Визуализирует распределение цены приложений по жанру на отдельном графике.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    sns.set_style('darkgrid')
    fig, ax = plt.subplots()
    fig.set_figwidth(20)
    fig.set_figheight(8)

    # Отбрасываем приложения с ценой > 80 $, они бесполезны для анализа
    # print(apps_df[['Category', 'App']][apps_df.Price > 80])

    a = sns.stripplot(data=apps_df[apps_df['Price'] < 79], x='Price', y='Genres',
                      linewidth=1, palette='Pastel1', jitter=0.2)
    a.set_xlabel(xlabel='Цена, $', size=20)
    a.set_ylabel(ylabel='Жанр', size=20)
    ax.set_title('Общее распределение цен на приложения', size=40)
    plt.show()
    figure = a.figure
    figure.savefig(f'data_visualization/apps_prices_scatterplot.png')
    print(f'Визуализация данных находится в файле "data_visualization/apps_prices_scatterplot"')


def visualize_installs_per_genre() -> None:
    """
    Визуализирует распределение установок приложений.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_choice = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    plt.figure(num=4)
    sns.set_style('darkgrid')
    if user_choice == 'All':
        a = sns.kdeplot(data=apps_df['Installs'], color='Navy', fill=True)
        a.set_title(f'Распределение установок приложений', size=40)
    elif user_choice in genres:
        a = sns.kdeplot(data=apps_df[(apps_df['Genres'] == f'{user_choice}')]['Installs'], color='Navy', fill=True)
        a.set_title(f'Распределение установок приложений в жанре\n{user_choice}', size=40)
    else:
        print('Такого жанра не существует')
        return
    a.set_xlabel(xlabel='Кол-во установок, сотен тыс.', size=20)
    a.set_ylabel(ylabel='Частота', size=20)
    figure = a.get_figure()
    plt.show()
    figure.savefig(f'data_visualization/apps_installs_{user_choice}.png')
    print(f'Визуализация данных находится в файле "data_visualization/apps_installs_{user_choice}"')


def visualize_optimal_app_size_per_genre() -> None:
    """
    Визуализирует зависимость между рейтингом и размером приложений.
    Сохраняет график в файл.
    """
    apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]
    genres = apps_df['Genres'].unique()
    get_all_genres()
    user_choice = input('Выберете жанр для вывода или введите "All" для вывода всех жанров\n')
    plt.figure(num=5)
    plt.grid()
    sns.set_style("darkgrid")
    if user_choice == 'All':
        a = sns.jointplot(data=apps_df, x=apps_df['Size'], y=apps_df['Rating'], color='DarkCyan')
        a.fig.suptitle(f'Зависимость между рейтингом и размером приложений', size=40)
    elif user_choice in genres:
        a = sns.jointplot(data=apps_df, x=apps_df[(apps_df['Genres'] == f'{user_choice}')]['Size'],
                          y=apps_df[(apps_df['Genres'] == f'{user_choice}')]['Rating'], color='DarkCyan')
        a.fig.suptitle(f'Зависимость между рейтингом и размером приложений в жанре\n{user_choice}', size=40)
    else:
        print('Такого жанра не существует')
        return
    a.fig.tight_layout()
    a.set_axis_labels(xlabel='Размер, Мб', ylabel='Рейтинг', size=20)
    plt.close(5)
    plt.show()
    figure = a.figure
    figure.savefig(f'data_visualization/optimal_app_size_{user_choice}.png')
    print(f'Визуализация данных находится в файле "data_visualization/optimal_app_size_{user_choice}"')
