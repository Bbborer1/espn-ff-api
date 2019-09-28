# SETTINGS = 'settings'
# ROSTERS = 'rosters'
# SCORE_BOARDS = 'score_boards'
# TOP_PERFORMERS = 'top_performers'
# TEAMS = 'teams'
# MODULAR = 'modular'
# NAV = 'nav'
# SCHEDULE = 'schedule'
# MATCHUP = 'matchup'
# MATCHUP_SCORE = 'matchup_score'
# PLAYERS = 'players'
# KONA_PLAYER_INFO = 'kona_player_info'
# DRAFT_INFO = 'draft_info'
# DRAFT_RECAP = 'draft_recap'
#
# PARAM_MAPPINGS = {SETTINGS: 'mSettings',
#                   ROSTERS: 'mRoster',
#                   SCORE_BOARDS: 'mScoreboard',
#                   TOP_PERFORMERS: 'mTopPerformers',
#                   TEAMS: 'mTeam',
#                   MODULAR: 'modular',
#                   NAV: 'mNav',
#                   SCHEDULE: 'mSchedule',
#                   MATCHUP: 'mMatchup',
#                   MATCHUP_SCORE: 'mMatchupScore',
#                   PLAYERS: 'mPlayers',
#                   KONA_PLAYER_INFO: 'kona_player_info',
#                   DRAFT_INFO: 'mDraftDetail',
#                   DRAFT_RECAP: 'mDraftRecap'}

LEAGUE_VIEWS = ['mSettings', 'mTeam']

SCHEDULE_VIEWS = ['']


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