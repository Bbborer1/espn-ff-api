from espn_ff_api.espn_base_class import EspnBase
from espn_ff_api.schedule_data import Schedule


def main():
    espn = EspnBase()
    s = Schedule(espn, 2019)

    print('here')


main()
