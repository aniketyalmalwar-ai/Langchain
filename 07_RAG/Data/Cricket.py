
"""
Cricket Management System
Description: A simple Python program to manage cricket players,
teams, match statistics, and performance analysis.
"""

# ==========================================
# 1. PLAYER CLASS
# ==========================================

class Player:

    def __init__(self, name, age, role, country):
        self.name = name
        self.age = age
        self.role = role
        self.country = country

    def display_details(self):
        print(f"Player Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")
        print(f"Country: {self.country}")


# ==========================================
# 2. BATSMAN CLASS
# ==========================================

class Batsman(Player):

    def __init__(self, name, age, country, runs, matches):
        super().__init__(name, age, "Batsman", country)
        self.runs = runs
        self.matches = matches

    def average(self):
        if self.matches == 0:
            return 0
        return round(self.runs / self.matches, 2)

    def display_statistics(self):
        self.display_details()
        print(f"Total Runs: {self.runs}")
        print(f"Matches: {self.matches}")
        print(f"Average: {self.average()}")


# ==========================================
# 3. BOWLER CLASS
# ==========================================

class Bowler(Player):

    def __init__(self, name, age, country, wickets, matches):
        super().__init__(name, age, "Bowler", country)
        self.wickets = wickets
        self.matches = matches

    def wickets_per_match(self):
        if self.matches == 0:
            return 0
        return round(self.wickets / self.matches, 2)

    def display_statistics(self):
        self.display_details()
        print(f"Total Wickets: {self.wickets}")
        print(f"Matches: {self.matches}")
        print(f"Wickets Per Match: {self.wickets_per_match()}")


# ==========================================
# 4. TEAM CLASS
# ==========================================

class Team:

    def __init__(self, team_name, country):
        self.team_name = team_name
        self.country = country
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_team(self):
        print(f"\nTeam: {self.team_name}")
        print(f"Country: {self.country}")

        for player in self.players:
            print(f"- {player.name} ({player.role})")

    def total_players(self):
        return len(self.players)


# ==========================================
# 5. MATCH STATISTICS
# ==========================================

class Match:

    def __init__(self, team1, team2, venue, overs):
        self.team1 = team1
        self.team2 = team2
        self.venue = venue
        self.overs = overs

    def display_match_details(self):
        print("\nMatch Details")
        print(f"{self.team1} vs {self.team2}")
        print(f"Venue: {self.venue}")
        print(f"Overs: {self.overs}")


# ==========================================
# 6. CRICKET DATA
# ==========================================

players_data = [
    {
        "name": "Virat Kohli",
        "country": "India",
        "role": "Batsman",
        "runs": 14000,
        "matches": 295
    },
    {
        "name": "Rohit Sharma",
        "country": "India",
        "role": "Batsman",
        "runs": 11000,
        "matches": 265
    },
    {
        "name": "Jasprit Bumrah",
        "country": "India",
        "role": "Bowler",
        "wickets": 150,
        "matches": 100
    },
    {
        "name": "Steve Smith",
        "country": "Australia",
        "role": "Batsman",
        "runs": 10000,
        "matches": 200
    }
]


# ==========================================
# 7. PLAYER PERFORMANCE ANALYSIS
# ==========================================

def calculate_batting_average(runs, matches):
    if matches <= 0:
        return 0

    average = runs / matches
    return round(average, 2)


def calculate_bowling_average(wickets, matches):
    if matches <= 0:
        return 0

    average = wickets / matches
    return round(average, 2)


def find_top_scorer(players):
    batsmen = [
        player for player in players
        if player["role"] == "Batsman"
    ]

    if not batsmen:
        return None

    return max(batsmen, key=lambda player: player["runs"])


def display_all_players(players):
    for player in players:
        print("\n--------------------")
        print(f"Name: {player['name']}")
        print(f"Country: {player['country']}")
        print(f"Role: {player['role']}")

        if player["role"] == "Batsman":
            print(f"Runs: {player['runs']}")
            print(
                f"Average: {calculate_batting_average(player['runs'], player['matches'])}"
            )

        elif player["role"] == "Bowler":
            print(f"Wickets: {player['wickets']}")
            print(
                f"Wickets Per Match: {calculate_bowling_average(player['wickets'], player['matches'])}"
            )


# ==========================================
# 8. MAIN PROGRAM
# ==========================================

def main():

    print("CRICKET MANAGEMENT SYSTEM")

    display_all_players(players_data)

    top_scorer = find_top_scorer(players_data)

    if top_scorer:
        print("\nTOP SCORER")
        print(f"Name: {top_scorer['name']}")
        print(f"Runs: {top_scorer['runs']}")

    india_team = Team("India", "India")

    kohli = Batsman(
        "Virat Kohli", 37, "India", 14000, 295
    )

    bumrah = Bowler(
        "Jasprit Bumrah", 32, "India", 150, 100
    )

    india_team.add_player(kohli)
    india_team.add_player(bumrah)

    india_team.display_team()

    match = Match(
        "India",
        "Australia",
        "Melbourne Cricket Ground",
        50
    )

    match.display_match_details()


if __name__ == "__main__":
    main()
