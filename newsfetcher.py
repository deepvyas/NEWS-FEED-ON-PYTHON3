# CREATED BY 

# 			PHANTM-V 		ON 29/08/2015

# FOR LEARNING PURPOSES AND PERSONAL USE
# USERS ARE ALLOWED TO DOWNLOAD MODIFY AND SHARE.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url = "http://www.timesofindia.indiatimes.com"
response =urlopen(url)
html = response.read()
pattern = re.compile('new_tops#[0-9]{1,}')
soup = BeautifulSoup(html,"html.parser")
data = soup.findAll('a',{"pg":pattern})
for a in data:
	print (a.text)
	print("===============================================================")
print("============================================================================================")
print('')
print("=============================================================================================")
pattern2 = re.compile('new_latest#[0-9]{1,2}')
data2 = soup.findAll('a',{"pg":pattern2})
for a in data2:
	print(a.text)
	print("===============================================================")
pattern_world = re.compile('World#[0-9]{1,2}')
data3= soup.findAll('a',{"pg":pattern_world})
for a in data3:
	print(a.text)
	print("===============================================================")
pattern_science = re.compile('Science#[0-9]{1,2}')
data4= soup.findAll('a',{"pg":pattern_science})
for a in data4:
	print(a.text)
	print("===============================================================")
pattern_education = re.compile('Education#[0-9]{1,2}')
data5= soup.findAll('a',{"pg":pattern_education})
for a in data5:
	print(a.text)
	print("===============================================================")
