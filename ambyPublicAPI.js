//
//This script is to demonstrate examples in Javascript for using
//the Ambyint public-api.
//
//https://api.ambyint.io/documentation/
//
////////////////////////////////////////////////////////////////

//Import Axios for API Calls
//https://www.npmjs.com/package/axios
// -  npm i axios

const axios = require("axios");

// TODO ensure ID and Secret are removed from this script
// https://medium.com/codait/environment-variables-or-keeping-your-secrets-secret-in-a-node-js-app-99019dfff716

const id = "";
const sec = "";

const env = "api.ambyint.io";

//Auth Function
//Used to get a bearer token from a client id/secret POST

const authorize = async () => {
  try {
    url = `https://${env}/authorize`;
    const data = {
      id: id,
      secret: sec,
    };

    const response = await axios.post(url, data);

    return response.data;
  } catch (err) {
    console.log(`error catch ${err}, ${err.config}`);
  }
};

const getWells = async (env, accessToken) => {
  try {
    const url = `https://@${env}/wells/`;
    const response = await axios.get(url, {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
    });
    console.log(`Environment ${env}`);
    return response.data;
  } catch (e) {
    console.log(e);
  }
};

const authenticateAndGetWells = async () => {
  const authReturn = await authorize();
  const accessToken = authReturn.accessToken;

  //Get well's unique well identifier, 
  const wellList = await getWells(env, accessToken);
  for (well of wellList) {
    console.log(well.uwi);
  }
};

authenticateAndGetWells();
