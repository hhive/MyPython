import requests
from bs4 import BeautifulSoup


# 获取url下的内容，返回soup对象
def get_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    return soup

def get_links(link_url):
    soup = get_page(link_url)
    links_div = soup.find_all('div', class_="pic-panel")
    links = [div.a.get('herf') for div in links_div]
    return links


# 获取列表也下的所有租房页面的链接，返回连接列表
url = 'https://bj.lianjia.com/zufang/'
get_links(url)
house_url = ''
soup = get_page(house_url)

# house_info = soup.find_all('p', class_ = 'lf')
house_info = soup.find_all('p')
price = soup.find('span', class_ = 'total').text
unit = soup.find('span', class_ = 'unit').text.strip()
area = house_info[0].text[3:]
layout = house_info[1].text[5:]
floor = house_info[2].text[3:]
direction = house_info[3].text[5:]


