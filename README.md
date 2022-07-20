# AmbyPublicAPISamples

API Documentation - api.ambyint.io

Ambyint has a public API where clients can send their production data.  These examples were developed for clients who needed some assistance interacting with API endpoints.   Simple NodeJS and Python examples are anomomysed and the endpoints are public facing. 

Unfortunetly, without a valid client id/secret you will not be able to run this code, they are described in comments what the return would look like. 

### Node JS Example
- Install Axios (`npm i axios`)
- Run in terminal with `node <location to script>

This example of code is meant to how a client how to pass an ID and Secret to authenticate to an `authorize` endpoint, which return a `BEARER` token for subsequent API calls (such as the `get Wells` call afterwards)


### Python Example
- Install Requests if needed `apt install python3-requests` or `pip3 install requests`
- Run in terminal with `python 3 <location to script>`

This script assumes you have already authenticated.  This example is to show a client how to parse a CSV of standardized columns, and pass each daily value to a production endpoint. 
