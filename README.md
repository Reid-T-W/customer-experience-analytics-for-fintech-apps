# customer-experience-analytics-for-fintech-apps

This project focues on analyzing customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for three Ethiopian banks:
Commercial Bank of Ethiopia (CBE)
Bank of Abyssinia (BOA)
Dashen Bank


## Project Structure

```
customer-experience-analytics-for-fintech-apps/
│
├── app/
│   ├── main.py         # Streamlit dashboard app
│   └── utils.py        # (Utility functions, if any)
│
├── data/
│   ├── scrape_cleaned/
│   │   ├── boa-cleaned.csv
│   │   ├── cbe-cleaned.csv
│   │   └── dashen-cleaned.csv
│   └── scrape_results/
│       ├── boa/
│       │   ├── app_boa_bank_scrape_result.json
│       │   └── review_boa_bank_scrape_result.json
│       ├── cbe/
│       │   ├── app_cbe_bank_scrape_result.json
│       │   └── review_cbe_bank_scrape_result.json
│       └── dashen/
│           ├── app_dashen_bank_scrape_result.json
│           └── review_dashen_bank_scrape_result.
│   ├── sentiment/
│   │   ├── boa-sentiment.csv
│   │   ├── cbe-sentiment.csv
│   │   └── dashen-sentiment.csv
├── notebooks/
│   ├── preprocess.ipynb
│   ├── sentiment-analysis.ipynb
├── scripts/
│   └── README.md
├── src/
│   └── main.py
└── .gitignore
└── requirement.txt
```

---

## Key Components

1. Data scrapping

2. Data Cleaning

3. Sentiment Analysis

## How to Run

## Prerequisites

Before reproducing this project, ensure you have the following installed:

- Python 3.x
- Git
- pip (Python package manager)

## Steps to Reproduce

### 1. **Clone the Repository**  
    Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Reid-T-W/customer-experience-analytics-for-fintech-apps.git
    cd customer-experience-analytics-for-fintech-apps
    ```

### 2. Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run Scrapping

```bash
python main.py
```

### 4. Explore Notebooks

- Open any notebook in the `notebooks/` folder with Jupyter or VS Code to view or rerun the analysis.

---

## Extending the Project

- Add more interactive visualizations to the dashboard (scatter plots, time series, etc.)
- Integrate additional meteorological variables.
- Automate data cleaning and EDA for new datasets.

---

## License

This project is for educational and research purposes.

---

## Authors

- Rediet Tadesse
- Kifiya 10 Academy, Week 2 Customer Experinace Analytics for Fintech Apps










2. **Set Up a Virtual Environment (Optional)**
    It is recommended to use a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

