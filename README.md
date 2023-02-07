# Dataset Name

Dataset Name is a dataset used by X for Y and Z.

## Latest output files

| Type                       | Shapefile                  | FileGDB | CSV                  |
| -------------------------- | -------------------------- | ------- | -------------------- |
| Clipped                    | [dataset_name]()           | NA      |
| Unclipped (Water Included) | [dataset_name_unclipped]() | NA      |
| No Geometry                | NA                         | NA      | [dataset_name.csv]() |

## Additional files

- [Source Data versions]()
- [Related export]()
- [Related export]()

---

## Source data

- dcp_xxx
- dcp_yyy
- dof_xxx

> [notes or table about source data]

## Output files

- File Name A
- File Name B

> [notes or table about output files]

## Data Dictionary

### File Name A

#### column_a

- **Display Name**: `Column A`
- **Description**: Description of the values in this column and their meaning.

#### column_b

- **Display Name**: `Column B`
- **Description**: Description of the values in this column and their meaning.

### File Name B

#### column_a

- **Display Name**: `Column A`
- **Description**: Description of the values in this column and their meaning.

## QAQC

Please refer to the [EDM QAQC web application](https://edm-data-engineering.nycplanningdigital.com) for cross version comparisons

---

## Build process

## Build logic

1. Load input datasets from `edm-recipes` DigitalOcean bucket to a Postgres database

2. ...

3. Publish outputs to `edm-publishing` DigitalOcean bucket in a versioned directory and, if appropriate, the `latest` directory

> [notes about build logic]

## Development

### Setup

1. Clone the repo locally

2. Open the repo in a `Remote Window` in VS Code to utilize this repo's dev container
    > Ensure Docker Desktop is running. Start dev container either when prompted or via the green icon at the bottom left).

3. Confirm setup is working by running a script in the dev container terminal (e.g. `./bash/config.sh`)

### Edit python package requirements

1. Edit package list and/or versions in `requirement.in`

2. Run `./bash.dev_pip_compile.sh` to compile and install packages

### Notes

> If `dev` branch doesn't exist, create it.
>
> Create new branches from and merge to `dev`.
>
> Merging `dev` to `main` should be only be done after thorough testing and stakeholder coordination.
>
> Only `main` has branch protection rules. This means that tests are allowed to fail on `dev`.
>
> If using VS Code's `Format on Save`, ensure the Python formatting provider is set to `black`

### Approach Motivations

Details about the purpose of this dataset and why any noteworthy decisions were made

Details about alternative approaches and why they weren't chosen
