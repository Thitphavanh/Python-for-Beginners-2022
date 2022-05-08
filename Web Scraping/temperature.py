from urllib.request import urlopen
from bs4 import BeautifulSoup


def checktemp(ID):
    url = 'https://www.tmd.go.th/province.php?id=' + str(ID)

    webopen = urlopen(url)  # open website do not open chrome
    html_page = webopen.read()  # read information in website
    webopen.close()

    # use BeautifulSoup help for translate
    data = BeautifulSoup(html_page, 'html.parser')

    temp = data.find('td', {'class': 'strokeme'})
    title = data.find('span', {'class': 'title'})

    province = title.text.strip()
    temp = temp.text

    print(province, temp)


checktemp(22)
