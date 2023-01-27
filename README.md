# PLUTO Plus
PLUTO with monthly zoning data updates for use in ZoLa portal


## Approach
- Use the Zoning Tax Lot database
    - The scale of the tax lots in the Zoning Tax Lot database is at the base bbl level whereas the scale of the tax lots in PLUTO is the billing bbl level.  Therefore, there is not a one-to-one match between records in the Zoning Tax Lot database and PLUTO.  Additionally, the spatial data in the Zoning Tax Lot database is updated monthly, while the spatial data in PLUTO is updated with each update, so if zoning data is applied to new, split, or merged lots and these changes are not yet reflected in PLUTO the zoning data would be incorrectly represented.
- Updating PLUTO monthly
    - Unfortunately, because of data issues with DOF source data, it would be impractical to build, QA, and release PLUTO monthly given the current amount of time it takes to produce and release a quarterly PLUTO update; Data Engineering would perpetually be working on PLUTO.
- Update PLUTO monthly but hold all source data but zoning data constant
    - Currently known negative impacts of this project to current processes:
        - Need to disable automatic weekly pulls of [CAMA and PTS](https://github.com/NYCPlanning/db-pluto/actions)
        - Need to disable routine open data update in [data library](https://github.com/NYCPlanning/db-data-library/actions)
    - Currently known positive impacts of this project to current processes:
        - Getting to more routine PLUTO updates 

### Inputs
...

### Logic
...

### Outputs
...

### QAQC
...

## Development
1. Clone repo
2. Open the repo in a `Remote Window` in VS Code to utilize this repo's dev container
> Ensure Docker Desktop is running. Start dev container either when prompted or via the green icon at the bottom left).

3. Confirm setup is working by running a script via dev container terminal (e.g. `./bash/config.sh`)

4. Open and merge branches to `dev` before `main`

## Approach Motivations
The zoning district boundaries and tax lot level zoning information become out of sync in ZoLa.  

[Here](https://zola.planning.nyc.gov/l/lot/3/388/12?aerial-year=aerials-2016&layer-groups=%5B%22building-footprints%22%2C%22commercial-overlays%22%2C%22street-centerlines%22%2C%22subway%22%2C%22tax-lots%22%2C%22zoning-districts%22%5D&print=false&search=false&selectedFirm=%5B%22A%22%2C%22Shaded%20X%22%2C%22V%22%5D&selectedOverlays=%5B%22C1-1%22%2C%22C1-2%22%2C%22C1-3%22%2C%22C1-4%22%2C%22C1-5%22%2C%22C2-1%22%2C%22C2-2%22%2C%22C2-3%22%2C%22C2-4%22%2C%22C2-5%22%5D&selectedPfirm=%5B%22A%22%2C%22Shaded%20X%22%2C%22V%22%5D&selectedZoning=%5B%22BP%22%2C%22C1%22%2C%22C2%22%2C%22C3%22%2C%22C4%22%2C%22C5%22%2C%22C6%22%2C%22C7%22%2C%22C8%22%2C%22M1%22%2C%22M2%22%2C%22M3%22%2C%22PA%22%2C%22R1%22%2C%22R10%22%2C%22R2%22%2C%22R3%22%2C%22R4%22%2C%22R5%22%2C%22R6%22%2C%22R7%22%2C%22R8%22%2C%22R9%22%5D&shouldRefresh=false#18.35/40.683849/-73.982711) is an example as of January 26, 2023.  The lot level zoning information for bbl 3003880012 shows an M1-2 zoning district, but the zoning boundaries show that the lot is in a R7A zoning district.  The application for this rezoning can be found in ZAP [here](https://zap.planning.nyc.gov/projects/2019K0461).

The reason why zoning district boundaries and tax lot level zoning information become out of sync is because zoning district boundaries are updated monthly, but PLUTO, which provides the tax lot level zoning information is updated at best quarterly.

Out of date tax lot zoning information in ZoLa has become a problem for zoning applicants, developers, and others who use ZoLa data to inform decisions and it has resulted in the stalling of procedures.

The solution to the issue is to update the tax lot level zoning data monthly.