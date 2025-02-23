from web_driver import TrackerAPILoader


class TrackerPageScraper:
    def __init__(self, profile):
        self.web_driver = TrackerAPILoader(profile)
