# Google Calendar Eevent Autoreminder Email
Automatically send a reminder email to invitees of events you have created in Google Calendar

## Requirements
Google Workspace account  
A Google Cloud Project  

Within GCP,  
You'll need to enable the Calendar and Gmail APIs for your project
Create a OAuth Client ID. Create a OAuth consent screen if this is your first time  
d.	Define the scopes your application can access:  
i.	For Google Calendar: https://www.googleapis.com/auth/calendar.readonly  
ii.	For Gmail: https://www.googleapis.com/auth/gmail.send  
Download the credential.json file  
Put the credential.json in your Github Actions as a new repository secret named 'GOOGLE_CREDENTIALS_JSON'
