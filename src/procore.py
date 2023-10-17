import os
import json

from dotenv import load_dotenv
load_dotenv()

import requests

BASE_URL = "https://app.procore.com"

# Access Token
# ------------
# Documentation: https://developers.procore.com/reference/rest/v1/authentication?version=1.0#get-or-refresh-an-access-token

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

endpoint = "/oauth/token"

headers = {"Content-Type": "application/json"}

body = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

response = requests.post(
    url=f"{BASE_URL}{endpoint}",
    headers=headers,
    data=json.dumps(body)  # Convert the dictionary to a JSON string
)

access_token_data = response.json()

access_token = access_token_data["access_token"]
print(f"First ten characters of the Access Token: {access_token[:10]}")

# Companies
# ---------
# Documentation: https://developers.procore.com/reference/rest/v1/companies?version=1.0#list-companies

endpoint = "/rest/v1.0/companies"

headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(
    url=f"{BASE_URL}{endpoint}",
    headers=headers
)

company_data = response.json()

# print response for review
#print(json.dumps(company_data, indent=4))

# save first (0th) "id" from the list which will correspond to RO
company_id = company_data[0]["id"]

# Projects
# --------
# Documentation: https://developers.procore.com/reference/rest/v1/projects?version=1.1#list-projects

endpoint = "/rest/v1.1/projects"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Procore-Company-Id": f"{company_id}"
}

params = {
    "company_id": f"{company_id}"
}

response = requests.get(
    url=f"{BASE_URL}{endpoint}",
    headers=headers,
    params=params
)

project_data = response.json()

# print response from first (0th) project for review
#print(json.dumps(project_data[0], indent=4))

# Loop through each item to get project names and IDs
for project in project_data:
    print(end="") # just a placeholder
    #print(f"{project['id']}: {project['name']}")

# Project Folders
# ---------------
# Documentation: https://developers.procore.com/reference/rest/v1/project-folders-and-files?version=1.0#list-project-folders-and-files

endpoint = "/rest/v1.0/folders"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Procore-Company-Id": f"{company_id}"
}

params = {
    "project_id": "1668030" # hard-coded South Lamar project ID
}

response = requests.get(
    url=f"{BASE_URL}{endpoint}",
    headers=headers,
    params=params
)

folders_data = response.json()

# Loop through each item to get folder names and IDs
for folder in folders_data["folders"]:
    print(end="") # just a placeholder
    #print(f"{folder['id']}: {folder['name']}")

# Individual Folder
# -----------------
# Documentation: https://developers.procore.com/reference/rest/v1/project-folders-and-files?version=1.0#show-project-folder

# To work on together

# RFIs
# ----
# Documentation: https://developers.procore.com/reference/rest/v1/rfis?version=1.0#list-rfis

# To work on individually