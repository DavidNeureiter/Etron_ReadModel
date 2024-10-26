import requests
import json

# Load configuration from the external JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

url_template = config["url_template"]
headers = config["headers"]

# Open a file to write responses
with open('responses.txt', 'w', encoding='utf-8') as file:
    # Loop through IDs from 0 to 1000
    for i in range(1001):
        # Format the URL with the current ID
        url = url_template.format(i)
        
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Write the response for each ID into the file
        file.write(f"Response for ID {i}:\n{response.text}\n\n")

print("Responses have been written to responses.txt.")
