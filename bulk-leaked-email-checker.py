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

        url = 'https://haveibeenpwned.com/api/v3/breachedaccount/' + email
        headers = {"hibp-api-key": HAVE_I_BEEN_PWNED_API_KEY}
        response = requests.get(url, headers=headers)              

        breachs = email + ","    
        for breach in response.json():
            breachs += breach['Name'] + " | "      

        SaveToFile("logs.csv", breachs)
        time.sleep(7)

    except Exception as erro:                
        print(response.text)
        print(response.status_code)              
        print("breachedaccount: " + str(erro))       
        time.sleep(7)         

if __name__ == "__main__":

    emails = LoadFile('emails.txt')

    for email in emails:
        CheckEmail(email)

    
