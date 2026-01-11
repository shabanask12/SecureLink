import pandas as pd
import os

def check_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "phishing_urls.csv")
    
    print(f"--- Checking file: {file_path} ---")
    
    # 1. Read raw text to see the separator and header
    with open(file_path, 'r', encoding='utf-8') as f:
        print("\n[Raw File Content - First 3 lines]")
        for i in range(3):
            print(f.readline().strip())

    # 2. Try loading with pandas
    print("\n[Pandas Loading Check]")
    try:
        df = pd.read_csv(file_path, header=None, names=['label', 'url'])
        print("First 5 rows loaded by Pandas:")
        print(df.head())
        
        print("\n[Data Stats]")
        print(f"Total rows: {len(df)}")
        print(f"Unique labels found: {df['label'].unique()}")
        
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    check_data()