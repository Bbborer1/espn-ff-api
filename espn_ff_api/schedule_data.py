from espn_ff_api.constants import WINNER_MAPPING


class Schedule(object):
    def __init__(self, espn_base_class, year):
        self.espn_base_class = espn_base_class
        self.year = year

        self.raw_data = self.espn_base_class.get_data(self.year,
                                                      views=['mSchedule', 'mMatchup',
                                                             'mMatchupScore', 'mPlayers',
                                                             'mScoreboard'])

        self.games = self.__parse_games()

    def __parse_games(self):
        games = []
        for game in self.raw_data.get('schedule'):
            schedule_game = ScheduleGame(game)
            games.append(schedule_game)
        return games


class ScheduleGame(object):
    def __init__(self, raw_game_data):
        self.raw_game_data = raw_game_data

        self.week = self.raw_game_data.get('matchupPeriodId')

        self.home_team = ScheduleTeam(self.raw_game_data.get('home'))

        self.away_team = ScheduleTeam(self.raw_game_data.get('away'))

        self.winner = WINNER_MAPPING.get(self.raw_game_data.get('winner'))

    def is_completed(self):
        if self.winner:
            return True
        return False

    def is_playoff_game(self):
        if self.raw_game_data.get('playoffTierType') != 'NONE':
            return True
        return False


class ScheduleTeam(object):
    def __init__(self, raw_team_data):
        self.raw_team_data = raw_team_data

        self.score = self.raw_team_data.get('totalPoints')
        self.team_id = self.raw_team_data.get('teamId')
