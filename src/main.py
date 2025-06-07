import json
from google_play_scraper import app, Sort, reviews

def run():
    """
    Scrape playstore data for three Ethiopian fintech apps 
    """
    # Scrape data from commerical bank of Ethiopias playstore
    # com.combanketh.mobilebanking

    # Scrape data from Bank of Abyssinias playstore
    # com.boa.boaMobileBanking
    
    # # Scrape data from Dashen Bank
    # # com.dashen.dashensuperapp
    # app_dashen_bank_scrape_result = app(
    #     'com.dashen.dashensuperapp',
    #     lang='en', # defaults to 'en'
    #     country='us' # defaults to 'us'
    # )

    # with open('data/scrape_results/dashen/app_dashen_bank_scrape_result.json', 'w', encoding='utf-8') as f:
    #     json.dump(app_dashen_bank_scrape_result, f, ensure_ascii=False, indent=4)
    
    # print("data/scrape_results/dashen/app_dashen_bank_scrape_result.json")

    review_dashen_bank_scrape_result, review_dashen_continuation_token = reviews(
        'com.dashen.dashensuperapp',
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=50, # defaults to 100
        filter_score_with=5 # defaults to None(means all score)
    )
    print("Scrape Data fetched")
    with open('data/scrape_results/dashen/review_dashen_bank_scrape_result.json', 'w', encoding='utf-8') as f:
        json.dump(review_dashen_bank_scrape_result, f, ensure_ascii=False, indent=4, default=str)
    print("Scrape Data Saved")
    while review_dashen_continuation_token:
        review_dashen_bank_scrape_result, review_dashen_continuation_token = reviews(
            'com.dashen.dashensuperapp',
            continuation_token=review_dashen_continuation_token # defaults to None(load from the beginning)
        )
        print("Scrape Data fetched")
        with open('data/scrape_results/dashen/review_dashen_bank_scrape_result.json', 'a', encoding='utf-8') as f:
            json.dump(review_dashen_bank_scrape_result, f, ensure_ascii=False, indent=4, default=str)
        print("Scrape Data Saved")


if __name__ == "__main__":
    run()
