import matplotlib.pyplot as plt

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

def draw_rating_table(df):
    fig, ax = plt.subplots(layout='constrained')

    table = ax.table(
        cellText = df.values,
        colLabels = ['Интервал рейтинга', 'Количество фильмов', 'Доля, %'],
        loc='center',
        cellLoc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)

    ax.axis('off')
    plt.show()