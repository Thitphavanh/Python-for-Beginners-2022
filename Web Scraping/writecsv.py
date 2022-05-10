import csv
from datetime import datetime


def writeToCsv(data):
	date = datetime.now().strftime('%Y-%m-%d')
	with open('data-temperature-{}.csv'.format(date), 'a', newline='', encoding='utf-8') as file:
		fileWriter = csv.writer(file)
		fileWriter.writerow(data)


writeToCsv(['มุกดาหาร', 25.5])
