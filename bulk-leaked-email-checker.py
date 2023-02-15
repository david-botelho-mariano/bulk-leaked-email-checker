import requests
import time

HAVE_I_BEEN_PWNED_API_KEY = ""

def SaveToFile(filename, data):

    with open(filename, 'a') as file:
        file.write(data + "\n")
    
def LoadFile(filename):

    with open(filename, 'r') as file:
        emails = file.read().splitlines()
        return emails

def CheckEmail(email):

    try:

        time.sleep(7)

        url = 'https://haveibeenpwned.com/api/v3/breachedaccount/' + email
        headers = {"hibp-api-key": HAVE_I_BEEN_PWNED_API_KEY}
        response = requests.get(url, headers=headers)              

        if response.status_code == 404:            
            return

        breachs = email + ","    
        for breach in response.json():
            breachs += breach['Name'] + " | "      

        SaveToFile("logs.csv", breachs)

    except Exception as erro:                
        print(response.text)
        print(response.status_code)              
        print("breachedaccount: " + str(erro))                

if __name__ == "__main__":

    emails = LoadFile('emails.txt')

    for email in emails:        
        CheckEmail(email)
    
