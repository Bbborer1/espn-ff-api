import os

import requests


class EspnBase(object):

    def __init__(self, league_id=None, espn_swid=None, espn_s2_code=None,
                 league_type='FFL'):
        self.league_id = league_id
        self.espn_swid = espn_swid
        self.espn_s2_code = espn_s2_code
        self.league_type = league_type

        if not self.league_id:
            self.league_id = os.environ.get('LEAGUE_ID')

        if not self.espn_swid:
            self.espn_swid = os.environ.get('ESPN_SWID')
        if not self.espn_s2_code:
            self.espn_s2_code = os.environ.get('ESPN_S2_CODE')

        self.unformatted_url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/{0}/segments/0/leagues/" + self.league_id
        self.unformatted_historic_url = f"https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + self.league_id + "?seasonId={0}"
        self.basic_url = 'https://fantasy.espn.com/apis/v3/games'

    def check_creds(self):
        if not self.league_id or not self.espn_swid or not self.espn_s2_code:
            raise RuntimeError('Missing credentials')

    def get_basic_espn_data(self):
        # get basic league data with no creds
        r = requests.get(self.basic_url)
        r.raise_for_status()
        response_data = r.json()
        for result in response_data:
            if result.get('abbrev') == self.league_type:
                return result
        raise RuntimeError(f'Could not find valid espn data for {self.league_type}')

    def get_url(self, year):
        basic_data = self.get_basic_espn_data()
        current_season_year = basic_data.get('currentSeason').get('id')

        if current_season_year == year:
            return self.unformatted_url.format(year)
        else:
            return self.unformatted_historic_url.format(year)

    def get_cookies(self):
        self.check_creds()
        return {'SWID': self.espn_swid,
                'espn_s2': self.espn_s2_code}

    def get_data(self, year, views=None, **kwargs):

        url = self.get_url(year)
        cookies = self.get_cookies()

        params = {'view': views}
        params.update(kwargs)

        r = requests.get(url,
                         params=params,
                         cookies=cookies)
        print(r.url)

        response_data = r.json()
        if type(response_data) == list and len(response_data) == 1:
            return response_data[0]
        return response_data
