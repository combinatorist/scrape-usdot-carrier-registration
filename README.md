# scrape-usdot-carrier-registration
This project gets information about different carriers (trucking) from USDOT).

## Caveats
### Base Carrier List (Manually Updated)
The scraper hits each carrier page based on a list.
The August 2020 version of that list is downloaded in the repo, but came from here:
https://ai.fmcsa.dot.gov/SMS/files/FMCSA_CENSUS1_2020Aug.zip

You can get the current list by going to this page:
https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx and downloading the "Motor Carrier Census Information".

## Usage
This project manages python dependencies with pipenv.
If you have it installed, simply run `pipenv install` in the directory.
Next, start a `pipenv shell`.
Then, calls to `python` or `ipython` (for development) will use the correct dependencies.
To run this script, do `python __init__.py` (in the pipenv shell).
