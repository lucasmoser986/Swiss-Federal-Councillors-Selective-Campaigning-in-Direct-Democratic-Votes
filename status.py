import requests
import json

headers = {
    "X-API-Key": "f6945064-2bee-3ff4-8f1d-2d4f894fa91d",
    "X-API-Secret": "1296ff2fd8836302d3b2cccca73a23a73a338089a8cab6c847de00b3df34cfd3"
}
API_BASE_URL = "https://swissdox.linguistik.uzh.ch/api"
API_URL_STATUS = f"{API_BASE_URL}/status"

r = requests.get(
    API_URL_STATUS,
    headers=headers
)

with open('dox_status.txt', 'w') as f:
    json.dump(r.json(), f)
