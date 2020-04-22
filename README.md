# census-response

Get census self-response rates from the U.S. Census Bureau API. This is the code behind the story "[Vermont Lags in U.S. Census Response](https://www.sevendaysvt.com/OffMessage/archives/2020/04/21/vermont-lags-in-us-census-response)," published 4/21/20.

## How to run this project

Before you get started, you'll need to register for a [Census API key](https://api.census.gov/data/key_signup.html). Once you have that, create a `.env` file in the base directory and save your key to a variable, like so: `CENSUS_KEY=[YOUR-API-KEY-HERE]`. You don't need to enclose your key in quotes.

Create your virtual environment by running `pipenv install`. *If you do not have Pipenv or Python 3.8 installed, this [IRE guide should help](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit#).*

Once that's installed, run `pipenv shell` to enter the virtual environment.

Edit the `STATE_FIPS` variable in the `etl/get_response_rates.py` file to reflect the state you want data for (I have it set to "50", which is Vermont). That script will download response rate numbers for the U.S., every state, and all counties and county subdivisions within the state you specify.

Download the data by running `python etl/get_response_rates.py`. This will save the data to a file with the response date appended; if you run this on multiple days or put it on a cron job, you'll get a file for each day and you can do some change-over-time analysis.

Then run `jupyter lab` and open the `analysis/analyze_response_rates.ipynb` file. This will let you dig into the numbers you just downloaded.

## Caveats

Self-response rates are calculated using total number of households as the denominator. States with higher numbers of second homes will end up with a lower self-response rate because those homes are included in the total household count.

The U.S. Census Bureau also does not mail messaging to P.O. boxes, so rural homes that don't receive mail delivery are not receiving any messaging while in-person outreach is suspended due to the pandemic.