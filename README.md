# get_incident_data
Grabs incident data over the last 30 days from the time the script runs. Returns up to a total amount of 10,000 records (API limitation). Returns the results in a CSV file for the user to analyze.

## Required API Key
A read-only API key is required on line 14: "Authorization": "Token token=<<INSERT API KEY HERE>>"