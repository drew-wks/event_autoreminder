# Google Calendar Event Invitee Reminder Email
Automatically send a reminder email to invitees of events you have created in Google Calendar

## Requirements
Google Workspace account: uses Google Calendar and Gmail  
A Google Cloud Project  


## Installation
1. Clone this project into your own Github repository
2. Install the dependencies run `pip install -r requirements.txt`
3. Within CGP, you'll need to enable the Calendar and Gmail APIs for your project
Create a OAuth Client ID. Create a OAuth consent screen if this is your first time  
Define the scopes your application can access:  
- For Google Calendar: https://www.googleapis.com/auth/calendar.readonly  
- For Gmail: https://www.googleapis.com/auth/gmail.send  
Download the credential.json file
4. Activate Github Actions if you haven't already  
5. Create the following secrets in Github Actions:
- GOOGLE_CREDENTIALS_JSON: your google OAuth credential.json
- ORGANIZER_EMAIL: Your organizer email
- ORGANIZER_NAME: Your name
- CALENDAR_ID: Your Google Calendar ID. To get your calendar ID, go to gmail settings. Your primary calendar ID will look like this 'your-email@gmail.com' and you secondary ones will look like this 'abcd1234efgh5678@group.calendar.google.com'. CHoose whichever is appropriate for your use case.
