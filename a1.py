# Name : Riya Sogani
# Roll No : 2019442
# Group : 6

import datetime
date=datetime.datetime(2019,6,30)
import ssl
import urllib.request

def getLatestRates():
    gcontext = ssl.SSLContext()
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest", context=gcontext)
    data=str(url.read())
    return data

def changeBase(amount, currency, desiredCurrency, date):
    gcontext = ssl.SSLContext()
    url = urllib.request.urlopen("https://api.exchangeratesapi.io/"+str(date), context=gcontext)
    data = str(url.read())
    rate1_start=data.find(currency)+5
    rate1_end=data.find(',',rate1_start)
    rate1=float(data[rate1_start:rate1_end])
    eur=amount/rate1
    rate2_start = data.find(desiredCurrency) + 5
    rate2_end=data.find(',',rate2_start)
    rate2=float(data[rate2_start:rate2_end])
    conversion=eur*rate2
    print(conversion)

def printAscending(json):
    rate_list=[]
    currency_list=[]
    x=json.find(":")
    y=json.find("}")

    for i in range (x+1,y-13,13):
        colon=json.find(':',i+1)
        comma=json.find(',',colon)
        rate=json[colon+1:comma]
        rate_list.append(rate)
    rate_list_last=rate_list[-1]
    z=len(rate_list_last)-1
    rate_list=rate_list[:-1]
    rate_list.append(json[json.find('}')-z:json.find('}')])
    rate_list=sorted(rate_list, key=float)

    for j in range(len(rate_list)):
        a=json.find(rate_list[j])
        currency=json[a-5:a-2]
        currency_list.append(currency)

    for k in range(len(rate_list)):
        print("1 EUR = "+ rate_list[k]+" "+currency_list[k])


def extremeFridays(startDate, endDate, currency):

    start_year=int(startDate[:4])
    start_month=int(startDate[5:7])
    start_day=int(startDate[8:])

    end_year = int(endDate[:4])
    end_month = int(endDate[5:7])
    end_day = int(endDate[8:])

    fridays_list=[]
    fridays_list_rates=[]


    for i in range(start_year,end_year+1):
        if i == end_year:
            last_month = end_month
        else:
            last_month = 12
        for j in range(start_month, last_month+1):
            if i == end_year and j == end_month:
                last_day = end_day
            elif j == 1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
                last_day = 31
            elif j == 4 or j==6 or j==9 or j==11:
                last_day = 30
            else:
                if start_year % 4 != 0:
                    last_day = 28
                else:
                    last_day = 29

            for k in range(start_day, last_day+1):
                date=datetime.datetime(i,j,k)

                if date.weekday()==4:
                    if j<10 and k<10:
                        fridays_list.append(str(i)+'-0'+str(j)+'-0'+str(k))
                    elif j<10 and k>=10:
                        fridays_list.append(str(i) + '-0' + str(j) + '-' + str(k))
                    elif j>=10 and k<10:
                        fridays_list.append(str(i) + '-' + str(j) + '-0' + str(k))
                    elif j>=10 and k>=10:
                        fridays_list.append(str(i) + '-' + str(j) + '-' + str(k))


    gcontext = ssl.SSLContext()
    url = urllib.request.urlopen(
        "https://api.exchangeratesapi.io/history?start_at=" + str(startDate) + "&end_at=" + str(endDate),
        context=gcontext)
    data = str(url.read())

    for l in range(len(fridays_list)):
        a = data.find(fridays_list[l])
        b = data.find('}', a)
        c = data.find(currency, a, b)
        d = data.find(',', c)
        e = data[c + 5:d]
        fridays_list_rates.append(e)
    fridays_list_rates=sorted(fridays_list_rates,key=float)

    f=data.find(fridays_list_rates[0])
    strongest_rate=data[f:f+len(fridays_list_rates[0])]
    g = data.find(fridays_list_rates[-1])
    weakest_rate=data[g:g+len(fridays_list_rates[-1])]
    h=data.rfind('-',0,f)
    strongest_date=data[h-7:h+3]
    i=data.rfind('-',0,g)
    weakest_date=data[i-7:i+3]
    print(currency+' was strongest on '+strongest_date+'. 1 Euro was equal to '+str(strongest_rate)+" "+currency)
    print(currency + ' was weakest on '+weakest_date+'. 1 Euro was equal to ' + str(weakest_rate)+" "+currency)

def findMissingDates(startDate,endDate):
    start_year = int(startDate[:4])
    start_month = int(startDate[5:7])
    start_day = int(startDate[8:])

    end_year = int(endDate[:4])
    end_month = int(endDate[5:7])
    end_day = int(endDate[8:])

    dates_list=[]
    missing_dates_list=[]


    for i in range(start_year, end_year + 1):
        if i == end_year:
            last_month = end_month
        else:
            last_month = 12
        for j in range(start_month, last_month + 1):
            if i == end_year and j == end_month:
                last_day = end_day
            elif j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
                last_day = 31
            elif j == 4 or j == 6 or j == 9 or j == 11:
                last_day = 30
            else:
                if start_year % 4 != 0:
                    last_day = 28
                else:
                    last_day = 29

            for k in range(start_day, last_day + 1):
                date = datetime.date(i, j, k)
                dates_list.append(str(date))

            start_day = 1
        start_month = 1

    gcontext = ssl.SSLContext()
    url = urllib.request.urlopen(
        "https://api.exchangeratesapi.io/history?start_at=" + str(startDate) + "&end_at=" + str(endDate),
        context=gcontext)
    data = str(url.read())

    print('The following dates were not present:')
    for i in range(len(dates_list)):
        a=data.find(dates_list[i])
        if a==-1:
            print(dates_list[i])


changeBase(100,"CAD",'USD','2010-10-25')

gcontext = ssl.SSLContext()
url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest", context=gcontext)
data=url.read()
data=str(data)
printAscending(data)

extremeFridays('2018-08-08', '2019-09-15', 'CAD')

findMissingDates('2018-08-08', '2019-09-15')