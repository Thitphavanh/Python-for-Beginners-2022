from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime



def writeToCsv(data):
	date = datetime.now().strftime('%Y-%m-%d')
	with open('data-temperature-{}.csv'.format(date), 'a', newline='', encoding='utf-8') as file:
		fileWriter = csv.writer(file)
		fileWriter.writerow(data)


alldata = {}


def checktemp(ID):
	url = 'https://www.tmd.go.th/province.php?id=' + str(ID)

	webopen = urlopen(url)  # open website do not open chrome
	html_page = webopen.read()  # read information in website
	webopen.close()

	# use BeautifulSoup help for translate
	data = BeautifulSoup(html_page, 'html.parser')

	try:
		temp = data.find('td', {'class': 'strokeme'})
		title = data.find('span', {'class': 'title'})

		province = title.text.strip()
		temp = temp.text
		# print(province, temp)
		alldata[province] = temp
	except:
		pass


for i in range(1, 101):
	checktemp(i)

# print(alldata['มุกดาหาร'])

for k,v in alldata.items():
	data = [k,v]
	writeToCsv(data)

print('saved')
