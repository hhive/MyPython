import requests
from bs4 import BeautifulSoup
import pymysql
import time


def get_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    return soup


def get_links(link_url):
    soup = get_page(link_url)
    links_div = soup.find_all('div', class_="pic-panel")
    print(links_div[1].a.get('href'))
    links = [div.a.get('href') for div in links_div]
    print(links)
    return links


def get_house_info(house_url):
    soup = get_page(house_url)
    # house_info = soup.find_all('p', class_ = 'lf')
    house_info = soup.find_all('p')
    price = soup.find('span', class_='total').text
    unit = soup.find('span', class_='unit').text.strip()
    area = house_info[0].text[3:]
    layout = house_info[1].text[5:]
    floor = house_info[2].text[3:]
    direction = house_info[3].text[5:]
    subway = house_info[4].text[3:]
    community = house_info[5].text[3:].replace('\n', '').replace(' ', '')
    location = house_info[6].text[3:]
    create_time = house_info[7].text[3:]
    agent = soup.find('a', class_='name LOGCLICK')
    if agent:
        agent_name = agent.text
        agent_id = agent.get('data-el')
    else:
        agent_name = "暂无"
        agent_id = "暂无"
    # evaluate = soup.find('div', class_ = 'evaluate')
    # score, number = evaluate.find('span',class_ = 'rate').text.split('/')
    # time = evaluate.find('span',class_ = 'time').text[5:-1]
    info = {
        '价格': price,
        '单位': unit,
        '面积': area,
        '户型': layout,
        '楼层': floor,
        '朝向': direction,
        '发布时间': create_time,
        '地铁': subway,
        '小区': community,
        '位置': location,
        '经纪人名字': agent_name,
        '经纪人id': agent_id,
    }
    return info


DATABASE = {
    'host':'127.0.0.1',
    'database':'LianJia',
    'user':'root',
    'password':'8888'
}


def get_db(setting):
    return pymysql.connect(**setting)


def insert(db, house):
    values = "'{}',"*10+"'{}'"
    sql_values = values.format(house['价格'], house['单位'], house['面积'], house['户型'],
                               house['楼层'], house['朝向'], house['地铁'], house['小区'],
                               house['位置'], house['经纪人名字'], house['经纪人id'])
    sql = """
        insert into `house`(`price`, `unit`, `area`, `layout`, `floor`, `direction`, `subway`,
                              `community`, `location`, `agent_name`, `agent_id`)
                              values ({})
    """.format(sql_values)
    print(sql)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


db = get_db(DATABASE)
links = get_links('https://bj.lianjia.com/zufang/')
for link in links:
    time.sleep(2)
    house = get_house_info(link)
    insert(db, house)


# use LianJia;
# # create table house(
# # id int not null auto_increment,
# # price varchar(255),
# # unit varchar(255),
# # area varchar(255),
# # layout varchar(255),
# # floor varchar(255),
# # direction varchar(255),
# # subway varchar(255),
# # community varchar(255),
# # location varchar(255),
# # agent_name varchar(255),
# # agent_id varchar(255),
# # primary key (id))engine=InnoDB default char set=utf8
