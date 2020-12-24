import requests
import time
import datetime
while True:
    # Kollar dagens tid och datum som senare används att kolla vilken timma det är
    current_hour = datetime.datetime.now()
    # Hämtar information från hemsidan och sparar det i en lista
    api_get = requests.get('http://sholiday.faboul.se/dagar/v2.1/').json()
    get_days = api_get['dagar']
    get_day = get_days[0]
    #Öppnar/skapar fil
    if current_hour.hour == 00:
        my_file = open('/home/niklas/Python/namnsdag.txt', 'w')
    #Skriver in informationen från information vi hämtade från hemsidan.
    #Och skriver in det i våran nya fil
        my_file.write(str(get_day))
    #programmet sovet tills nästa dag så den uppdaterar namnsdagen
        time.sleep(3600)
