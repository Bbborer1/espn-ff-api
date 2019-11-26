from espn_ff_api.constants import POSITION_MAP
from espn_ff_api.espn_base_class import EspnBase
from espn_ff_api.player_data import PlayerData

import csv


def count_times_startable(sorted_ranks):
    player_counts = {}
    for week, weekly_data in sorted_ranks.items():
        for position, players_list in weekly_data.items():
            position_counts = player_counts.get(position, {})

            for i in range(len(players_list)):
                player = players_list[i]
                top_ten = False
                top_twenty = False
                top_thirty = False
                if i < 10:
                    top_ten = True
                if i < 20:
                    top_twenty = True
                if i < 30:
                    top_thirty = True
                player_data = position_counts.get(player.name, {
                    'times_top_10': 0,
                    'times_top_20': 0,
                    'times_top_30': 0,
                    'points_scored': 0,
                    'player': player})
                position_counts.update({player.name:
                                            {'player': player,
                                             'times_top_20': player_data.get(
                                                 'times_top_20') + 1 if top_twenty else player_data.get(
                                                 'times_top_20'),
                                             'times_top_10': player_data.get(
                                                 'times_top_10') + 1 if top_ten else player_data.get(
                                                 'times_top_10'),
                                             'times_top_30': player_data.get(
                                                 'times_top_30') + 1 if top_thirty else player_data.get(
                                                 'times_top_30'),
                                             'points_scored': player_data.get(
                                                 'points_scored') + player.actual_stats.get(
                                                 'score', 0)}})

            player_counts.update({position: position_counts})
    return player_counts


def format_records(records):
    return_values = []
    for position_id, position_values in records.items():
        position = POSITION_MAP.get(position_id)
        for player_name, player_data in position_values.items():
            if player_data.get('times_top_30', 0) > 0:
                new_dict = {'name': player_name,
                            'times_top_10': player_data.get('times_top_10'),
                            'times_top_20': player_data.get('times_top_20'),
                            'times_top_30': player_data.get('times_top_30'),
                            'points_scored': player_data.get('points_scored'),
                            'position': position,
                            'draft_auction_value': player_data.get('player').draft_auction_value
                            }
                return_values.append(new_dict)

    return return_values


def main():
    espn = EspnBase()
    s = PlayerData(espn, 2019)

    y = s.weekly_ranks()

    z = count_times_startable(y)

    master_list = format_records(z)
    with open('aggregate_stats.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'position', 'times_top_10', 'times_top_20', 'times_top_30',
                      'points_scored', 'draft_auction_value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="|",
                                extrasaction='ignore')

        writer.writeheader()
        writer.writerows(master_list)

    print('here')


main()
