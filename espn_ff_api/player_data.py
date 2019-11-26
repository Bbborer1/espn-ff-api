from espn_ff_api.constants import PLAYER_VIEWS


class PlayerData(object):

    def __init__(self, espn_base_class, year):
        self.espn_base_class = espn_base_class
        self.year = year

        self.raw_data = self.get_raw_data()

        self.players = self.get_players()

    def get_raw_data(self):
        raw_data_by_week = {}
        for week in range(1, 12):
            raw_data = self.espn_base_class.get_data(self.year,
                                                     views=PLAYER_VIEWS,
                                                     scoringPeriodId=week)
            raw_data_by_week.update({week: raw_data})

        return raw_data_by_week

    def get_players(self):
        players = {}
        for week, raw_player_data in self.raw_data.items():
            position_dict = {}
            for player in raw_player_data.get('players'):
                weekly_player = WeeklyPlayer(player, week, self.year)
                position = position_dict.get(weekly_player.position_id, {})
                position.update({weekly_player.name: weekly_player})

                position_dict.update({weekly_player.position_id: position})

            players.update({week: position_dict})
        return players

    @staticmethod
    def order_dict(players):
        sorted_players = sorted(players.items(),
                                key=lambda x: x[1].actual_stats.get('score'),
                                reverse=True)
        return [player for name, player in sorted_players]

    def weekly_ranks(self):
        sorted_data = {}
        for week, weekly_data in self.players.items():
            weekly_sorted = sorted_data.get(week, {})
            for position, position_dict in weekly_data.items():
                weekly_sorted.update({position: self.order_dict(position_dict)})
            sorted_data.update({week: weekly_sorted})

        return sorted_data


class WeeklyPlayer(object):
    def __init__(self, raw_player_data, week, year):
        self.week = week
        self.year = year
        self.raw_player_data = raw_player_data
        self.raw_player_details = self.raw_player_data.get('player')
        self.raw_player_stats = self.raw_player_details.get('stats')
        self.position_id = self.raw_player_details.get('defaultPositionId')
        self.name = self.raw_player_details.get('fullName')
        self.average_auction_value = self.raw_player_details.get('ownership').get('auctionValueAverage')
        self.on_team_id = self.raw_player_data.get('onTeamId')
        self.draft_auction_value = self.raw_player_data.get('keeperValueFuture')



    @property
    def is_free_agent(self):
        return self.raw_player_data.get('onTeamId') == 0

    @property
    def actual_raw_stats(self):
        for stat_dict in self.raw_player_stats:
            year_match = stat_dict.get('seasonId') == self.year
            weeks_match = stat_dict.get('scoringPeriodId') == self.week
            actual_values = stat_dict.get('statSourceId') == 0
            if year_match and weeks_match and actual_values:
                return stat_dict
        return {}

    @property
    def actual_stats(self):

        return {
            'score': round(self.actual_raw_stats.get('appliedTotal', 0), 3),
            'targets': self.actual_raw_stats.get('stats', {}).get('58', 0),
            'receptions': self.actual_raw_stats.get('stats', {}).get('53', 0)
        }
