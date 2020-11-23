import requests
from bs4 import BeautifulSoup
import csv

URL = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id={};trophy=117;type=season"

#list of all the years IPL played till date.

years = ["2007%2F08","2009","2009%2F10","2011","2012",'2013',"2014","2015","2016","2017","2018","2019","2020%2F21"]


'''
The below block of code will loop through all the years
Writes a csv file named "ipl_new.csv"
'''
for year in years:
    print("*****updating csv file for the year:{}*****".format(year))
    url = URL.format(year)
    page = requests.get(url)
    bs = BeautifulSoup(page.content, 'lxml')
    
    with open("ipl_new.csv",'a', newline='') as f:
        csv_writer = csv.writer(f)
        for tr in bs.find_all("tr"):
            data = []
            for th in tr.find_all("th"):
                data.append(th.text)
            for td in tr.find_all("td"):
                if td.a:
                    data.append(td.a.text.strip())
                else:
                    data.append(td.text.strip())
            if data:
                csv_writer.writerow(data)