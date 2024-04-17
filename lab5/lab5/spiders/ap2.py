import scrapy

from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from lab5.items import Item
class Ap2Spider(scrapy.Spider):
    name = "ap2"
    allowed_domains = ["robota.ua"]
    start_urls = ["https://robota.ua"]
    start_urls1 = ["https://robota.ua/auth/login"]

    def start_requests(self):
        for url in self.start_urls1:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     "alliance-recommended-vacancy-list")
                ),
                execute=self.login
            )

    def login(self, driver, wait):
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@type="email"]')))
        email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
        email_input.send_keys("mamamamo494@gmail.com")
        username_password = driver.find_element(By.XPATH, '//input[@type="password"]')
        username_password.send_keys("password")
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@class="santa-no-underline ng-star-inserted"]')))
        recommendation_button = driver.find_element(By.XPATH, '//a[@class="santa-no-underline ng-star-inserted"]')
        recommendation_button.click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@type="text"]')))
        input1 = driver.find_element(By.XPATH, '//input[@type="text"]')
        input1.send_keys("Hr")
        button = driver.find_element(By.XPATH, '//santa-button[@class="santa-ml-20"]')
        button.click()

    def parse(self, response):
        for item in response.css("alliance-recommended-vacancy-list.ng-star-inserted a"):
            name = item.css('::text').get().strip()
            url = item.css('img::attr(src)').get()

            yield Item(
                name=name,
                url=url,
                image_urls=[url],
            )

        pass
