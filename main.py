import page_scraper
import hero_stats
from screenshot_reader import image_to_string
import threading
import time
from prettytable import PrettyTable
from mapped_names import hero_name_map

MIN_BANLIST_SIZE = 10
table = PrettyTable()
table.field_names = ["Hero", "Winrate", "Games Played", "Player"]

# Record the start time
start = time.time()

# def check_profile(profile_name, ban_list):
#     scraper = page_scraper.PageScraper()
#
#     try:
#         heroes = scraper.scrape_page(profile_name)
#
#     except KeyError:
#         print(f"Unable to check {profile_name}'s profile...")
#
#     else:
#         profile_hero_stats = hero_stats.HeroStats(heroes)
#         profile_hero_stats.ban_calculator()
#         for hero in profile_hero_stats.ban_heroes:
#             add_to_master(ban_list, hero[0], hero[1], hero[2], profile_name)
#
#     finally:
#         scraper.web_driver.driver.close()

# def add_to_master(ban_list, hero_name, hero_winrate, hero_matches, profile_name):
#     if len(ban_list) < MIN_BANLIST_SIZE:
#         ban_list.append([hero_name, hero_winrate, hero_matches, profile_name])
#
#     else:
#         min_value = min(ban_list, key=lambda x: x[1])
#         if hero_winrate > min_value[1]:
#             min_index = ban_list.index(min_value)
#             ban_list[min_index] = [hero_name, hero_winrate, hero_matches, profile_name]

def check_profiles(list_of_profiles):
    a = {k: threading.Thread(target=check_profile, args=(name, master_ban_list)) for k, name in
         enumerate(list_of_profiles)}

    # Start all threads
    for thread in a.values():
        thread.start()

    for thread in a.values():
        thread.join()

    master_ban_list.sort(key=lambda x: x[2], reverse=True)

def ban_output(ban_list):
    if len(ban_list) == 0:
        print("No heroes with high enough winrate to consider banning")
    else:
        # Convert names in ban_list to mapped names
        ban_list = [[hero_name_map.get(hero, hero)] + rest for hero, *rest in ban_list]

        print(f"Top {len(ban_list)} heroes to ban:")
        for i in range(len(ban_list)):
            hero = ban_list[i][0]
            winrate = f"{round(ban_list[i][1])}%"
            games_played = ban_list[i][2]
            player = ban_list[i][3]
            table.add_row([hero, winrate, games_played, player])
        print(table)

profile_names = image_to_string()
check_profiles(profile_names)
ban_output(master_ban_list)

end = time.time()

print(f"\nTotal time: {round(end - start, 2)} seconds")