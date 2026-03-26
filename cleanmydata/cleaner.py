import pandas as pd
from cleanmydata.decision_engine import decide
from cleanmydata.scorer import score_column

def clean(df):
    print("\nCleaning data (intelligent mode)...\n")

    cols = list(df.columns)
    report = []

    for col in cols:
        action = decide(df, col)
        confidence = score_column(df, col, action)

        if action == "drop":
            df = df.drop(columns=[col])
            print(f"{col}: dropped (confidence={confidence})")

        elif action == "mean":
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(df[col].mean())
            print(f"{col}: mean (confidence={confidence})")

        elif action == "median":
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(df[col].median())
            print(f"{col}: median (confidence={confidence})")

        elif action == "mode":
            if not df[col].mode().empty:
                df[col] = df[col].fillna(df[col].mode()[0])
                print(f"{col}: mode (confidence={confidence})")
            else:
                df[col] = df[col].fillna("Unknown")
                print(f"{col}: fallback (confidence={confidence})")

        report.append((col, action, confidence))

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"\nRemoved {before - after} duplicate rows")

    # Summary
    print("\nCleaning Summary:")
    for col, action, conf in report:
        print(f"{col} -> {action} (confidence={conf})")

    print("\nCleaning complete ✅")

    return df