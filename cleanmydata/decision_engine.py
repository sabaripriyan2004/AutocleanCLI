import pandas as pd

def decide(df, col):
    missing_ratio = df[col].isnull().mean()

    # Try converting to numeric (handle dirty data)
    converted = pd.to_numeric(df[col], errors='coerce')
    numeric_ratio = converted.notnull().mean()

    # If mostly numeric → treat as numeric
    if numeric_ratio > 0.7:

        if missing_ratio > 0.5:
            return "drop"

        # Skew-based decision
        if abs(converted.skew()) > 1:
            return "median"
        else:
            return "mean"

    # Otherwise categorical
    if missing_ratio > 0.5:
        return "drop"

    return "mode"