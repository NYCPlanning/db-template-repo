# Dataset Name
Dataset Name is a datatset used by X for Y and Z.

## Latest output files
Type | Shapefile | FileGDB | CSV
-- | -- | -- | --
Clipped | [dataset_name]() | NA 
Unclipped (Water Included) | [dataset_name_unclipped]() | NA
No Geometry |  NA | NA  | [dataset_name.csv]()

## Additional files
- [Source Data versions]()
- [Datatset Name corrections]()
- [Related export]()
- [Related export]()

---

### Source data
- dcp_xxx
- dcp_yyy
- dof_xxx
> [details or table about source data]

### Build logic
1. Load input datasets from `edm-recipes` DigitalOcean bucket to a Postgres database

2. ...

3. Publish outputs to `edm-publishing` DigitalOcean bucket in a versioned directory and, if appropriate, the `latest` directory

> [details about build logic]

### Output files
- Output files:
> [details or table about outputs]

### QAQC
Please refer to the [EDM QAQC web application](https://edm-data-engineering.nycplanningdigital.com) for cross version comparisons

## Development
1. Clone repo

2. Open the repo in a `Remote Window` in VS Code to utilize this repo's dev container
> Ensure Docker Desktop is running. Start dev container either when prompted or via the green icon at the bottom left).

3. Confirm setup is working by running a script via dev container terminal (e.g. `./bash/config.sh`)

4. Open and merge branches to `dev` before `main`

---

### Approach Motivations
Details about the purpose of this dataset and why any noteworthy decisions were made.

Details about alternative approaches and why they weren't chosen.