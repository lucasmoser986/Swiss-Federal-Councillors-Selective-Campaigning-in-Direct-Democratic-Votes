import requests

with open("/Users/lucasmoser/Desktop/2. Semester/5 Abstimmungsforschung/swissdox/dox_ids.txt") as file:
    ids = [line.rstrip() for line in file]
with open("/Users/lucasmoser/Desktop/2. Semester/5 Abstimmungsforschung/swissdox/dox_links.txt") as file:
    links = [line.rstrip() for line in file]    

headers = {
    "X-API-Key": "f6945064-2bee-3ff4-8f1d-2d4f894fa91d",
    "X-API-Secret": "1296ff2fd8836302d3b2cccca73a23a73a338089a8cab6c847de00b3df34cfd3"
}

for i in range(len(ids)):
    API_URL_DOWNLOAD = links[i]
    r = requests.get(
        API_URL_DOWNLOAD,
        headers=headers
    )
    if r.status_code == 200:
        fp = open("./%s.tsv" % (ids[i],), "wb")
        fp.write(r.content)
        fp.close()
        print(ids[i])
    else:
        print(r.text)

