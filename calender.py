import requests
import json
urlAdressToApi=""
for year in range(2016,2067):
    for month in range(1,13):
        for day in range(1,32):
            #define the first date when the programm start
            try:
                urlAdressToApi='https://www.hebcal.com/converter/?cfg=json&gy='+str(year)+'&gm='+str(month)+'&gd='+str(day)+'&g2h=1'
                #the address that i am take the data/api
                url=(urlAdressToApi)
                response=requests.get(url).json()
                #converting to json text
                yearTxt=str(response['gy'])
                monthTxt=str(response['gm'])
                dayTxt=str(response['gd'])
                hebrewTxt=str(response['hebrew'])
                #take data
                print(dayTxt+'/'+monthTxt+'/'+yearTxt+'\n')
                print(hebrewTxt)
                #checking fixability (בדיקת תקינות קבלת הנתונים אבך שורות האלו תוכל למחוק אותם והן אינן הכרחיות)
                f = open("calender.txt", "a")
                f.write(dayTxt+'/'+monthTxt+'/'+yearTxt+'\n')
                f.write(hebrewTxt)
                f.close()
            except KeyError:
                break
                #access to file and write on him and close him
                #made in B.N.H(Binyamin Haimson)
    f = open("calender.txt", "a")
    f.write('the end of year\n'+ str(year))
    f.close()
