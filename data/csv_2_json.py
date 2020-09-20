import csv 
import json 
  
def make_json(csvFilePath, jsonFilePath): 

    data = {} 
      
    # Open a csv reader called DictReader 
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for rows in csvReader: 
            key = rows['movieId'] 
            data[key] = rows 
  
    # Open a json writer, and use the json.dumps()  
    # function to dump data 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(data, indent=4)) 
          

csvFilePath = r'combined.csv'
jsonFilePath = r'database.json'
  
make_json(csvFilePath, jsonFilePath)