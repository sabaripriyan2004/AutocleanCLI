def analyze(df):
    report = {}

    for col in df.columns:
        report[col] = {
            "missing": int(df[col].isnull().sum()),
            "dtype": str(df[col].dtype),
            "unique": int(df[col].nunique())
        }

    return report