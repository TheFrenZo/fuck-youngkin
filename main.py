import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def main():
    subject = "I'm concerned about my son's teacher in Roanoke"
    with open("body.txt") as f:
        body = f.read()

    
