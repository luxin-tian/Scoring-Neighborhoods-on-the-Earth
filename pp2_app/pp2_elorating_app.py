"""This program uses http://pulse.media.mit.edu/data/ to demostrate an
application of the elorating module.

To run from terminal::

   >>> cd /path/to/this/project
   >>> python3 pp2_app/pp2_elorating_app.py
   Please input the path of Place Pulse 2.0 data <vote.csv>: .../pp2_20161010/votes.csv
   Please choose a category: safety, lively, wealthy, beautiful, depressing, or boring: safety

   This program uses the data from http://pulse.media.mit.edu/data/ to demostrate an application of the elorating module.

   Dimension: safety

   File length: 1223650
   Reading Files |████████████████████████████████| 1223649/1223650

   number of Elements: 111367
   Loading Elements |████████████████████████████████| 111367/111367

   number of valid records: 368926
   Calculating Elo Scores |████████████████████████████████| 368926/368926


   Data saved to ./logfiles/elorating_log_Fri_Dec_6_16:54:57_2019.csv



   Highest: 1134.3642935436123
   Lowest: 873.5102761124806
   Mean: 1000.0
   Stdev: 15.013932094550254

To import in Python (in the workplace '/path/to/this/project')::

    import pp2_app.pp2_elorating_app
"""
import csv
import elorating
from progress.bar import ShadyBar


def main(filename, category):
    """Calculate the Elo Rating scores of the locations in terms of certain
    dimension and export the data into a csv file.

    Args:
        filename (str): the file path of the 'vote.csv' file downloaded from `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_.
        category (str): can be one of the six dimensions: 'safety', 'lively', 'wealthy', 'beautiful', 'depressing', or 'boring'.

    Returns:
        The path of the exported data.
    """
    print('\nThis program uses the data from http://pulse.media.mit.edu/data/ to demostrate an application of the elorating module. \n')
    print(f'Dimension: {category}\n')
    elo_project = elorating.Elo()
    vote_data = {}
    element_set = set()

    with open(filename, 'r') as fh:
        count_line = sum(1 for line in fh)
        print(f'File length: {count_line}')

    with open(filename, 'r') as fh:
        reader = csv.DictReader(fh, delimiter=',')
        index = 0
        with ShadyBar('Reading Files', max=count_line) as bar:
            for index, row in enumerate(reader):
                if row['category'] == category:
                    left_id = row['left_id']
                    right_id = row['right_id']

                    left_location = ','.join(
                        [row['left_lat'], row['left_long']])
                    right_location = ','.join(
                        [row['right_lat'], row['right_long']])

                    left_element = elorating.Element(
                        left_id, info=left_location)
                    right_element = elorating.Element(
                        right_id, info=right_location)

                    vote_data[(left_element, right_element, index)
                              ] = row["winner"]
                    element_set.add(left_element)
                    element_set.add(right_element)
                bar.next()

    votedict = {"left": 1,
                "right": 2,
                "equal": 0}

    count_element = len(element_set)
    print(f'\nnumber of Elements: {count_element}')
    with ShadyBar('Loading Elements', max=count_element) as bar:
        for element in element_set:
            elo_project.add(element)
            bar.next()

    count_vote_data = len(vote_data)
    print(f'\nnumber of valid records: {count_vote_data}')
    with ShadyBar('Calculating Elo Scores', max=count_vote_data) as bar:
        for left_element, right_element, index in vote_data:
            vote = votedict[vote_data[(left_element, right_element, index)]]
            elo_project.update_rating(left_element, right_element, vote)
            bar.next()

    print('\n')
    file_output = elo_project.save_data()

    print('\n', elo_project.stats())

    return file_output


if __name__ == "__main__":
    main(input('Please input the path of Place Pulse 2.0 data <vote.csv>: '), 
         input('Please choose a category: safety, lively, wealthy, beautiful, depressing, or boring: '))
