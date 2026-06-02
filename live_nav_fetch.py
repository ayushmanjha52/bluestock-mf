import requests
import pandas as pd
import os

def fetch_and_save_nav(scheme_code, scheme_name, output_dir='data/raw'):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        json_data = response.json()
        meta = json_data.get('meta', {})
        data_list = json_data.get('data', [])
        
        if not data_list:
            print(f"No data for {scheme_code}")
            return None
        
        df = pd.DataFrame(data_list)
        df['scheme_code'] = scheme_code
        df['scheme_name'] = meta.get('scheme_name', scheme_name)
        df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
        df['nav'] = pd.to_numeric(df['nav'], errors='coerce')
        df = df.sort_values('date', ascending=False).reset_index(drop=True)
        
        filename = f"NAV_{scheme_code}_{scheme_name.replace(' ', '_')}.csv"
        filepath = os.path.join(output_dir, filename)
        df.to_csv(filepath, index=False)
        
        latest = df.iloc[0]
        print(f" {scheme_name} ({scheme_code}) → Latest NAV: {latest['nav']} on {latest['date'].strftime('%d-%m-%Y')}")
        print(f"   Saved: {filename} | Records: {len(df)}")
        return df
    except Exception as e:
        print(f" Error for {scheme_code}: {e}")
        return None


if __name__ == "__main__":
    os.makedirs('data/raw', exist_ok=True)
    
    schemes = [
        {"code": 125497, "name": "HDFC Top 100 Direct"},
        {"code": 119551, "name": "SBI Bluechip"},
        {"code": 120503, "name": "ICICI Bluechip"},
        {"code": 118632, "name": "Nippon Large Cap"},
        {"code": 119092, "name": "Axis Bluechip"},
        {"code": 120841, "name": "Kotak Bluechip"},
    ]
    
    for s in schemes:
        fetch_and_save_nav(s["code"], s["name"])
    
    print("\n All live NAV data fetched successfully!")
