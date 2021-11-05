from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
from time import sleep

page_para = ""
# for i in range(0, 3):
#


# url = f"https://www.zillow.com/grand-rapids-mi/rentals/1-_beds/{page_para}/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Grand%20Rapids%2C%20MI%22%2C%22mapBounds%22%3A%7B%22west%22%3A-85.86246881640625%2C%22east%22%3A-85.43949518359375%2C%22south%22%3A42.80779084510801%2C%22north%22%3A43.07319827467048%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A11671%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/39.0.2171.95 Safari/537.36'}
# response = requests.get("https://www.zillow.com/homes/Grand-Rapids,-MI_rb/", headers=headers)

CHROME_DRIVER = "D:\Python\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER)


def get_pages(page_number):
    page_para = str(page_number) + '_p/'
    if page_number == 0:
        page_para = ""

    driver.get(
        f"https://www.zillow.com/grand-rapids-mi/rentals/1-_beds/{page_para}?searchQueryState=%7B%22usersSearchTerm%22%3A"
        "%22Grand%20Rapids%2C%20MI%22%2C%22mapBounds%22%3A%7B%22west%22%3A-85.86246881640625%2C%22east%22%3A-85"
        ".43949518359375%2C%22south%22%3A42.86720464961727%2C%22north%22%3A43.013983013023534%7D%2C"
        "%22regionSelection%22%3A%5B%7B%22regionId%22%3A11671%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22"
        "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B"
        "%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22"
        "%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22"
        "%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22"
        "%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A"
        "%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C"
        "%22mapZoom%22%3A11%7D")
    sleep(5)

    for i in range(20):
        container = driver.find_element_by_xpath('//*[@id="search-page-list-container"]')
        driver.execute_script(f"arguments[0].scrollTop = 500*{i}", container)
        sleep(1)
    response = driver.page_source
    driver.find_element_by_xpath('//*[@id="grid-search-results"]/div[2]/nav/ul/li[6]/span')
    return response

def get_number_of_pages(response):
    total_pages = int(soup.find('span', 'Text-c11n-8-37-0__aiai24-0').get_text().split()[-1])
    return total_pages

def beautisoup(response):
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.prettify())
    banners = soup.find_all("div", "list-card-info")
    for banner in banners:
        link = banner.contents[0].get('href')
        address = banner.contents[0].get_text()
        price = banner.contents[2].contents[0].get_text()

        print(link)
        print(address)
        print(price)
    print(len(banners))

#     '//*[@id="grid-search-results"]/div[2]/nav/ul/li[6]/span'
# for
# beautisoup(get_pages(0))

# for child in banners[0].contents[2].descendants:
#     print(child)

# prices = [item.find('div', 'list-card-price') for item in soup.find_all("div", "list-card-info")]
# print(prices)
# ul = soup.find('ul', 'photo-cards')
# list_of_lis = ul.find_all('li')
# for item in list_of_lis:
#    print(item.contents)
