# Compare two csvs
from python.utils import load_csv_file

DATA_DIRECTORY = "data/compare_csvs"
MAX_COMPARISON_ROWS = 50

if __name__ == "__main__":
    print("loading csvs ...")
    old_csv = load_csv_file(
        directory=DATA_DIRECTORY, filename="acs_2010_new_030222.csv"
    )
    new_csv = load_csv_file(directory=DATA_DIRECTORY, filename="acs_2010_new.csv")

    print("comparing csvs ...")
    if not len(old_csv) == len(new_csv):
        print("WARNING! Can only compare data of the same length!")
        print(
            f"""
            Files aren't identical lengths
                {len(old_csv):,} rows in old data
                {len(new_csv):,} rows in new data
            """
        )
        print("compare common rows ... TODO")
    else:
        compare_result = old_csv.compare(new_csv, align_axis=0)
        rows_with_diff_count = len(compare_result) // 2

        if rows_with_diff_count == 0:
            print(f"Files are identical ({len(old_csv)} rows)")
        else:
            print(
                f"""
                Files aren't identical
                    {rows_with_diff_count:,} rows out of
                    {len(old_csv):,} rows in old data
                    {len(new_csv):,} rows in new data
                """
            )
            compare_result = compare_result.set_index(
                compare_result.index.set_levels(
                    [f"ID old_data", f"ID new_data"], level=1
                )
            )
            print("showing first {MAX_COMPARISON_ROWS} rows of comparison results\n")
            print(compare_result.head(MAX_COMPARISON_ROWS))
