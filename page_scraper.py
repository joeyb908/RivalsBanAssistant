from web_driver import TrackerAPIReader


class TrackerPageScraper:
    def __init__(self, profile):
        self.web_driver = TrackerAPIReader(profile)
