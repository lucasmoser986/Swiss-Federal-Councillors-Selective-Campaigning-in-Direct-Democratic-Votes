import requests
import time

with open("/Users/lucasmoser/Desktop/2. Semester/5 Abstimmungsforschung/swissdox/dox_parameters.txt") as file:
    votes = [line.rstrip() for line in file]

 
headers = {
    "X-API-Key": "f6945064-2bee-3ff4-8f1d-2d4f894fa91d",
    "X-API-Secret": "1296ff2fd8836302d3b2cccca73a23a73a338089a8cab6c847de00b3df34cfd3"
}
API_BASE_URL = "https://swissdox.linguistik.uzh.ch/api"
API_URL_QUERY = f"{API_BASE_URL}/query"


for i in range(int(len(votes)/6)):
    yaml = """
        query:
            sources:
                - AZ
                - APPZ
                - BAZ
                - BLZ
                - BZ
                - NLZ
                - NIW
                - OBW
                - URZ
                - ZUGZ
                - SOZ
                - SGT
                - TA
                - TZ
                - HEU
                - TDG
                - TPS
                - TLM
            dates:
                - from: %s
                  to: %s
            languages:
                - de
                - fr
            content:
                AND:
                    - OR:
                        - Abstimmung*
                        - Votation*
                        - votation*
                    - %s
        result:
            format: TSV
            maxResults: 500
            columns:
                - id
                - medium_code
                - medium_name
                - head
                - subhead
                - content
        version: 1.2
    """ % (votes[6*i+4], votes[6*i+5], votes[6*i+3])
     
    data = {
        "query": yaml,
        "name": " ".join([votes[6*i],votes[6*i+2]])[0:45],
        "expirationDate": "2025-05-15"
    }
     
    r = requests.post(
        API_URL_QUERY,
        headers=headers,
        data=data
    )
    print(r.json())
    time.sleep(60)
