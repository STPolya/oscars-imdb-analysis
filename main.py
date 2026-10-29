import pandas as pd
from pathlib import Path
from modules.loading import load_files
from modules.preparation import prepare_imdb_titles, prepare_oscar_nominations

BASE_DIR = Path(__file__).parent

OSCAR_FILE = BASE_DIR / 'data' / 'oscar_nominations.csv'
TITLES_FILE = BASE_DIR / 'data' / 'imdb_titles.tsv'
RATINGS_FILE = BASE_DIR / 'data' / 'imdb_ratings.tsv'

raw_nominations = load_files(OSCAR_FILE, ';')
nominations = prepare_oscar_nominations(raw_nominations )

ratings = load_files(RATINGS_FILE, '\t')

raw_titles = load_files(TITLES_FILE, '\t', dtype={'runtimeMinutes': str})
titles = prepare_imdb_titles(raw_titles)

nominations_ratings = nominations.merge(
    ratings[['tconst', 'averageRating', 'numVotes']],
    left_on='FilmId',
    right_on='tconst',
    validate='many_to_one'
).drop(columns=['tconst'])

# первый вопрос
best_picture_winners = nominations_ratings.loc[
    (nominations_ratings['Winner'] == True) & (nominations_ratings['CanonicalCategory'] == 'BEST PICTURE'),
    ['Year', 'CanonicalCategory', 'Film', 'Winner', 'averageRating']
]
best_picture_winners.to_csv('best_picture_winners.csv', sep=';', index=False)





