from __future__ import print_function
import pickle
import os.path, os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from printRequest import PrintRequest


inProgress = []
todo = []
finished = []
failed = []
requests = [todo, inProgress, finished, failed]

options = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def main():
	"""Shows basic usage of the Sheets API.
	Prints values from a sample spreadsheet.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPES)
			creds = flow.run_local_server()
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('sheets', 'v4', credentials=creds)

	# Call the Sheets API
	sheet = service.spreadsheets()
	result = sheet.values().get(spreadsheetId='1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24',
								range='Form Responses 1').execute()

	values = result.get('values', [])

	if not values:
		print('No data found.')
	else:
		makeSets(values)

def listMenu(list):
	choice = numInput()
	if (type(choice) != str):
		print(list[choice])

def selector():
	while(True):
		print('TODO[0]\nPROGRESS[1]\nFINISHED[2]\nFAILED[3]')
		choice = numInput()
		if (type(choice) == str):
			continue
		printList(choice)

def numInput():
	print("Input selection: (q) to quit (m) to return to menu")
	toReturn = input()
	if (toReturn.lower() == 'q'):
		quit()
	elif (toReturn.lower() == 'm'):
		return 'm'
	else:
		return int(toReturn)


def printList(choice):
	os.system('cls')
	list = requests[choice]
	print('\t NOW VIEWING ' + options[choice] + '\n')
	for x in range(len(list)):
		try:
			print ('[' + str(x) + '] ' + str(list[x]) + '\n')
		except:
			print ("Unable to print")
	listMenu(list)

def makeSets(values):
	rowNum = 1
	for row in values:
		newRequest = PrintRequest(row, rowNum)
		rowNum = rowNum + 1

		if (newRequest.status == '0'):
			todo.append(newRequest)
		elif (newRequest.status == '1'):
			inProgress.append(newRequest)
		elif (newRequest.status == '2'):
			finished.append(newRequest)
		elif (newRequest.status == '3'):
			failed.append(newRequest)
	selector()


if __name__ == '__main__':
	main()
