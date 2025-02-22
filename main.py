import page_scraper
import hero_stats

def check_profile(profile_name, ban_list):
    try:
        scraper = page_scraper.Scraper(profile_name)
        data = scraper.web_driver.data
        heroes = data[2:len(data) - 3]
        profile_hero_stats = hero_stats.HeroStats(heroes)
        profile_hero_stats.ban_calculator()
        for hero in profile_hero_stats.ban_heroes:
            add_to_master(ban_list, hero[0], hero[1])
        scraper.web_driver.driver.close()
    except KeyError:
        print(f"{profile_name} has a private profile")

def add_to_master(ban_list, hero_name, hero_winrate):
    if len(ban_list) < 3:
        ban_list.append([hero_name, hero_winrate])

    else:
        min_value = min(ban_list, key=lambda x: x[1])
        if hero_winrate > min_value[1]:
            min_index = ban_list.index(min_value)
            ban_list[min_index] = [hero_name, hero_winrate]

def check_profiles(profile_names):
    for name in profile_names:
        check_profile(name, master_ban_list)

    master_ban_list.sort(key=lambda x: x[1], reverse=True)

profile_names = input("Enter profile names separated by comma:\n")
profile_names = profile_names.split(',')
master_ban_list = []

check_profiles(profile_names)

# for name in profile_names:
#     check_profile(name, master_ban_list)
#
# master_ban_list.sort(key=lambda x: x[1], reverse=True)

if len(master_ban_list) == 0:
    print("No heroes with high enough winrate to consider banning")
else:
    print(f"Top {len(master_ban_list)} heroes to ban")
    for i in range(len(master_ban_list)):
          print(f"\t{round(master_ban_list[i][1])}%: {master_ban_list[i][0]}")

