from web_driver import RivalsAPIReader


class Scraper:
    def __init__(self, profile):
        self.web_driver = RivalsAPIReader(profile)
