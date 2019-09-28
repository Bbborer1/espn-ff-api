from espn_ff_api.constants import LEAGUE_VIEWS
from espn_ff_api.espn_base_class import EspnBase


class LeagueData(object):

    def __init__(self, espn_base_class, year):
        self.espn_base_class = espn_base_class
        self.year = year

        self.raw_data = self.espn_base_class.get_data(self.year,
                                                      views=LEAGUE_VIEWS)

        # Pull from base level of raw data
        self.settings = self.raw_data.get('settings')
        self.previous_seasons = self.raw_data.get('status').get('previousSeasons')

        # Use raw data to parse these values
        self.league_members = self.__parse_members()
        self.teams = self.__parse_teams()

    def __parse_teams(self):
        teams = self.raw_data.get('teams')
        formatted_teams = {}
        for team in teams:
            formatted_team = LeagueTeam(team, self.league_members)
            formatted_teams.update({formatted_team.team_id: formatted_team})

        return formatted_teams

    def __parse_members(self):
        league_members = {}
        for member in self.raw_data.get('members'):
            member_id = member.get('id')
            first_name = member.get('firstName')
            last_name = member.get('lastName')

            league_members.update({member_id:
                {
                    'member_id': member_id,
                    'first_name': first_name,
                    'last_name': last_name
                }
            })
        return league_members


class LeagueTeam(object):
    def __init__(self, raw_data, member_data):
        self._member_data = member_data
        self.raw_data = raw_data
        self.name = self.raw_data.get('location') + ' ' + self.raw_data.get('nickname')
        self.projected_rank = self.raw_data.get('currentProjectedRank')
        self.division = self.raw_data.get('divisionId')
        self.team_id = self.raw_data.get('id')
        self.playoff_seed = self.raw_data.get('playoffSeed')
        self.points = self.raw_data.get('points')
        self.record = self.raw_data.get('record')

        transaction_counter = self.raw_data.get('transactionCounter')

        self.total_acquisitions = transaction_counter.get('acquisitions')
        self.acquisitions_budget_spent = transaction_counter.get('acquisitionBudgetSpent')

        self.owners = self.__parse_owners()

    def __parse_owners(self):
        owners = []
        for owner in self.raw_data.get('owners'):
            member_data = self._member_data.get(owner)
            owners.append(member_data)

        return owners


def main():
    espn = EspnBase()
    league = LeagueData(espn, 2019)

    print('here')


main()
