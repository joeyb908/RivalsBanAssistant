from web_driver import WebDriver
from json import loads
from selenium.webdriver.common.by import By

class PageScraper:
    def __init__(self):
        self.web_driver = WebDriver()

    def scrape_page(self, profile):
        self.web_driver.driver.get(
            f"https://api.tracker.gg/api/v2/marvel-rivals/standard/profile/ign/{profile}/segments/career?mode=competitive&season=2")
        json_data = loads(self.web_driver.driver.find_element(By.TAG_NAME, "body").text)
        data = json_data["data"]
        heroes = data[2:len(data) - 3]
        return heroes