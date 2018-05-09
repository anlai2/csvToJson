import csv, json

csvFilePath = "cleaned_hm.csv" # CSV file to be translated
jsonFilePath = "happy.json" # JSON file to be created

# Read the CSV and add the data to a dictionary...
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["hmid"]
        data[hmid] = csvRow

# Add data to a root node...
root = {}
root["happy"] = data

# Write data to JSON file...
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent=4))
