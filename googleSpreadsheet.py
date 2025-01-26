import os
from dotenv import load_dotenv
from faceRecognition import scan
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

key = os.getenv("SERVICE_ACCOUNT_FILE")
creds = Credentials.from_service_account_file(key, scopes = SCOPES)

service = build("sheets", "v4", credentials=creds)

sheet = service.spreadsheets()

spreadsheet_id = "17IYW9cXMTSYT1Tqa3_HUV71a9LRpUgdvGNCXoQlgMt8"

names = [[]]
attendance = [[]]
cell = ""

# result = sheet.values().get(spreadsheetId = spreadsheet_id, range = "A2:A").execute()

# currVal = result.get("values", [])


with open("id.txt", "r") as file:
    max = file.readline()
    max = int(max)
    
    if max == 1:
        scan()
    else:
        for i in range(1, max):
            if scan() == i:
                dataAttend = [1]
                attendance.append(dataAttend)
                cell = "B" + str(i) + ":B"
                break
#print(cell)
with open("names.txt", "r") as file:
    for line in file:
        data = [line.strip()]
        names.append(data)

body1 = {"values": names}
body2 = {"values": attendance}

sheet_write = sheet.values().update(spreadsheetId = spreadsheet_id, range = "A1:A", valueInputOption = "RAW", body = body1).execute()
sheet_write = sheet.values().update(spreadsheetId = spreadsheet_id, range = cell, valueInputOption = "RAW", body = body2).execute()


