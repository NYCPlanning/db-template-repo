# Inspect a shapefile
from python.utils import load_shapefile

DATA_DIRECTORY = ".data/inspect_shapefile"


def run_inspection() -> None:
    data = load_shapefile(
        directory=DATA_DIRECTORY, filename="cbbr_submissions_poly_shapefile.zip"
    )
    print(data.iloc[0])


if __name__ == "__main__":
    run_inspection()
