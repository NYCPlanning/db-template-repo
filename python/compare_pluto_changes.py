# Ensure all intended PLUTO changes for specific BBLs appear in the two change files
import pandas as pd

DATA_FILE_DIRECTORY = "data/pluto_corrections_22v3.1_x"
COLUMNS_TO_SORT_BY = [
    "field",
    "reason",
    "bbl",
    "version",
]
PROGRAMMATIC_CHANGE_REASONS = ["Zero lot area", "Normalized owner name"]


def load_csv_file(filename: str) -> pd.DataFrame:
    data = pd.read_csv(f"{DATA_FILE_DIRECTORY}/{filename}")
    data.columns = data.columns.str.lower()
    return data


def export_csv_file(dataframe: pd.DataFrame, filename: str):
    dataframe.to_csv(f"{DATA_FILE_DIRECTORY}/{filename}", index=False)


def compare_inputs_to_changes():
    print("Starting PLUTO changes comparison")

    print("loading csvs ...")
    input_research = load_csv_file("pluto_input_research.csv")
    changes_applied = load_csv_file("pluto_changes_applied.csv")
    changes_not_applied = load_csv_file("pluto_changes_not_applied.csv")
    print("✅")

    print("limiting to relevant records ...")
    # limit input_research
    input_research = input_research.dropna(subset=["bbl"])
    input_research["bbl"] = input_research["bbl"].astype(int)
    input_research = input_research.sort_values(by=COLUMNS_TO_SORT_BY)
    export_csv_file(input_research, "dev_input_research.csv")

    # limit change files
    print(f"{PROGRAMMATIC_CHANGE_REASONS=}")
    changes_applied = changes_applied[
        ~changes_applied["reason"].isin(PROGRAMMATIC_CHANGE_REASONS)
    ]
    changes_not_applied = changes_not_applied[
        ~changes_not_applied["reason"].isin(PROGRAMMATIC_CHANGE_REASONS)
    ]
    print("✅")

    print("combining change files ...")
    combined_changes = pd.concat(
        [
            changes_applied,
            changes_not_applied,
        ]
    ).reset_index(drop=True)
    # reformat certain data to match input_research
    combined_changes["new_value"] = combined_changes["new_value"].apply(
        lambda x: str(x).replace(".0", "")
    )
    combined_changes["new_value"] = combined_changes["new_value"].apply(
        lambda x: str(x).replace("nan", "")
    )

    combined_changes = combined_changes.sort_values(by=COLUMNS_TO_SORT_BY)
    export_csv_file(combined_changes, "dev_combined_changes.csv")
    print("✅")

    print("comparing files ...")
    # ensure same length
    length_difference = len(input_research) - len(combined_changes)
    if length_difference < 0:
        print(
            f"compare_result has {abs(length_difference)} more rows than input_research"
        )
    elif length_difference > 0:
        print(
            f"input_research has {abs(length_difference)} more rows than compare_result"
        )
    else:
        print(f"Both datasets have {len(input_research)} rows")

    compare_result = input_research.compare(combined_changes, align_axis=0)
    rows_with_diff_count = len(compare_result) // 2
    # compare_result = compare_result.set_index(
    #     compare_result.index.set_levels(
    #         [f"ID {dataset_id_a}", f"ID {dataset_id_b}"], level=1
    #     )
    # )

    if rows_with_diff_count == 0:
        print("Records are identical")


def inspect_pluto_records():
    print("loading csvs ...")
    pluto = load_csv_file("pluto.csv")
    print(pluto.info())
    print("✅")


if __name__ == "__main__":
    # compare_inputs_to_changes()
    inspect_pluto_records()
