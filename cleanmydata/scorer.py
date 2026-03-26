def score_column(df, col, action):
    missing_ratio = df[col].isnull().mean()

    if action == "drop":
        return 0.9 if missing_ratio > 0.5 else 0.6

    if action in ["mean", "median"]:
        return 0.8 if missing_ratio < 0.3 else 0.6

    if action == "mode":
        return 0.7

    return 0.5