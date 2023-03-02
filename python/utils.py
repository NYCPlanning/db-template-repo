import pandas as pd


def load_csv_file(directory: str, filename: str) -> pd.DataFrame:
    # if not directory:
    data = pd.read_csv(f"{directory}/{filename}")
    data.columns = data.columns.str.lower()
    return data
