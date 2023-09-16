# IMDB metadata extractor

Extracts a movie metadata from the IMDB using the JSON+LD annotations provided in the
IMDB HTML pages. 

## Installing

```
$ pip install imdb-metadata-extractor
```

## Usage

```
$ imdb-metadata-extractor tt0058700
{
    "name": "The Last Man on Earth",
    "poster": "https://m.media-amazon.com/images/M/MV5BODA0MzRhYWMtMGUxYi00NmQyLWEyOWYtMGI4NjM3ZDE5NTEyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    "description": "When a disease turns all of humanity into the living dead, the last man on earth becomes a reluctant vampire hunter.",
    "rating": 6.7,
    "release": "1964-05-06",
    "genre": "Drama; Horror; Sci-Fi",
    "actors": "Vincent Price; Franca Bettoia; Emma Danieli"
}
```

By default the results are displayed in the STDOUT, but It's also possible to set a output file and
format (JSON, CSV of XLSX).

```
$ imdb-metadata-extractor tt0058700 --output tt0058700.csv --format csv
```