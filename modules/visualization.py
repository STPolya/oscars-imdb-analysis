def draw_rating_bar(df, ax):
    ax.bar(df['rating_range'], df['film_count'])
    ax.set_title('Распределение рейтингов IMDb')
    ax.set_xlabel('Интервал рейтинга IMDb')
    ax.set_ylabel('Количество фильмов')

def draw_rating_scatter(df, ax):
    ax.scatter(df['Year'], df['averageRating'])
    ax.set_title('Рейтинги IMDb по годам')
    ax.set_xlabel('Годы проведения Оскара')
    ax.set_ylabel('Рейтинг IMDb')