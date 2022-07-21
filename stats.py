from googleapiclient.discovery import build
from google.oauth2 import service_account
from pandasgui import show
import pandas as pd


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
# https://docs.google.com/spreadsheets/d/1aCpeUYfHtljYXj0NvdiI9tJVbIDuGpETf1UaWm13AKQ/edit#gid=52637800
Spreadsheet_ID = '1aCpeUYfHtljYXj0NvdiI9tJVbIDuGpETf1UaWm13AKQ'
Team_Members = 'Team Members!B3:E52'

# Google API Key = AIzaSyD66aobgceKpDcWlkmNZx4YDzMLhBEG0tQ
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=Spreadsheet_ID,range=Team_Members).execute()
values = result.get('values', [])

#show(values)
#print(values[3][0])


starting = 0
for i in range(len(values)):
        print("Username: {}\nTeam: {}\nPoints: {}\nSubmissions: {}".format(values[starting][0], values[starting][1], values[starting][2], values[starting][3]))
        print("----")
        starting += 1





# Display both array and array value do [array][value]. Ex: values[3][2] will show 78

