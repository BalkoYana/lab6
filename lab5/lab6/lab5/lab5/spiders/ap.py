import scrapy
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
class ApSpider(scrapy.Spider):
    name = "ap"
    allowed_domains = ["apteka-ds.com.ua"]
    start_urls = ["https://apteka-ds.com.ua"]
    start_urls1 = ["https://robota.ua/auth/login"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     "li button")
                ),
                execute=self.login
            )

    def login(self, driver, wait):
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//li[class="header-cabinet_item-block"]')))
        input = driver.find_element(By.XPATH, '//li[@class="header-cabinet_item-block"]')
        username_input = driver.find_element(By.XPATH, '//div[class="auth-main-block"]')

        username_input.send_keys("UzhnuTest")
        username_password = driver.find_element(By.XPATH, '//input[@name="password"]')
        username_password.send_keys("UzhnuTestPassword")
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Не зараз')]")))
        later_button = driver.find_element(By.XPATH, "//button[contains(text(),'Не зараз')]")
        later_button.click()
    def parse(self, response):
        pass
