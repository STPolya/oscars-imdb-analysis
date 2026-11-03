def prepare_oscar_nominations(df):
    df['Year'] = df['Year'].str.replace('/', '').astype(int)
    df['Winner'] = df['Winner'].astype('boolean').fillna(False)
    df = df.loc[
        (df['Year'] <= 2025) & (df['Year'] >= 1990),
        ['Year', 'CanonicalCategory', 'Film', 'FilmId', 'Winner']
    ]
    df = df.dropna(subset=['Year', 'CanonicalCategory', 'Film', 'FilmId'])

    return df