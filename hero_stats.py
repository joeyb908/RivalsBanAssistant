
class HeroStats:
    def __init__(self, heroes):
        self.heroes = heroes
        self.top_three_heroes = []
        self.ban_heroes = []

    def find_hero_winrate(self, index):
        hero_matches = float(self.heroes[index]["stats"]["matchesPlayed"]["value"])
        hero_name = self.heroes[index]["metadata"]["name"]
        hero_winrate = float(self.heroes[index]["stats"]["matchesWinPct"]["value"])

        if hero_matches < 10:
            return [hero_name, 1]

        return [hero_name, hero_winrate, hero_matches]

    def add_hero(self, index):
        [hero_name, hero_winrate, hero_matches] = self.find_hero_winrate(index)
        if len(self.top_three_heroes) < 3:
            self.top_three_heroes.append(self.find_hero_winrate(index))

        else:
            min_value = min(self.top_three_heroes, key=lambda x: x[1])
            if hero_winrate > min_value[1]:
                min_index = self.top_three_heroes.index(min_value)
                self.top_three_heroes[min_index] = [hero_name, hero_winrate, hero_matches]

    def ban_calculator(self):
        for i in range(len(self.heroes)):
            self.add_hero(i)

        for hero, winrate, matches in self.top_three_heroes:
            if winrate > 59.9:
                self.ban_heroes.append([hero, winrate, matches])

    def clear(self):
        self.heroes = []
        self.top_three_heroes = []
        self.ban_heroes = []