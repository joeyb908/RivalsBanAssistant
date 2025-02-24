import page_scraper
import hero_stats

MIN_BANLIST_SIZE = 10

class BanAssistant:
    def __init__(self):
        self.scraper = None
        self.master_ban_list = []


    def check_profile(self, profile_name):
        self.scraper = page_scraper.PageScraper()

        try:
            heroes = self.scraper.scrape_page(profile_name)

        except KeyError:
            print(f"Unable to check {profile_name}'s profile...")

        else:
            profile_hero_stats = hero_stats.HeroStats(heroes)
            profile_hero_stats.ban_calculator()
            for hero in profile_hero_stats.ban_heroes:
                self.add_to_master(self, hero[0], hero[1], hero[2], profile_name)

        finally:
            self.scraper.web_driver.driver.close()

    def add_to_master(self, hero_name, hero_winrate, hero_matches, profile_name):
        if len(self.master_ban_list) < MIN_BANLIST_SIZE:
            self.master_ban_list.append([hero_name, hero_winrate, hero_matches, profile_name])

        else:
            min_value = min(self.master_ban_list, key=lambda x: x[1])
            if hero_winrate > min_value[1]:
                min_index = self.master_ban_list.index(min_value)
                self.master_ban_list[min_index] = [hero_name, hero_winrate, hero_matches, profile_name]