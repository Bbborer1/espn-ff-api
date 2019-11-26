

LEAGUE_VIEWS = ['mSettings', 'mTeam']
SCHEDULE_VIEWS = ['mSchedule', 'mMatchup', 'mMatchupScore', ]
PLAYER_VIEWS = ['kona_player_info']

WINNER_MAPPING = {'AWAY': 'away',
               'HOME': 'home',
               'UNDECIDED': None}


POSITION_MAP = {
    1: 'QB',
    16: 'DEF',
    5: 'K',
    3: 'WR',
    4: 'TE',
    2: 'RB'
}


STARTERS = {
    'QB': 20,
    'DEF': 10,
    'K': 10,
    'WR': 20,
    'TE': 10,
    'RB': 20,
    'FLEX': 10
}

FLEX = ['WR', 'TE', 'RB']


STAT_MAP = {53: 'points for receptions',
            102: 'related to defense',
            72: 'fumble',
            24: 'rushing yard points',
            25: 'rushing td points',
            26: 'two point conversion points',
            42: 'reception yard points',
            43: 'reception td points',
            44: 'two point conversion - not sure if rushing or reception',
            8: 'passing yard points',
            4: 'passing td points',
            }