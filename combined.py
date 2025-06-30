import subprocess
import sys
from src.main import run_all_scrapers as standard_scrapers
from src.report.export_csv import export_articles_to_csv

def run_standard_scrapers():
    print("▶️ Running standard scrapers (CNN, BBC, NYT, Blog)...")
    standard_scrapers()
    print("✅ Standard scrapers finished.")

def run_scrapy_spider():
    print("▶️ Running Scrapy spider (Al Jazeera Sports)...")
    subprocess.run(["scrapy", "crawl", "sports"], cwd="src/scrapers/scrapy_crawler")
    print("✅ Scrapy spider finished.")

def export_csv():
    print("▶️ Exporting all articles to CSV...")
    export_articles_to_csv()
    print("✅ Export completed.")

def main():
    print("""📋 Choose an option:
1. Run all standard scrapers
2. Run scrapy spider
3. Export CSV
4. Run everything (1 + 2 + 3)
""")
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        run_standard_scrapers()
    elif choice == "2":
        run_scrapy_spider()
    elif choice == "3":
        export_csv()
    elif choice == "4":
        run_standard_scrapers()
        run_scrapy_spider()
        export_csv()
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
