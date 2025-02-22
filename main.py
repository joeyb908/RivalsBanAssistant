import page_scraper
import hero_stats
from screenshot_reader import image_to_string

MIN_BANLIST_SIZE = 10

def check_profile(profile_name, ban_list):
    try:
        scraper = page_scraper.Scraper(profile_name)
        data = scraper.web_driver.data
        heroes = data[2:len(data) - 3]
        profile_hero_stats = hero_stats.HeroStats(heroes)
        profile_hero_stats.ban_calculator()
        for hero in profile_hero_stats.ban_heroes:
            add_to_master(ban_list, hero[0], hero[1], hero[2])
        scraper.web_driver.driver.close()
    except KeyError:
        print(f"Unable to check {profile_name}'s profile...")

def add_to_master(ban_list, hero_name, hero_winrate, hero_matches):
    if len(ban_list) < MIN_BANLIST_SIZE:
        ban_list.append([hero_name, hero_winrate, hero_matches])

    else:
        min_value = min(ban_list, key=lambda x: x[1])
        if hero_winrate > min_value[1]:
            min_index = ban_list.index(min_value)
            ban_list[min_index] = [hero_name, hero_winrate, hero_matches]

def check_profiles(list_of_profiles):
    for name in list_of_profiles:
        print(f"Checking {name}...")
        check_profile(name, master_ban_list)

    master_ban_list.sort(key=lambda x: x[2], reverse=True)

profile_names = image_to_string()
master_ban_list = []

check_profiles(profile_names)

if len(master_ban_list) == 0:
    print("No heroes with high enough winrate to consider banning")
else:
    print(f"Top {len(master_ban_list)} heroes to ban")
    for i in range(len(master_ban_list)):
          print(f"\t{master_ban_list[i][0]}: {round(master_ban_list[i][1])}% with {master_ban_list[i][2]} matches played")

