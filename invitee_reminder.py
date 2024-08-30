import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime

# Step 0: Assign variables
organizer_email = os.getenv('ORGANIZER_EMAIL')
organizer_name = os.getenv('ORGANIZER_NAME')
calendar_id = os.getenv('CALENDAR_ID')

'''
Step 1: Authenticate and build services
'''
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/gmail.send']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

calendar_service = build('calendar', 'v3', credentials=creds)
gmail_service = build('gmail', 'v1', credentials=creds)


'''
Step 2. Define event trigger (6 hours before event starts)
'''
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
events_result = calendar_service.events().list(
    calendarId=calendar_id, timeMin=now, singleEvents=True,
    orderBy='startTime').execute()
events = events_result.get('items', [])

for event in events:
    start_time = event['start'].get('dateTime', event['start'].get('date'))
    event_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    reminder_time = event_time - datetime.timedelta(hours=6)

    if datetime.datetime.utcnow() > reminder_time:
        continue
    formatted_event_time = event_time.strftime('%A, %d %b %Y at %H:%M')
    event_begins_hhmm = event_time.strftime('%H%M')


'''
Step 7: Send email reminder to attendees
'''
    subject = f"Reminder {event['summary']} today at {event_begins_hhmm} ET"
    body = f"Greetings!\n\nA quick reminder of our team meeting: {formatted_event_time} - {event_begins_hhmm} ET\n\nPlease share your updates into the meeting notes:\n{event.get('description', 'No description provided')}\n\n{organizer_name}\n{organizer_email}"
    
    message = {
        'raw': base64.urlsafe_b64encode(f"From: {organizer_email}\nTo: {organizer_email}\nSubject: {subject}\n\n{body}".encode('utf-8')).decode('utf-8')
    }
    
    gmail_service.users().messages().send(userId="me", body=message).execute()



    # Step 8: Log the events
    print(f"Logging event: {event['summary']} at {event_time.strftime('%H:%M')}")
    print(f"Sent reminder for event: {event['summary']}")
