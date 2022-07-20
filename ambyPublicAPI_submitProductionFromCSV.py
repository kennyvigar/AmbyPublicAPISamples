########
# AMBYINT PRODUCTION API - PYTHON SCRIPT SAMPLE
# 
# The purpose of this sample document is to walk a user or admin through interaction with the Public API
# This script parses a document called ambyintDailyProduction.csv for daily values, and submits each value to a oilProduction, gasProduction, waterProduction, casingPressure, tubingPressure endpoint
# 
# https://api.ambyint.io/documentation/
########


# Import Requirements

import requests #pip install first
from datetime import datetime
import json
import time

# Insert Bearer Token below
# Token is received from the Authorization endpoint for use with all subsequent API calls

authorizeInfo = {
        "Authorization": "Bearer *************",
        "Content-Type": "application/json"
    }


host = "https://api.ambyint.io" 

# Start
print("start")


# Parse CSV
with open("/ambyintDailyProduction.csv", "r") as f_csvFile:
    for row in f_csvFile:
        if "Date" in row: #skip header
            continue
        rawRow = row.strip() #entry we're iterating on
        date, uwi, oilProd, gasProd, waterProd, tubingPress, casingPress = rawRow.split(",") #split row on comma

        formattedDate = int(datetime.strptime(date, "%m/%d/%y").timestamp() * 1000) #timestamp format

        uwi = uwi.replace("/","%2F")
        print(f"- - - - - - - - - - - - - - - - - - - - - - - ")
        print(f"Processing UWI... {uwi}")

        #send oil Prod endpoint using REQUESTS
        if oilProd or oilProd==0:
            oilProdUrl = f"{host}/{uwi}/oilProduction"
            oilData = {
                "timestamp": formattedDate,
                "unit": "m3/d",
                "value": oilProd
            }
            oilDataFormatted = json.dumps(oilData)
            
            r = requests.put(url=oilProdUrl, headers=authorizeInfo, data=oilDataFormatted)
            #r = requests.get(url=oilProdUrl, headers=authorizeInfo)

            print("--- Oil Production") 
            print(oilProdUrl)       
            print(r.status_code)
            print(r.reason)
       
       
        #send gas Prod endpoint using REQUESTS
        if gasProd or gasProd==0:
            gasProdUrl = f"{host}/{uwi}/gasProduction"
            gasData = {
                "timestamp": formattedDate,
                "unit": "e3m3/d",
                "value": gasProd
            }
            gasDataFormatted = json.dumps(gasData)

            r = requests.put(url=gasProdUrl, headers=authorizeInfo, data=gasDataFormatted)
            
            print("--- Gas Production")        
            print(r.status_code)
            print(r.reason)

        #send water Prod endpoint using REQUESTS

        if waterProd or waterProd==0:
            waterProdUrl = f"{host}/{uwi}/waterProduction"
            waterData = {
                "timestamp": formattedDate,
                "unit": "m3/d",
                "value": waterProd
            }
            waterDataFormatted = json.dumps(waterData)

            r = requests.put(url=waterProdUrl, headers=authorizeInfo, data=waterDataFormatted)
            
            print("--- Water Production")        
            print(r.status_code)
            print(r.reason)
            
        # #wellParamTubing endpoint using REQUESTS

        if tubingPress or tubingPress==0:
            tubingPressUrl = f"{host}/{uwi}/tubing" 
            tubingData = {
                "timestamp": formattedDate,
                "unit": "psi",
                "value": tubingPress
            }
            tubingPressDataFormatted = json.dumps(tubingData)

            r = requests.put(url=tubingPressUrl, headers=authorizeInfo, data=tubingPressDataFormatted)
            
            print("--- Tubing Press Production")        
            print(r.status_code)
            print(r.reason)

        # #wellParamCasing endpoint using REQUESTS

        if casingPress or casingPress==0:
            casingPressUrl = f"{host}/{uwi}/casing"
            casingData = {
                "timestamp": formattedDate,
                "unit": "psi",
                "value": casingPress
            }
            casingPressDataFormatted = json.dumps(casingData)

            r = requests.put(url=casingPressUrl, headers=authorizeInfo, data=casingPressDataFormatted)
            
            print("--- Casing Press Production")        
            print(r.status_code)
            print(r.reason)
                  
            
        print(f"Completed Processing UWI... {uwi} for {date}")
        time.sleep(0.1) #100 ms sleep
        print(f"- - - - - - - - - - - - - - - - - - - - - - - ")

print("END")
