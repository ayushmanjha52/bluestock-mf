import os
import pandas as pd

RAW_DIR = 'data/raw'

def load_all_csvs():
    print("="*80)
    print("TASK 3: Loading all 10 CSV datasets")
    print("="*80)
    csv_files = sorted([f for f in os.listdir(RAW_DIR) if f.endswith('.csv')])
    print(f"Found {len(csv_files)} CSV files\n")
    
    for file in csv_files:
        path = os.path.join(RAW_DIR, file)
        try:
            df = pd.read_csv(path)
            print(f" {file}")
            print(f"   Shape: {df.shape}")
            print(f"   Columns: {df.columns.tolist()}")
            print(df.head(3).to_string())
            print(f"   Nulls: {df.isnull().sum().sum()}")
            if df.duplicated().sum() > 0:
                print(f"    Duplicates: {df.duplicated().sum()}")
            print("    Loaded\n")
        except Exception as e:
            print(f"    Error: {e}\n")


def explore_fund_master():
    print("="*80)
    print("TASK 6: Explore fund_master")
    print("="*80)
    fm = pd.read_csv(os.path.join(RAW_DIR, '01_fund_master.csv'))
    print(f"Shape: {fm.shape}")
    print(f"Unique Fund Houses ({fm['fund_house'].nunique()}): {fm['fund_house'].unique()[:8]}")
    print(f"\nUnique Categories: {fm['category'].unique()}")
    print(f"\nRisk Grades:\n{fm['risk_category'].value_counts()}")
    print(f"\nTotal unique AMFI codes: {fm['amfi_code'].nunique()}")
    print("="*80)


def validate_amfi_codes():
    print("\n" + "="*80)
    print("TASK 7: Validate AMFI codes")
    print("="*80)
    fm = pd.read_csv(os.path.join(RAW_DIR, '01_fund_master.csv'))
    nh = pd.read_csv(os.path.join(RAW_DIR, '02_nav_history.csv'))
    
    master_codes = set(fm['amfi_code'].dropna().astype(str).str.strip().str.upper())
    history_codes = set(nh['amfi_code'].dropna().astype(str).str.strip().str.upper())
    
    print(f"fund_master unique codes : {len(master_codes)}")
    print(f"nav_history unique codes : {len(history_codes)}")
    print(f"Codes present in both    : {len(master_codes & history_codes)}")
    
    if len(master_codes - history_codes) == 0:
        print("\n All fund_master codes exist in nav_history!")
    else:
        print(f"\n Missing codes: {list(master_codes - history_codes)[:5]}")
    
    print(f"\nData Quality Summary: Coverage = {100 * len(master_codes & history_codes) / len(master_codes):.1f}%")
    print("="*80)


if __name__ == "__main__":
    print(" DAY 1 – PROJECT SETUP + DATA INGESTION STARTED\n")
    load_all_csvs()
    explore_fund_master()
    validate_amfi_codes()
    print("\n Day 1 tasks completed successfully!")
