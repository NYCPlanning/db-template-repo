from python.utils import execute_sql_file, get_source_data_versions


if __name__ == "__main__":
    print("Loading source data via python ...")
    execute_sql_file(filename="load_source_data.sql")

    print("Getting source data versions ...")
    source_data_versions = get_source_data_versions()
    print(
        source_data_versions.to_markdown(
            tablefmt="github",
            intfmt=",",
        )
    )
