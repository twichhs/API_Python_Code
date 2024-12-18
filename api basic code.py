from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
import datetime as dt
import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]
def credencial():
    creds= None

    if os.path.exists("token.json"):
        creds= Credentials.from_authorized_user_file("token.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request)
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    try: # ADICIONAR O QUE A API IRA FAZER 
        service = build('calendar','v3', credencial = creds)
        pass
    except HttpError as error:
        print(f"An erros occurred: {error}")