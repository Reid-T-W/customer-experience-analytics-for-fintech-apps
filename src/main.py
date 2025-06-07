import json
from google_play_scraper import app, Sort, reviews

def run_dashen():
    """
    Scrape playstore data for three Ethiopian fintech apps 
    """
    app_dashen_bank_scrape_result = app(
        'com.dashen.dashensuperapp',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    print("CBE App Scrape Data fetched")
    with open('data/scrape_results/dashen/app_dashen_bank_scrape_result.json', 'w', encoding='utf-8') as f:
        json.dump(app_dashen_bank_scrape_result, f, ensure_ascii=False, indent=4, default=str)

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

def run_cbe():
    """
    Scrape playstore data for Commercial Bank of Ethiopia app
    """
    app_cbe_bank_scrape_result = app(
        'com.combanketh.mobilebanking',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    print("CBE App Scrape Data fetched")
    with open('data/scrape_results/cbe/app_cbe_bank_scrape_result.json', 'w', encoding='utf-8') as f:
        json.dump(app_cbe_bank_scrape_result, f, ensure_ascii=False, indent=4, default=str)
    # App ID: com.combanketh.mobilebanking

    review_cbe_scrape_result, review_cbe_continuation_token = reviews(
        'com.combanketh.mobilebanking',
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.NEWEST
        count=50,  # defaults to 100
        filter_score_with=5  # defaults to None (means all scores)
    )
    print("CBE Scrape Data fetched")
    with open('data/scrape_results/cbe/review_cbe_scrape_result.json', 'w', encoding='utf-8') as f:
        json.dump(review_cbe_scrape_result, f, ensure_ascii=False, indent=4, default=str)
    print("CBE Scrape Data Saved")
    while review_cbe_continuation_token and len(review_cbe_scrape_result) > 0:
        review_cbe_scrape_result, review_cbe_continuation_token = reviews(
            'com.combanketh.mobilebanking',
            continuation_token=review_cbe_continuation_token
        )
        print("CBE Scrape Data fetched")
        with open('data/scrape_results/cbe/review_cbe_scrape_result.json', 'a', encoding='utf-8') as f:
            json.dump(review_cbe_scrape_result, f, ensure_ascii=False, indent=4, default=str)
        print("CBE Scrape Data Saved")

def run_boa():
    """
    Scrape playstore data for Bank of Abyssinia app
    # """
    app_boa_bank_scrape_result = app(
        'com.boa.boaMobileBanking',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    print("CBE App Scrape Data fetched")
    with open('data/scrape_results/boa/app_boa_bank_scrape_result.json', 'w', encoding='utf-8') as f:
        json.dump(app_boa_bank_scrape_result, f, ensure_ascii=False, indent=4, default=str)
    # App ID: com.boa.boaMobileBanking

    review_boa_scrape_result, review_boa_continuation_token = reviews(
        'com.boa.boaMobileBanking',
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.NEWEST
        count=50,  # defaults to 100
        filter_score_with=5  # defaults to None (means all scores)
    )
    print("BOA Scrape Data fetched")
    with open('data/scrape_results/boa/review_boa_scrape_result.json', 'w', encoding='utf-8') as f:
        json.dump(review_boa_scrape_result, f, ensure_ascii=False, indent=4, default=str)
    print("BOA Scrape Data Saved")
    while review_boa_continuation_token and len(review_boa_scrape_result) > 0:
        review_boa_scrape_result, review_boa_continuation_token = reviews(
            'com.boa.boaMobileBanking',
            continuation_token=review_boa_continuation_token
        )
        print("BOA Scrape Data fetched")
        with open('data/scrape_results/boa/review_boa_scrape_result.json', 'a', encoding='utf-8') as f:
            json.dump(review_boa_scrape_result, f, ensure_ascii=False, indent=4, default=str)
        print("BOA Scrape Data Saved")

if __name__ == "__main__":
    # run_dashen()
    run_cbe()
    run_boa()
