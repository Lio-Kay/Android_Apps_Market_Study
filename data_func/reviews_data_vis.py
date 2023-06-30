import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from reviews_data_stat import get_and_validate_reviews_data


sns.set_theme(style='dark')

reviews_df = get_and_validate_reviews_data()

print(reviews_df['Genres'].unique())

data = pd.DataFrame({'Positive reviews': reviews_df[(reviews_df['Sentiment_x'] == 'Positive')]['Sentiment_Share'],
        'Neutral reviews': reviews_df[(reviews_df['Sentiment_x'] == 'Neutral')]['Sentiment_Share'],
        'Negative reviews': reviews_df[(reviews_df['Sentiment_x'] == 'Negative')]['Sentiment_Share']},
        index=reviews_df['Genres'].unique())

data.plot(kind='bar', stacked=True, color=['Green', 'Gray', 'Red'])
plt.show()
