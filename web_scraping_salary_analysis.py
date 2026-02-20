
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")
table = soup.find("table")

languages = []
avg_salaries = []

for row in table.find_all("tr"):
    cols = row.find_all("td")
    language = cols[1].getText()
    avg_salary = cols[3].getText()
    print(f"{language} ---> {avg_salary}")
    languages.append(language)
    avg_salaries.append(avg_salary)


df = pd.DataFrame({"Language" :languages , "Avg_salary" : avg_salaries})
df = df.drop(df.index[0])

df.to_csv("popular_languages.csv")
print("DataFrame Saved to popular_languages.csv")
