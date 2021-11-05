from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER = "D:\Python\chromedriver_win32\chromedriver.exe"


class ZillowScraper:
    def __init__(self, url):
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.driver.get(url)
        self.response = ""
        self.scroll_page()
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def scroll_page(self):
        for i in range(20):
            container = self.driver.find_element_by_xpath('//*[@id="search-page-list-container"]')
            self.driver.execute_script(f"arguments[0].scrollTop = 500*{i}", container)
            sleep(1)
        self.response = self.driver.page_source

    def next_page(self, page_number):
        try:
            # self.driver.find_element_by_xpath('//*[@id="grid-search-results"]/div[2]/nav/ul/li[7]/a').click()
            # self.driver.find_element_by_css_selector('a.cyhUbV').click()
            # self.driver.find_element_by_link_text(f'{page_number}')
            lis = self.driver.find_elements_by_css_selector("li.eGOQHk")
            lis[1].click()
        except NoSuchElementException:
            print("no more pages")
            pass
        # self.driver.find_element_by_xpath('//*[@id="grid-search-results"]/div[2]/nav/ul/li[6]/span')

    def get_number_of_pages(self):
        total_pages = int(self.soup.find('span', 'Text-c11n-8-37-0__aiai24-0').get_text().split()[-1])
        return total_pages

    def get_all_the_pages(self):
        self.beautisoup()
        for i in range(2, self.get_number_of_pages() + 1):
            self.next_page(i)
            self.scroll_page()
            self.beautisoup()

    def beautisoup(self):
        self.soup = BeautifulSoup(self.response, 'html.parser')

        banners = self.soup.find_all("div", "list-card-info")

        for banner in banners:
            link = banner.contents[0].get('href')
            address = banner.contents[0].get_text()
            price = banner.contents[2].contents[0].get_text()
            driver = webdriver.Chrome(CHROME_DRIVER)
            driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc4o27k6taW1G66MYXStTBqjI9L8TlOt7axrb0zX741i8KkQQ'
                       '/viewform?usp=sf_link')
            inputs = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            inputs.click()
            sleep(1)
            inputs.send_keys(address)

            inputs1 = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            inputs1.send_keys(price)

            inputs2 = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            inputs2.send_keys(link)
            sleep(1)
            driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
            sleep(1)
            driver.quit()
