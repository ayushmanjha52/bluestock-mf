# Bluestock MF Capstone Project

## Project Overview
This project builds a complete data analytics pipeline for mutual fund data including data cleaning, SQL database, exploratory analysis, performance metrics, advanced risk analytics, and an interactive Power BI dashboard.

## Folder Structure
BlueStock Project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   └── run_pipeline.py
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
├── sql/
│   ├── schema.sql
│   └── queries.sql
└── README.md

## How to Run the Project
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the master pipeline: `python scripts/run_pipeline.py`
4. Open the Power BI dashboard file from the `dashboard/` folder

## Datasets Used
- NAV History
- Investor Transactions
- Scheme Performance
- Portfolio Holdings
- Fund Master

## Deliverables
- Complete Jupyter Notebooks
- SQLite Database
- Power BI Dashboard (4 pages)
- Final Report & Presentation
- Advanced Analytics outputs

## Author
Ayushman Jha
