import numpy as np
import pandas as pd
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path =r"C:\Users\91885\Desktop\sahil solution\chromedriver.exe") # link to your chromedriver
driver.maximize_window()

driver.get('https://clutch.co/uk/app-developers/london')
time.sleep(1)
arr = driver.find_elements_by_xpath("//ul[@class='directory-list']/li")
number_of_company = len(arr)

data = []
for i in range(number_of_company-1):
    company_data = {}
    company_url = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[2]/ul/li/a")
    company_url = company_url.get_attribute("href")
    company_data["company_url"] =company_url 
    ele = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]")
    company_name = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div/div/h3").text
    company_rating = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div//span").text
    company_reviews = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div/div/div/a[2]").text
    minimum_project_size = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div[2]//div[@data-content='<i>Min. project size</i>']").text
    average_hourly_rates = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div[2]/div/div[2]//div[@data-content='<i>Avg. hourly rate</i>']").text
    employees =driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div[2]/div/div[2]//div[@data-content='<i>Employees</i>']").text
    location = driver.find_element_by_xpath(f"//ul[@class='directory-list']/li[@data-position={i+1}]/div/div[1]/div[2]/div/div[2]//div[@data-content='<i>Location</i>']").text
    company_data["company_name"] = company_name
    company_data['minimum_project_size'] = minimum_project_size
    company_data["average_hourly_rates"] = average_hourly_rates
    company_data["employees"] = employees
    company_data["location"] = location
    company_data["rating"] = company_rating
    company_data["reviews"] = company_reviews
    data.append(company_data)
    
    
fieldnames = ["company_url","company_name","minimum_project_size","average_hourly_rates","employees","location","rating","reviews"]
with open('company_data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
                                 
                                 
