from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

SCOPES = 'https://www.googleapis.com/auth/calendar'

def main():
	plik=open("new.txt","r") #nowy rozklad
	line=plik.read()
	plik.close()
	
	plik2=open("old.txt","r") #stary rozklad
	line2=plik2.read() 
	plik2.close()
	if(line!=line2):
  		print("ZMIANY!!!")
	else:
		print("brak zmian")
		return
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
		creds = tools.run_flow(flow, store)
	service = build('calendar', 'v3', http=creds.authorize(Http()))
    
	service.calendars().clear(calendarId='primary').execute()
	plik=open("new.txt","r") #new
    
	line=plik.readlines()[2:]
	plik.close()
	przedmiot=[]
	for i in range(len(line)):
		os.system('cls')
		przedmiot.append(line[i].split(","))
		name=przedmiot[i][0]+" "+przedmiot[i][1]
		x=name.find("(w)")
		if(x!= -1):
			color="1"
		else:
			color="11"
		timestart= przedmiot[i][2]+"T"+przedmiot[i][3]+":00+02:00"
		timeend=przedmiot[i][2]+"T"+przedmiot[i][5]+":00+02:00"
		event = {
        'summary': name,
        'colorId': color,
        'start': {'dateTime': timestart},
        'end': {'dateTime': timeend}
        }
        
		print('%d of %d' %(i+1,len(line)))
		event = service.events().insert(calendarId='primary', body=event).execute()
        
if __name__ == '__main__':
    main()
   

