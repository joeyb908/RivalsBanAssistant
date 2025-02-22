import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class RivalsAPIReader:
    def __init__(self, profile):
        self.driver = webdriver.Chrome()
        self.driver.get(f"https://api.tracker.gg/api/v2/marvel-rivals/standard/profile/ign/{profile}/segments/career?mode=competitive&season=2")
        self.json_data = json.loads(self.driver.find_element(By.TAG_NAME, "body").text)
        # with open("./json/page_data.json") as json_file:
        #     self.json_data = json.load(json_file)
        self.data = self.json_data["data"]
