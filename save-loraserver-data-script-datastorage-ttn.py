import json
import requests

Application = "arduinosdi1222222222222222"
APIKey = "NNSXS.OAOMV2ADRMBDJZZVWU2QHMDACYEBDJXG2NKNCFY.IT5GJMVYEEJYI6J7LR6A45Y3ONZTBZQQU7JLF4M4SKFUHEEBUNUA"
Fields = "up.uplink_message.decoded_payload,up.uplink_message.frm_payload"
NumberOfRecords = 3
URL = "https://eu1.cloud.thethings.network/api/v3/as/applications/" + Application + "/packages/storage/uplink_message?order=-received_at&limit=" + str(NumberOfRecords) + "&field_mask=" + Fields
Header = { "Accept": "text/event-stream", "Authorization": "Bearer " + APIKey }

#print("\n\nFetching from data storage...\n")

r = requests.get(URL, headers = Header)
JSON = "{\"data\": [" + r.text.replace("\n\n", ",")[:-1] + "]}";

#print("URL: {}\n".format(r.url))
#print("Status: {}\n".format(r.status_code))
print("Response: {}\n".format(r.text))
#print("JSON: ")
#print(json.dumps(json.loads(JSON), indent = 4))
print()
