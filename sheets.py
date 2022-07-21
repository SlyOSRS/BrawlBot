from dataclasses import dataclass
import datetime
import os
import sys
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pandasgui import show

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
# https://docs.google.com/spreadsheets/d/1aCpeUYfHtljYXj0NvdiI9tJVbIDuGpETf1UaWm13AKQ/edit#gid=52637800
SAMPLE_SPREADSHEET_ID = '1aCpeUYfHtljYXj0NvdiI9tJVbIDuGpETf1UaWm13AKQ'
SAMPLE_RANGE_NAME = 'Scoreboard!M24:M26'

Noobs_EP = '1s7LpmdO75uArFtMl5_qMZGWEZfG36JD7DOUR3t8WPrQ'
Noobs_EP_Range = 'NEW Member\'s list!A2:E300'

# Google API Key = AIzaSyD66aobgceKpDcWlkmNZx4YDzMLhBEG0tQ
service = build('sheets', 'v4', credentials=creds)
#
## Call the Sheets API
sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()


playerName = 'Scoreboard!L24:N26'
totalPoints = 'Scoreboard!N14:16'
members = 'Team Members!B2:E52'

namesOnly = 'Team Members!B3:B52'
#names = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=playerName).execute()
#
#values = names.get('values', [])

#print(names)
#print('-')

#starting = 0
#for i in range(len(values)):


        #starting += 1
#print(values)

#values = result.get('values', [])
##print(result)
##print("----")
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
playerName = 'Scoreboard!L24:N26'

def whoSentIt(ctx):
        print("Hi")
        print("{} | {} executed !mvp at {} in channel {}".format(ctx.author.display_name, ctx.author.id, datetime.datetime.utcnow(), ctx.author))


def testing(removing_command):
        print("Removing command {}".format(removing_command))

global dice
def rolling(dice:int):
        print('Rolling {} '.format(dice))
        return dice
