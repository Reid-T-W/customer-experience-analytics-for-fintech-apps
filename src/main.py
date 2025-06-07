import json
from google_play_scraper import app

def run():
    """
    Scrape playstore data for three Ethiopian fintech apps 
    """
    # Scrape data from commerical bank of Ethiopias playstore
    # com.combanketh.mobilebanking

    # Scrape data from Bank of Abyssinias playstore
    # com.boa.boaMobileBanking

    # Scrape data from Dashen Bank
    # com.dashen.dashensuperapp
    dashen_bank_scrape_result = app(
        'com.dashen.dashensuperapp',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    with open('data/scrape_results/dashen_bank_result.json', 'w', encoding='utf-8') as f:
        json.dump(dashen_bank_scrape_result, f, ensure_ascii=False, indent=4)

    
    print("Result saved to dashen_bank_result.json")

if __name__ == "__main__":
    run()
