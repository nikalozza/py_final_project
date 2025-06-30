from concurrent.futures import ThreadPoolExecutor
from src.scrapers import cnn_scraper, bbc_scraper, nyt_rss_scraper, blog_scraper

def run_all_scrapers():
    with ThreadPoolExecutor() as executor:
        executor.submit(cnn_scraper.scrape_cnn)
        executor.submit(bbc_scraper.scrape_bbc)
        executor.submit(nyt_rss_scraper.scrape_nyt_rss)
        executor.submit(blog_scraper.scrape_blog)

if __name__ == "__main__":
    run_all_scrapers()
