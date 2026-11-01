def prepare_oscar_nominations(df):
    df['Year'] = df['Year'].str.replace('/', '').astype(int)
    df['Winner'] = df['Winner'].astype('boolean').fillna(False)
    df = df.loc[
        (df['Year'] <= 2025) & (df['Year'] >= 1990),
        ['Year', 'CanonicalCategory', 'Film', 'FilmId', 'Winner']
    ]
    df = df.dropna(subset=['Year', 'CanonicalCategory', 'Film', 'FilmId'])

    return df

def prepare_imdb_titles(df):
    df = df.dropna(subset=['startYear'])
    df['startYear'] = df['startYear'].astype(int)
    df = df[(df['startYear'] >= 1989) & (df['startYear'] <= 2024) & (df['titleType'] == 'movie')]

    return df[['tconst', 'primaryTitle', 'startYear']]