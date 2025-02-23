from json import loads
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

class TrackerAPIReader:
    def __init__(self, profile):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.options)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
        )
        self.driver.get(f"https://api.tracker.gg/api/v2/marvel-rivals/standard/profile/ign/{profile}/segments/career?mode=competitive&season=2")
        self.json_data = loads(self.driver.find_element(By.TAG_NAME, "body").text)
        self.data = self.json_data["data"]
