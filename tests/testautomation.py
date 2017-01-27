import requests
import json

"""
 Server has to be started at port 5000
 Test data given is populated in postgresql
 Redis server started on port 6379

"""

username = "plivo1"
password = "20S0KPNOIM"

url = "http://localhost:5000"
testdata = json.loads(open('testcases.json').read())

print "==== Testing Inbound ===="

passed = 0
failed = 0

for i in testdata["inbound"]:
    resp = requests.post(url + "/inbound/sms", json=i["testcase"], auth=(username, password))
    if resp.json()["message"] is not None and resp.json()["message"] == i["message"]:
        passed = passed + 1
    elif resp.json()["error"] is not None and resp.json()["error"] == i["message"]:
        passed = passed + 1
    else:
        failed = failed + 1

print "Passed", str(passed)
print "Failed", str(failed)

passed = 0
failed = 0


print "==== Testing Outbound ===="

for i in testdata["outbound"]:
    if "count" not in i:
        resp = requests.post(url + "/outbound/sms", json=i["testcase"], auth=(username, password))
    else:
        for j in range(50):
            resp = requests.post(url + "/outbound/sms", json=i["testcase"], auth=(username, password))
    if resp.json()["message"] is not None and resp.json()["message"] == i["message"]:
        passed = passed + 1
    elif resp.json()["error"] is not None and resp.json()["error"] == i["message"]:
        passed = passed + 1
    else:
        failed = failed + 1

print "Passed", str(passed)
print "Failed", str(failed)
