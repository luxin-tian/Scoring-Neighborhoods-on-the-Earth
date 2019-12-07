"""This program calls the :mod:`pp2_app.pp2_elorating_app` module to calculate
the Elo Rating scores of places in some cities in terms of some dimensions and
export interactive maps to .html files.

To run from terminal::

    >>> cd /path/to/this/project
    >>> python3 pp2_app/pp2_visualization_app.py
    Please input the path of Place Pulse 2.0 data <vote.csv>: /Users/tianluxin/Desktop/mpcs-python/project/autumn-2019-project-luxin-tian/data_and_files/pp2_20161010/votes.csv
    cities: Chicago,Los Angeles
    categories: safety,lively

    This program uses the data from http://pulse.media.mit.edu/data/ to demostrate an application of the elorating module.

    Dimension: safety
    File length: 1223650
    Reading Files |████████████████████████████████| 1223649/1223650

    number of Elements: 111367
    Loading Elements |████████████████████████████████| 111367/111367

    number of valid records: 368926
    Calculating Elo Scores |████████████████████████████████| 368926/368926


    Data saved to ./logfiles/elorating_log_Fri_Dec_6_17:51:27_2019.csv


    Highest: 1134.3642935436123
    Lowest: 873.5102761124806
    Mean: 1000.0
    Stdev: 15.013932094550254
    Interactive map saved to ./vis/pp2_Chicago_safety.html
    Interactive map saved to ./vis/pp2_Los Angeles_safety.html

    This program uses the data from http://pulse.media.mit.edu/data/ to demostrate an application of the elorating module.

    Dimension: lively
    File length: 1223650
    Reading Files |████████████████████████████████| 1223649/1223650

    number of Elements: 110890
    Loading Elements |████████████████████████████████| 110890/110890

    number of valid records: 267292
    Calculating Elo Scores |████████████████████████████████| 267292/267292


    Data saved to ./logfiles/elorating_log_Fri_Dec_6_17:52:25_2019.csv


    Highest: 1129.7027310192975
    Lowest: 880.1816699253212
    Mean: 1000.0
    Stdev: 12.060674162814488
    Interactive map saved to ./vis/pp2_Chicago_lively.html
    Interactive map saved to ./vis/pp2_Los Angeles_lively.html

To import in Python(in the workplace '/path/to/this/project'):

    import pp2_app.pp2_elorating_app
"""
import csv
import folium
import numpy as np
import elorating
from pp2_app import pp2_elorating_app
import copy
import os


def _city_coordinates(cityname):
    """Return the geographical coordinates of a city.

    Args:
        cityname(str): one of the 56 cities covered by `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_.

    Returns:
        A geographical coordinates (tuple(float, float)).
    """
    citydict = {
        'Chicago': (41.881832, -87.623177),
        'Paris': (48.8566, 2.3522),
        'Valparaiso': (-33.0472, -71.6127),
        'New York': (40.7128, -74.0060),
        'Washington DC': (38.9072, -77.0369),
        'Tel Aviv': (32.0853, 34.7818),
        'London': (51.5074, -0.1278),
        'Singapore': (1.3521, 103.8198),
        'Boston': (42.3601, -71.0589),
        'Amsterdam': (52.3667, 4.8945),
        'Sao Paulo': (-23.5505, -46.6333),
        'San Francisco': (37.7749, -122.4194),
        'Copenhagen': (55.6761, 12.5683),
        'Mexico City': (19.4326, -99.1332),
        'Sydney': (-33.8688, 151.2093),
        'Taipei': (25.0330, 121.5654),
        'Rio De Janeiro': (-22.9068, -43.1729),
        'Bangkok': (13.7563, 100.5018),
        'Stockholm': (59.3293, 18.0686),
        'Hong Kong': (22.3193, 114.1694),
        'Berlin': (52.5200, 13.4050),
        'Philadelphia': (39.9526, -75.1652),
        'Seattle': (47.6062, -122.3321),
        'Melbourne': (-37.8136, 144.9631),
        'Dublin': (53.3498, -6.2603),
        'Milan': (45.4642, 9.1900),
        'Los Angeles': (34.0522, -118.2437),
        'Guadalajara': (20.6597, -103.3496),
        'Moscow': (55.7558, 37.6173),
        'Barcelona': (41.3851, 2.1734),
        'Rome': (41.9028, 12.4964),
        'Belo Horizonte': (-19.9167, -43.9345),
        'Helsinki': (60.1699, 24.9384),
        'Tokyo': (35.6804, 139.7690),
        'Santiago': (-33.4489, -70.6693),
        'Portland': (45.5051, -122.6750),
        'Prague': (50.0755, 14.4378),
        'Atlanta': (33.7490, -84.3880),
        'Toronto': (43.6532, -79.3832),
        'Bucharest': (44.4268, 26.1025),
        'Lisbon': (38.7223, -9.1393),
        'Kyoto': (35.0116, 135.7681),
        'Montreal': (45.5017, -73.5673),
        'Madrid': (40.4168, -3.7038),
        'Kiev': (50.4501, 30.5234),
        'Warsaw': (52.2297, 21.0122),
        'Glasgow': (55.8642, -4.2518),
        'Minneapolis': (44.9778, -93.2650),
        'Denver': (39.7392, -104.9903),
        'Munich': (48.1351, 11.5820),
        'Bratislava': (48.1486, 17.1077),
        'Zagreb': (45.8150, 15.9819),
        'Cape Town': (-33.9249, 18.4241),
        'Johannesburg': (-26.2041, 28.0473),
        'Houston': (29.7604, -95.3698),
        'Gaborone': (-24.6282, 25.9231)
    }
    return citydict[cityname]


def to_map(filename, cityname_list, category_list):
    """Call the :mod:`pp2_app.pp2_elorating_app` to calculate the Elo Rating
    score of palces in some cities in terms of some dimensions.

    Args:
        filename (str): the file path of the 'vote.csv' file downloaded from `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_.
        cityname_list (list(str)): a list of city names, of which the Elo Rating scores will be calculated.
        category_list (list(str)): a list of measurement dimensions in 'safety', 'lively', 'wealthy', 'beautiful', 'depressing', or 'boring'.

    Export:
        Interactive maps will be exported to './vis/' in .html files.
    """
    file_output = {}

    def _hex_color(score):
        score_array = np.array(list(city.values()))
        q1 = np.quantile(score_array, 0.25)
        q3 = np.quantile(score_array, 0.75)
        color_value = 255 * 2 * (score - q1) / (q3 - q1)
        if color_value <= 255:
            r = 255
            g = int(color_value)
        elif color_value > 255:
            r = int(255 - (color_value - 255))
            g = 255
        return '#' + ('00' + hex(r)[2:])[-2:] + ('00' + hex(g)[2:])[-2:] + '00'

    for category in category_list:
        file_output = pp2_elorating_app.main(filename, category)

        for cityname in cityname_list:
            city = dict()
            with open(file_output, 'r') as fh:
                reader = csv.DictReader(fh, delimiter=',')
                for row in reader:
                    lat = float(row['Info'].split(',')[0])
                    lon = float(row['Info'].split(',')[1])
                    if (
                        abs(lat - _city_coordinates(cityname)[0]) < 1 and
                        abs(lon - _city_coordinates(cityname)[1]) < 1
                    ):
                        city[(lat, lon)] = float(row['RatingScore'])

            m = folium.Map(
                location=list(_city_coordinates(cityname)),
                zoom_start=11)

            for lat, lon in city.keys():
                folium.Circle([lat, lon],
                              radius=50,
                              tooltip=city[(lat, lon)],
                              color=(_hex_color(city[(lat, lon)]))
                              ).add_to(m)

            os.makedirs('logfiles/', exist_ok=True)
            m.save(f'./vis/pp2_{cityname}_{category}.html')
            print(
                f'Interactive map saved to ./vis/pp2_{cityname}_{category}.html')


if __name__ == '__main__':
    to_map(
        input('Please input the path of Place Pulse 2.0 data <vote.csv>: '),
        input('cities: ').split(','),
        input('categories: ').split(','))
