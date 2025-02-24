import page_scraper
import hero_stats
import threading
from prettytable import PrettyTable
from mapped_names import hero_name_map
from screenshot_reader import image_to_string

MIN_BANLIST_SIZE = 10

class BanAssistant:
    def __init__(self):
        self.master_ban_list = []
        self.profile_names = image_to_string()
        self.table = PrettyTable()
        self.table.field_names = ["Hero", "Winrate", "Games Played", "Player"]

    def check_profile(self, profile_name):
        scraper = page_scraper.PageScraper()  # Use a local variable instead of self.scraper

        try:
            heroes = scraper.scrape_page(profile_name)
        except KeyError:
            print(f"Unable to check {profile_name}'s profile...")
        else:
            profile_hero_stats = hero_stats.HeroStats(heroes)
            profile_hero_stats.ban_calculator()
            for hero in profile_hero_stats.ban_heroes:
                hero_name = hero[0]
                hero_winrate = hero[1]
                hero_matches = hero[2]
                self.add_to_master(hero_name, hero_winrate, hero_matches, profile_name)
        finally:
            scraper.web_driver.driver.close()  # Close the local driver instance

    def check_profiles(self):
        # Create dict of size n-profiles_to_check to run concurrently
        a = {k: threading.Thread(target=self.check_profile, args=(name,)) for k, name in
             enumerate(self.profile_names)}

        for thread in a.values():
            thread.start()

        for thread in a.values():
            thread.join()

        self.master_ban_list.sort(key=lambda x: x[2], reverse=True)

    def add_to_master(self, hero_name, hero_winrate, hero_matches, profile_name):
        if len(self.master_ban_list) < MIN_BANLIST_SIZE:
            self.master_ban_list.append([hero_name, hero_winrate, hero_matches, profile_name])

        else:
            min_value = min(self.master_ban_list, key=lambda x: x[1])
            if hero_winrate > min_value[1]:
                min_index = self.master_ban_list.index(min_value)
                self.master_ban_list[min_index] = [hero_name, hero_winrate, hero_matches, profile_name]

    def bans(self):
        if len(self.master_ban_list) == 0:
            print("No heroes with high enough winrate to consider banning")
        else:
            # Convert names in ban_list to mapped names
            self.master_ban_list = [[hero_name_map.get(hero, hero)] + rest for hero, *rest in self.master_ban_list]

            print(f"Top {len(self.master_ban_list)} heroes to ban:")
            for i in range(len(self.master_ban_list)):
                hero = self.master_ban_list[i][0]
                winrate = f"{round(self.master_ban_list[i][1])}%"
                games_played = self.master_ban_list[i][2]
                player = self.master_ban_list[i][3]
                self.table.add_row([hero, winrate, games_played, player])
            print(self.table)

    def run(self):
        self.profile_names = image_to_string()
        self.check_profiles()
        self.bans()