MIN_WINRATE = 40
MIN_MATCHES = 10

class HeroStats:
    def __init__(self, heroes):
        self.heroes = heroes
        self.top_heroes = []
        self.ban_heroes = []

    def find_hero_winrate(self, index):
        hero_matches = float(self.heroes[index]["stats"]["matchesPlayed"]["value"])
        hero_name = self.heroes[index]["metadata"]["name"]
        hero_winrate = float(self.heroes[index]["stats"]["matchesWinPct"]["value"])

        if hero_matches < MIN_MATCHES:
            return [hero_name, 1, 1]

        return [hero_name, hero_winrate, hero_matches]

    def add_hero(self, index):
        [hero_name, hero_winrate, hero_matches] = self.find_hero_winrate(index)
        if len(self.top_heroes) < 3:
            self.top_heroes.append([hero_name, hero_winrate, hero_matches])
        else:
            min_value = min(self.top_heroes, key=lambda x: x[1])
            if hero_winrate > min_value[1]:
                min_index = self.top_heroes.index(min_value)
                self.top_heroes[min_index] = [hero_name, hero_winrate, hero_matches]

    def ban_calculator(self):
        for i in range(len(self.heroes)):
            self.add_hero(i)

        for hero, winrate, matches in self.top_heroes:
            if winrate > MIN_WINRATE:
                self.ban_heroes.append([hero, winrate, matches])