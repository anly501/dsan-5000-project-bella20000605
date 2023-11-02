import requests
import pandas as pd
import json
import csv

# Define the API endpoint URL
url = "https://datacatalogapi.worldbank.org/ddhxext/ResourceFileData?resource_unique_id=DR0090755&version_id=2023-09-27T16:44:25.8023254Z"

# Make the GET request
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    data = response.json()  # If the response contains JSON data, it can be accessed using the .json() method

else:
    print("Failed to retrieve data. Status code:", response.status_code)

# Print the data it is a dictionary
# print(type(data))

# Extract column names from the "MetaData" section
#method A
columns = [item['ColumnName'] for item in data["MetaData"]]

#method B
# meta_data = data["MetaData"]
# print(meta_data)
# list1=[]
# for item in meta_data:
#     print(item["ColumnName"])
#     list1.append(item["ColumnName"])
# print(list1)
# columns = [item["ColumnName"] for item in meta_data]


# Extract data from the "Details" section
details = data["Details"]
rows = []
for chunk in details:
    row=[]
    for key,value in chunk.items():
    # Check if the value is None and replace it with an empty string if needed
        value = value if value is not None else ''
        row.append(value)
    rows.append(row)
print(rows)


# Write data to a CSV file
with open('./api_python.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(columns)
    
    # Write the data rows
    csv_writer.writerows(rows)

print("CSV file 'api_python.csv' has been created.")

