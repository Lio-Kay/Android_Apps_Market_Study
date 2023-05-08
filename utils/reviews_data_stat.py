import pandas as pd
import numpy as np

from apps_data_stat import get_and_validate_app_data


apps_df = get_and_validate_app_data()
# Отбрасываем субжанры, в которых всего 1-3 приложения
apps_df['Genres'] = apps_df['Genres'].str.split(';').str[0]


def get_and_validate_reviews_data():
    with open(file='../data/googleplaystore_user_reviews.csv', mode='r', encoding='utf-8') as apps_data:
        raw_reviews_df = pd.read_csv(apps_data)
    # Объединяем данные из googleplaystore_user_reviews.csv и googleplaystore.csv через 'App'
    merged_reviews_df = pd.merge(left=apps_df, right=raw_reviews_df, on='App', how='inner')
    # Удаляем строки если есть NaN в столбцах Sentiment, Translated_Review
    merged_reviews_df = merged_reviews_df.dropna(subset=['Sentiment', 'Translated_Review'])
    # Получаем число негативных, нейтральных и положительных Sentiment по каждому жанру
    grouped_sentiment_category_count = merged_reviews_df.groupby(['Genres', 'Sentiment'])\
        .agg({'App': 'count'}).reset_index()
    # Получаем общее число Sentiment по каждому жанру
    grouped_sentiment_category_sum = merged_reviews_df.groupby(['Genres']).agg({'Sentiment': 'count'}).reset_index()
    # Группируем два датасета по жанру
    validated_reviews_df = pd.merge(left=grouped_sentiment_category_count,
                                    right=grouped_sentiment_category_sum, on=['Genres'])
    # Создаем новый столбец показывающий % типа отзыва от общего числа
    validated_reviews_df['Sentiment_Share'] = validated_reviews_df.App / validated_reviews_df.Sentiment_y
    # Жанр Adventure содержит только негативные и положительные отзывы, отбрасываем его
    validated_reviews_df = validated_reviews_df.groupby('Genres').filter(lambda x: len(x) == 3)
    return validated_reviews_df


reviews_df = get_and_validate_reviews_data()


def get_all_remaining_genres():
    genres = reviews_df['Genres'].unique()
    counter = 0
    for number, a in enumerate(genres, start=1):
        if counter < 4:
            print(number, a.replace('_', ' '), end=' | ')
            counter += 1
        else:
            print(number, a.replace('_', ' '))
            counter = 0


