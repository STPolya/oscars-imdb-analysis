import numpy as np

def draw_rating_bar(df, ax):
    ax.bar(df['rating_range'], df['film_count'])
    ax.set_title('Распределение рейтингов IMDb')
    ax.set_xlabel('Интервал рейтинга IMDb')
    ax.set_ylabel('Количество фильмов')

def draw_categories_bar(df, ax):
    bars = ax.barh(df['CanonicalCategory'], df['film_share_pct'])
    ax.bar_label(bars, fmt='%.1f%%')

    ax.set_title('Другие награды победителей в категории "Лучший фильм"')
    ax.set_xlabel('Доля фильмов, также выигравших в указанной категории, %')
    ax.set_ylabel('Категория награды')

def draw_rating_scatter(df, ax):
    ax.scatter(df['Year'], df['averageRating'])
    ax.set_title('Рейтинги IMDb по годам')
    ax.set_xlabel('Год наградного сезона')
    ax.set_ylabel('Рейтинг IMDb')

def draw_awards_double_bar(categories, values1, values2, ax):
    x = np.arange(len(categories))
    width = 0.3

    ax.bar(x - width / 2, values1, width, label='Победитель "Лучшего фильма"')
    ax.bar(x + width / 2, values2, width, label='Максимум на церемонии')

    ax.set_title('Количество наград "Лучшего фильма" и максимум наград на каждой церемонии')
    ax.set_xlabel('Год наградного сезона')
    ax.set_ylabel('Количество наград')

    ax.set_xticks(x)
    ax.set_xticklabels(categories)

    ax.legend()

    ax.grid(axis='y', linestyle='--', alpha=0.6)
