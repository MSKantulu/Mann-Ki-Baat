!pip install bs4
!pip install requests

# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data
def getdata(url):
  r = requests.get(url)
  return r.text

htmldata = getdata("https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-79th-episode-of-mann-ki-baat/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
k=soup.find_all('div', attrs={'class':'news-bg'})
for data in k:
  for d1 in soup.find_all("p"):
    t=data.get_text()
print(t)

//All link in one go into file in drive

# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data
def getdata(url):
  r = requests.get(url)
  return r.text
m= ''
list1=['https://www.pmindia.gov.in/en/news_updates/english-rendering-of-mann-ki-baat-address-by-pm-on-all-india-radio/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-2nd-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/kn/news_updates/2017%e0%b2%b0-%e0%b2%8f%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%bf%e0%b2%b2%e0%b3%8d-30%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af/']
file1= open('myfile.txt','a')

for i in list1:
  htmldata = getdata(i)
  soup = BeautifulSoup(htmldata, 'html.parser')
  data = ''
  k=soup.find_all('div', attrs={'class':'news-bg'})
  for data in k:
    for d1 in soup.find_all("p"):
      t=data.get_text()
    file1.write(t)
file1.close()


 import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data
def getdata(url):
  r = requests.get(url)
  return r.text

list1=['https://www.pmindia.gov.in/en/news_updates/english-rendering-of-mann-ki-baat-address-by-pm-on-all-india-radio/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-2nd-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-3rd-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-48th-episode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-4th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-50th-episode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-mann-ki-baat-2-0programme-on-all-india-radio/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-10th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-11th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-12th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-13th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-14th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-15th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-16th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-17th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-18th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-19th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-20th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-21st-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-5th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-6th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-75thepisode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-76th-episode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-77th-episode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-78th-episode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-79th-episode-of-mann-ki-baat/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-7th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-8th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-9th-episode-of-mann-ki-baat-2-0/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-address-on-all-india-radio/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-address-on-all-india-radio-2/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-address-on-all-india-radio-3/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-address-on-all-india-radio-3/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-address-on-all-india-radio-4/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-at-all-india-radio/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-10/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-10/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-12/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-13/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-14/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-16/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-17/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-18/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-19/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-2/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-20/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-21/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-3/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-4/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-5/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-6/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-7/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-9/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-on-august-28-2016/',
       'https://www.pmindia.gov.in/en/news_updates/pms-mann-ki-baat-programme-on-all-india-radio-on-june-26-2016/',
       'https://www.pmindia.gov.in/en/news_updates/text-of-pms-mann-ki-baat-programme-on-all-india-radio-3/',
       'https://www.pmindia.gov.in/en/news_updates/text-of-prime-ministers-mann-ki-baat-on-all-india-radio-9/'
       ]
file1= open('Mann-En.txt','a')

for i in list1:
  htmldata = getdata(i)
  soup = BeautifulSoup(htmldata, 'html.parser')
  data = ''
  k=soup.find_all('div', attrs={'class':'news-bg'})
  for data in k:
    for d1 in soup.find_all("p"):
      t=data.get_text()
    file1.write(t)
file1.close()

list2= [Kannada
'https://www.pmindia.gov.in/kn/news_updates/2017%e0%b2%b0-%e0%b2%8f%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%bf%e0%b2%b2%e0%b3%8d-30%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d-2-%e0%b2%a8%e0%b3%87-%e0%b2%95%e0%b2%82%e0%b2%a4%e0%b2%bf%e0%b2%a8-%e0%b2%ad%e0%b2%be/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8-3/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-4/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%85%e0%b2%b5%e0%b2%b0-%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81-%e0%b2%95%e0%b2%a8%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d-2-0-%e0%b2%a8%e0%b3%87-%e0%b2%ae%e0%b3%8a%e0%b2%a6%e0%b2%b2-%e0%b2%95%e0%b2%82%e0%b2%a4/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-14-2/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-15/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf%e0%b2%af%e0%b2%b5%e0%b2%b0-%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81-12%e0%b2%a8%e0%b3%87-%e0%b2%b8%e0%b2%82/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d-2-0-13-%e0%b2%a8%e0%b3%87-%e0%b2%b8%e0%b2%82%e0%b2%9a%e0%b2%bf%e0%b2%95%e0%b3%86%e0%b2%af%e0%b2%b2/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-23/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-24/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-26/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6%e0%b2%bf%e0%b2%af%e0%b2%b5%e0%b2%b0/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6%e0%b2%bf%e0%b2%af%e0%b2%b5%e0%b2%b0-3/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-31/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-32/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-33/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-8/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-9/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-35/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-36/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-37/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-57/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-60/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-12/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81-8-%e0%b2%a8%e0%b3%87-%e0%b2%86%e0%b2%b5%e0%b3%83%e0%b2%a4%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-13/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d-%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b2%a6%e0%b2%be%e0%b2%b3%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81-%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/29-01-2017%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af-%e0%b2%ae%e0%b3%82%e0%b2%b2%e0%b2%95-%e0%b2%aa%e0%b3%8d%e0%b2%b0/',
'https://www.pmindia.gov.in/kn/news_updates/26-02-2017%e0%b2%b0-%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d-%e0%b2%ae%e0%b3%82%e0%b2%b2-%e0%b2%b9%e0%b2%bf%e0%b2%82%e0%b2%a6%e0%b2%bf/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-14/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%8a%e0%b2%b2%e0%b2%b5%e0%b2%bf%e0%b2%a8-%e0%b2%a6%e0%b3%87%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%b8%e0%b2%bf%e0%b2%97%e0%b2%b3%e0%b3%87-%e0%b2%a8%e0%b2%ae%e0%b2%b8/',
'https://www.pmindia.gov.in/kn/news_updates/28-01-2018%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%ae%e0%b2%be%e0%b2%a1%e0%b2%bf%e0%b2%a6%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/28-01-2018%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%ae%e0%b2%be%e0%b2%a1%e0%b2%bf%e0%b2%a6%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81-%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-3/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%a6%e0%b2%bf%e0%b2%a8%e0%b2%be%e0%b2%82%e0%b2%95-27-05-2018-%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8-%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-2/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%a6%e0%b2%bf%e0%b2%a8%e0%b2%be%e0%b2%82%e0%b2%95-26-08-2018%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-20/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-5/',
'https://www.pmindia.gov.in/kn/news_updates/28-%e0%b2%ae%e0%b3%87-2017%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%aa%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-22/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b2%a6-%e0%b2%ae%e0%b2%be%e0%b2%a4%e0%b3%81%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8-2/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-25-06-2017%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%aa%e0%b3%8d%e0%b2%b0/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-9/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6%e0%b3%8d%e0%b2%b0-%e0%b2%ae%e0%b3%8b%e0%b2%a6-2/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf%e0%b2%af%e0%b2%b5%e0%b2%b0%e0%b3%81-%e0%b2%a6%e0%b2%bf%e0%b2%a8%e0%b2%be%e0%b2%82%e0%b2%95/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf-%e0%b2%86%e0%b2%b2%e0%b3%8d-%e0%b2%87%e0%b2%82%e0%b2%a1%e0%b2%bf%e0%b2%af%e0%b2%be-%e0%b2%b0%e0%b3%87%e0%b2%a1%e0%b2%bf/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%aa%e0%b3%8d%e0%b2%b0%e0%b2%a7%e0%b2%be%e0%b2%a8%e0%b2%ae%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%bf-%e0%b2%b6%e0%b3%8d%e0%b2%b0%e0%b3%80-%e0%b2%a8%e0%b2%b0%e0%b3%87%e0%b2%82%e0%b2%a6-16/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%86%e0%b2%97%e0%b2%b8%e0%b3%8d%e0%b2%9f%e0%b3%8d-282016%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af%e0%b2%b2%e0%b3%8d/',
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%a8%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%8a%e0%b2%b2%e0%b2%b5%e0%b2%bf%e0%b2%a8-%e0%b2%a6%e0%b3%87%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%b8%e0%b2%bf%e0%b2%97%e0%b2%b3%e0%b3%86-%e0%b2%a8%e0%b2%bf/',
'https://www.pmindia.gov.in/kn/news_updates/26-03-2017%e0%b2%b0%e0%b2%82%e0%b2%a6%e0%b3%81-%e0%b2%86%e0%b2%95%e0%b2%be%e0%b2%b6%e0%b2%b5%e0%b2%be%e0%b2%a3%e0%b2%bf%e0%b2%af-%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac/'
'https://www.pmindia.gov.in/kn/news_updates/%e0%b2%ae%e0%b2%a8%e0%b3%8d-%e0%b2%95%e0%b2%bf-%e0%b2%ac%e0%b2%be%e0%b2%a4%e0%b3%8d/]
