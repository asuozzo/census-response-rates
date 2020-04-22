import os
import requests
import pandas as pd

key = os.environ["CENSUS_KEY"]

def get_response_rate(geog_for, geog_in=None):
    params = {
        "get":"NAME,GEO_ID,DRRALL,DRRINT,CRRALL,CRRINT,RESP_DATE",
        "for":geog_for,
        "key":key
    }
    if geog_in:
        params["in"] = geog_in
    
    r = requests.get("https://api.census.gov/data/2020/dec/responserate", params=params)
    data = r.json()
    rr = pd.DataFrame(data[1:],columns=data[0])
    
    return rr


if __name__=="__main__":
    
    # fill in your state's fips code here
    STATE_FIPS = "50"
    
    # get national and state-by-state response rates
    rr_us = get_response_rate("us:1")
    rr_states = get_response_rate("state:*")
    
    # get response rate for all counties in your state
    rr_county = get_response_rate("county:*","state:{0}".format(STATE_FIPS))
    rr_towns = get_response_rate("county subdivision:*","state:{0}".format(STATE_FIPS))

    # merge all dataframes together
    rr_all = rr_us.append([rr_states, rr_county, rr_towns])

    # save to a file named with the response date. The data is updated daily, so
    # if you run this on multiple days or put it on a cron job you'll end up 
    # with a file for each day and you can plot the numbers over time
    rr_all.to_csv("data/source/responserates_{0}.csv".format(rr_all.iloc[0].RESP_DATE), index=False)