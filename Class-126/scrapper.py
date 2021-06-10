from selenium import webdriver
from bs4 import BeautifulSoup

import time
import csv

startUrl = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\Subramaniam\Dropbox\My PC (LAPTOP-499770CL)\Downloads\chromedriver_win32")
browser.get(startUrl)

time.sleep(10)

def Scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            li_tag = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tag):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0]
                else:
                    try:
                       temp_list.append(li_tag.contents[0])
                    except:
                       temp_list.append("")
        planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv","w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planet_data) 
                
Scrape()
