# scrape-usdot-carrier-registration
This project gets information about different carriers (trucking) from USDOT).

## Caveats
### Base Carrier List (Manually Updated)
The scraper hits each carrier page based on a list.
The August 2020 version of that list is downloaded in the repo, but came from here:
https://ai.fmcsa.dot.gov/SMS/files/FMCSA_CENSUS1_2020Aug.zip

You can get the current list by going to this page:
https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx and downloading the "Motor Carrier Census Information".

### Schema
Right now, the `results` from each page make sense in python.
It's a list of included cargo (types) and vehicle types.
However, when it is written into csv's, the lists aren't valid columns.
They also only align by row number.

I plan to pivot them into long lists and include a carrier number they explicitly join to.
Then, we should also include all the carrier level attributes in a third csv that can join to both.

### Known Bugs
There are some known bugs (and desired features) in [./todo.txt].

## Usage
This project manages python dependencies with pipenv.
If you have it installed, simply run `pipenv install` in the directory.
Next, start a `pipenv shell`.
Then, calls to `python` or `ipython` (for development) will use the correct dependencies.
To run this script, do `python __init__.py` (in the pipenv shell).

## Design / Strategy
To get going quickly, I used Beautiful Soup which is very flexible and easy to write.
I started development in ipython where I could dynamically adjust and retry code.

### Performance
To make the parser faster at scale, we should switch from Beautiful Soup to the Scrapy library.
We can use https://github.com/combinatorist/scrape_mat as a syntax example.

### Page Changes
To make the parser more robust, we should add the `warnings` library and check every assumption about the page structure.
For example, if we don't get any vehicle types listed for a certain carrier, we need to know whether that's because we failed to parse them or the page didn't have them.
For example, we should check whether there are any new or missing html tags.
This will allows us to run with different logging levels.
For testing, to make sure the page structure hasn't changed, we can run with warnings as errors or with a limit on warnings of the same type.
We can run these on a random subset of the carriers (or in a random order) to make sure we aren't just testing the same few pages we've already tested or developed on.
The more syntactic, semantic, and logical assumptions we can test on the page and the scraped results, the better.
Overtime, we may notice slight changes in the page structure, which can generalize over.
We can't guarantee today's parser will work tomorrow, but if it works flexibly for all past versions, we're doing pretty well and we're protected in case they revert.
We also need to add try catch errors so a change to one carrier's page, doesn't stop us from trying other carriers.

### Page Reliability
It may also happen that page isn't always up.
This is one reason, it would be good to record when we pulled each record (as well as their published last modified date).
Then, we can always prioritize scraping the carriers which are new in the file or we haven't checked in a long time.

In my first run, I suddenly lost my connection after scraping 4.6K pages.
I still have internet so I assume they are blocking me or their page is just down.
Regardless, it is polite and prudent to use exponential backup when scraping.
This means when there's a connection error, we should wait a set period of time.
Then, if we get another connection error, we should double the wait time and continue.
Once, we are able to connect again, we may start halving the wait time or start over without one.
Ideally, we'd add a tiny bit of randomness to the wait time so we don't get in sync with other periodic loads on the system.

