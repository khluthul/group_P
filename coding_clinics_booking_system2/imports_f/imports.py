'''
here we create all the imports needed throughout
the program and call them from this file to main
'''
# import statement for OAuth 2.0
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle # (saving an object to a file)
import os.path # path finder
import datetime