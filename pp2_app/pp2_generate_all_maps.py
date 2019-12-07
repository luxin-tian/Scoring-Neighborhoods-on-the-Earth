
"""Running this program will calculate the Elo Rating socres of the places in
all the cities covered by Place Pulse 2.0 <http://pulse.media.mit.edu/data/> in
terms of all the dimensions and export all the interactive maps.

To run from terminal:

    >>> cd /path/to/this/project
    >>> python3 pp2_app/pp2_generate_all_maps.py
    (... the outputs are omitted)
"""
from pp2_app import pp2_visualization_app


def main():
    citylist = [
        'Chicago',
        'Paris',
        'Valparaiso',
        'New York',
        'Washington DC',
        'Tel Aviv',
        'London',
        'Singapore',
        'Boston',
        'Amsterdam',
        'Sao Paulo',
        'San Francisco',
        'Copenhagen',
        'Mexico City',
        'Sydney',
        'Taipei',
        'Rio De Janeiro',
        'Bangkok',
        'Stockholm',
        'Hong Kong',
        'Berlin',
        'Philadelphia',
        'Seattle',
        'Melbourne',
        'Dublin',
        'Milan',
        'Los Angeles',
        'Guadalajara',
        'Moscow',
        'Barcelona',
        'Rome',
        'Belo Horizonte',
        'Helsinki',
        'Tokyo',
        'Santiago',
        'Portland',
        'Prague',
        'Atlanta',
        'Toronto',
        'Bucharest',
        'Lisbon',
        'Kyoto',
        'Montreal',
        'Madrid',
        'Kiev',
        'Warsaw',
        'Glasgow',
        'Minneapolis',
        'Denver',
        'Munich',
        'Bratislava',
        'Zagreb',
        'Cape Town',
        'Johannesburg',
        'Houston',
        'Gaborone']

    catelist = [
        'safety',
        'lively',
        'wealthy',
        'beautiful',
        'depressing',
        'boring']

    pp2_visualization_app.to_map(
        input('pp2 data file path: '),
        sorted(citylist),
        catelist)


if __name__ == '__main__':
    main()
