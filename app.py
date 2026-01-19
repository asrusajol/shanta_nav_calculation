import logging
import os
from scraper import scrape_nav_data
from db import insert_nav_records
from config import LOG_FILE

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename= LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    try:
        logging.info("Nav scraping started")
        records = scrape_nav_data()
        insert_nav_records(records)

        logging.info("NAV scraping completed successfully")
        logging.info(f"Records processed: {len(records)}")

    except Exception as e:
        logging.exception("NAV scraper failed")

if __name__ == "__main__":
    main()