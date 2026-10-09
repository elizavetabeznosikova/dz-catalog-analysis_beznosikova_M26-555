movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
import math


def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    avg = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, avg)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"
def rating_tier(rating):
    if rating >= 7:
        return "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"
print("Фильмы без жанра comedy:")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(f"  {movie['title']}")
print("\nПоиск шедевра (рейтинг > 9.0):")
index = 0
while index < len(movies):
    if movies[index]["rating"] > 9.0:
        print(f"  Найден: {movies[index]['title']} (рейтинг {movies[index]['rating']})")
        break
    index += 1
else:
    print("  Шедевров не найдено")
def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
def normalize_title(title):
    words = title.split()
    capitalized = [word[0].upper() + word[1:] for word in words]
    return " ".join(capitalized)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    hours = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {hours}, жанры: {genres}'
def titles_sorted_by_rating(movies):
    """Список названий фильмов, отсортированных по убыванию рейтинга."""
    return [
        movie["title"]
        for movie in sorted(movies, key=lambda m: m["rating"], reverse=True)
    ]


def top_n_by_rating(movies, n=3):
    """Топ-n фильмов по рейтингу: список кортежей (title, rating)."""
    top = sorted(movies, key=lambda m: m["rating"], reverse=True)[:n]
    return [(movie["title"], movie["rating"]) for movie in top]


def count_by_genre(movies):
    """Словарь {жанр: количество фильмов}, построенный через dict.get()."""
    genres_count = {}
    for movie in movies:
        for genre in movie["genres"]:
            genres_count[genre] = genres_count.get(genre, 0) + 1
    return genres_count


def actor_filmography(movies):
    """Словарь {актер: [список названий фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, [])
            filmography[actor].append(movie["title"])
    return filmography


# Словарь {title: rating} для фильмов с рейтингом выше среднего
above_average = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average_rating(movies)
}
def all_genres(movies):
    """Множество всех уникальных жанров каталога."""
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Множество актеров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры из movies_a, не встречающиеся в movies_b."""
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    """Генератор: лениво отдаёт фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


print("\nВысокие оценки (>= 8.0):")
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
print(f"\nСуммарная длительность фильмов с рейтингом > 7: {total_duration} минут")

def build_report(movies):
    """Единый отчёт по каталогу — объединяет все предыдущие этапы."""
    print("ОТЧеТ ПО КАТАЛОГУ")

    avg = average_rating(movies)
    print(f"Средний рейтинг: {avg}")

    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")
    for title, rating in top_n_by_rating(movies, n=3):
        movie = next(m for m in movies if m["title"] == title)
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(genre_counts.items(), key=lambda item: -item[1]):
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")

build_report(movies)

