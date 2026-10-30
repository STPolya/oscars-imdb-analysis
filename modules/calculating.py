import pandas as pd

def calculate_rating_distribution(df):
    bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    group_names = ['1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10']

    df['rating_range'] = pd.cut(df['averageRating'], bins = bins, labels=group_names, right=False, include_lowest=True)

    rating_distribution = (df.groupby('rating_range', as_index=False, observed=False)
        .agg(film_count = ('averageRating', 'count'))
        .assign(film_share_pct = lambda x: round((x['film_count'] / 36) * 100, 1))
    )

    return rating_distribution