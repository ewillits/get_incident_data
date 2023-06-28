import requests
import csv

clear_csv = open("incident_data.csv", "w")
clear_csv.truncate()
clear_csv.close()

#get all incidents - looping through API calls to create a list of the incidents and offsetting until false
pagerduty_url = "https://api.pagerduty.com/incidents/"
querystring = {"limit": "100", "offset": 0,}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token=INSERT API KEY HERE",
    }
list_of_incidents = []
while True:
    response = requests.request("GET", pagerduty_url, headers=headers, params=querystring)
    #error handling if not 200 response - mostly for 10k incident limit
    if response.status_code not in range(200,299):
        print(response.json())
        break
    list_of_incidents.extend(response.json()["incidents"])
    querystring["offset"] += 100
    if response.json()["more"] is False:
        print("Completed list of incidents.")
        break

#create dictionary from list of incidents, adding unique incidents and incrementing duplicate incidents
incident_dictionary = {}
incident_count = 0
for each_incident in list_of_incidents:
    if each_incident["title"] in incident_dictionary:
        incident_dictionary[each_incident["title"]] += 1
        incident_count += 1
    else:
        incident_dictionary.update({each_incident["title"]:1})
        incident_count += 1

#print for user output
print("Completed analysis of "+str(incident_count)+" incidents.")

#CSV writer - opens a csv with defined fields to be written to
with open("incident_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Incident_Title","Incident_Count"])
    writer.writerows(incident_dictionary.items())