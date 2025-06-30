# PY Final Project - News Aggregator

This project collects news articles from various sources (BBC, CNN, NYT, PromptCloud Blog, Al Jazeera Sports), saves them to a PostgreSQL database, and supports exporting them to CSV files.

---

## 1. Requirements

* Windows OS
* Python 3.10 or higher
* PostgreSQL running locally (with a `final_project` database)

---

## 2. Setup

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: PostgreSQL Setup

Make sure PostgreSQL is running and `settings.yaml` is filled correctly with your database credentials:

File: `src/config/settings.yaml`

```yaml
database:
  url: postgresql+psycopg2://postgres:yourpassword@localhost:5432/final_project_db
```

---

run this once per each terminal session : $env:PYTHONPATH="."

## 3. Running Scrapers (except Scrapy Spider)

Run the following command from the root directory:

```bash
python src/main.py
```

This runs all scrapers listed in `scrapers.yaml` (BBC, CNN, NYT RSS, Blog, Session scraper).

---

## 4. Running Reuters Scrapy Spider

Navigate to the correct folder and set Python path:

```bash
$env:PYTHONPATH=(Get-Location).Path; cd src/scrapers/scrapy_crawler; scrapy crawl sports
```

---

## 5. Exporting Articles to CSV

To export all articles from the database into `articles_export.csv`:

```bash
python src/report/export_csv.py
```

---

## 6. Run Combined CLI

The CLI shows article counts, export option, and filter by source:

```bash
python combined.py
```

---

## 7. Drop All Articles

To drop all articles in the database:

```bash
python src/drop_table.py
```

---

## 8. Run Unit Tests

```bash
python -m unittest tests/test_models.py
python -m unittest tests/test_scrapers.py
```

You can also run them all:

```bash
python -m unittest discover tests
```

---

## 9. Notes

* The CLI script is in `combined.py`
* The Scrapy spider is in `src/scrapers/scrapy_crawler/reuters/spiders/sports_spider.py`
* All YAML config is inside `src/config`

---

## Project Structure

* `src/scrapers/` - Python-based scrapers
* `src/scrapers/scrapy_crawler/` - Scrapy project for Reuters
* `src/data/` - Database and model logic
* `src/report/` - CSV export script
* `tests/` - Unit tests
