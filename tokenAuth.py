import requests
import json
from getpass import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

USER = input("Enter your username for DNAC: ")
PASS = getpass("Enter your password for DNAC: ")

BASEURL = "https://sandboxdnac.cisco.com"
authAPI = '/dna/system/api/v1/aut/token'
deviceListAPI = '/dna/intent/api/v1/network-device'


authPayload={}
authHeaders = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

dnaAuth = BASEURL + authAPI

authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(USER, PASS), headers=authHeaders, data=authPayload)
tokenJson = authResponse.json()

TOKEN = tokenJSON['Token']

dnaDeviceList = BASEURL + deviceListAPI

getPayload={}
getHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Auth-Token': TOKEN
}

getResponse = requests.get(dnaDeviceList, headers=getHeaders, data=getPayload)

getJSON = getResponse.json()

pprint(getJSON)
