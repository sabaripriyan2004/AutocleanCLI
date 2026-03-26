import pandas as pd

def load(filepath: str):
    print("Loading file...")

    df = pd.read_csv(filepath)

    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")

    return df