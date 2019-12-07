"""This module allows users to manage an Elo Rating project and calculate the
scoring results.

Users can import data from files or manually operate elements within a project, 
calculate Elo Rating scores, and save data to a file. This class supports 
common operations and statistical methods. `Scoring Neighborhoods on the Earth 
<https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/>`_  is a 
sample Elo Rating project using voting outcomes to measure urban perceptions.
"""

from time import ctime
from functools import wraps
import csv
import os
import statistics


class Element:
    """A class used to represent an element to be added into the Elo Rating
    project.

    An instance of this class is hashable. Instances of this class are the 
    objects to work on in an Elo Rating project. 

    Args:     
        element_id (object): Any hashable object that can be used to uniquely identify the element. 
        info (str, optional): Can store some information about this element such as name, alias, comments, etc. (default='')

    Attributes: 
        element_id (read-only): a hashable object that represents an element. 
        info (str): a string that stores descriptive information about an element. 

    Example: 
    
    >>> import elorating
    >>> el1 = elorating.Element('001774', info='The Uniersity of Chiacgo')
    >>> el2 = elorating.Element('001739', info='Northwestern University')
    >>> el1.element_id
    '001774'
    >>> el1 == el2
    False
    >>> hash(el1)
    -7300844225016213262
    >>> print(el1)
    Element ID: 001774 ; Info: The Uniersity of Chiacgo.
    """

    def __init__(self, element_id, info=''): 
        self.__id = element_id
        self.info = info

    @property
    def element_id(self):
        '''object: Return the id of this element. The id is read-only and 
        cannot be changed over its lifetime. '''
        return self.__id

    def __hash__(self):
        return hash(self.element_id)

    def __eq__(self, element):
        return self.element_id == element.element_id

    def __str__(self): 
        return f'Element ID: {self.element_id} ; Info: {self.info}. '

    def __repr__(self):
        return f'<elorating.Element object> Element ID: {self.element_id} ; Info: {self.info}. '


class Elo: 
    """A class used to manage the Elo Rating project.

    Args: 
        base_score (int): The default score of a newly added element. (default=1000)
        scale (int): The scoring scale used for normalizing the Elo scores to a user-defined scale. 

    Raises: 
        InterruptedError: ``base_score`` is changed during the project. 
        TypeError: Some arguments do not satisfy their type requriements. 

    Attributes: 
        base_score (int): The default score of a newly added element. 


    Example:: 

        >>> import elorating
        >>> scoring_universities = elorating.Elo()
        >>> uchicago = elorating.Element('001774', info='The Uniersity of Chiacgo')
        >>> northwestern = elorating.Element('001739', info='Northwestern University')
        >>> scoring_universities.add(uchicago, northwestern)
        [<elorating.Element object> Element ID: 001774 ; Info: The Uniersity of Chiacgo. , <elorating.Element object> Element ID: 001739 ; Info: Northwestern University. ]
        >>> scoring_universities.update_rating(uchicago, northwestern, 1)
        (1005.0, 995.0)
        >>> scoring_universities.score(uchicago)
        1005.0
        >>> scoring_universities.win_prob(uchicago, northwestern)
        0.5143871841659987
        >>> print(scoring_universities.stats())

        Highest: 1005.0
        Lowest: 995.0
        Mean: 1000.0
        Stdev: 7.0710678118654755
        >>> scoring_universities.remove(northwestern)
        [<elorating.Element object> Element ID: 001739 ; Info: Northwestern University. ]
        >>> scoring_universities.save_data(mute=1)
        './logfiles/elorating_log_Fri_Dec_6_15:45:54_2019.csv'

    """

    def __init__(self, base_score=1000, scale=100): 
        self.element_space = dict()
        self.base_score = base_score
        self.scale = scale

    @property
    def base_score(self):
        """Return the default rating score of a new element.

        The default initial score cannot be change over the project to
        ensure the fairness of the rating.
        """
        return self.__base_score

    @base_score.setter
    def base_score(self, base_score):         
        if isinstance(base_score, int):
            if len(self.element_space) > 0:
                raise InterruptedError(
                    'Change the base_score would affect the current records. Failed. ')
            self.__base_score = base_score
        else:
            raise TypeError(
                "Elo rating must be initiated with an integar base_score. ")

    @property
    def scale(self): 
        """Return the scoring scale of the project, to which the exported data
        would be normalized to."""
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if isinstance(scale, int):
            self.__scale = scale
        else:
            raise TypeError(
                "Elo rating score can be only standardized with a integar [scale]. ")

    class __Decorators:
        """Define the decorators in Elo class."""
        @classmethod
        def check_instance(cls, func):

            @wraps(func)
            def inner(self, *args, **kwargs):
                for arg in args:
                    if not isinstance(arg, Element):
                        raise TypeError(
                            'One of the arguments is not an Element object. ')
                return func(self, *args, **kwargs)

            return inner

    def save_data(self, mute=0):
        """Save the scoring outcome to a csv file with three fields: ``ID``,
        ``Info``, ``RatingScore``.

        Args:
            mute (0 or 1): if mute=1 the file path will not be printed; if mute=0 the file path will be printed when finishing saving data. (default=0)

        Returns:
            The path of the saved data.
        """
        if len(self.element_space) == 0:
            return
        os.makedirs('logfiles/', exist_ok=True)
        filename = f'./logfiles/elorating_log_{(chr(95).join(ctime().split()))}.csv'
        upperbound = self.stats(option='max')
        with open(filename, mode='w') as log:
            log_writer = csv.writer(
                log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow(
                ["ID", "Info", "RatingScore", "StandardizedScore"])
            for element in self.element_space:
                log_writer.writerow([element.element_id, element.info, self.score(
                    element), self.scale * (self.score(element)/upperbound)])
        if mute == 0:
            print(f'Data saved to {filename}')
        return filename

    def import_data(self, filename):
        """Import a data file generated by this file to continue the project
        with the saved outcome.

        The imported file must be a csv file that includes the three fields: ``ID``, ``Info``, ``RatingScore``.
        The CSV should be consistent with the format requirements:
        - ID must be strings splitted by ','
        - Info must be a string
        - RatingScore must be a floating number

        Raises:
            InterruptedError: Try to import data into an non-empty Elo object. Data from files can only be imported into an empty Elo object.
            TyeError: The CSV file does not meet the format requirement.
            KeyError: The CSV file is not found.
        """
        if len(self.element_space) > 0:
            raise InterruptedError('File can only be read into an empty Elo object. ')
        with open(filename, mode='r') as log:
            log_reader = csv.DictReader(
                log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in log_reader:
                try:
                    element = Element(row["ID"], info=row["Info"])
                    self.add(element)
                    self.element_space[element] = float(row['RatingScore'])
                except KeyError as key_er:
                    key_er.args = ('The CSV file is not found. ',)
                    raise
                except TypeError as type_er:
                    type_er.args = (
                        'The CSV file does not meet the format requirement. ',)
                    raise

    @__Decorators.check_instance
    def add(self, *elements): 
        """Add an Element object to an Elo object.

        Args:
            *elements (tuple(Element)): one or more than one Element objects that need to be added into the Elo object.

        Returns:
            A list of Element objects that have been added.

        Raises:
            TypeError: at least one arguments is not Element object.
        """
        for element in elements:
            if element in self:
                raise KeyError(f'{element} is already in the record.')
            else:
                self.element_space[element] = self.base_score
        return list(elements)

    @__Decorators.check_instance
    def remove(self, *elements):
        """Remove an Element object to an Elo object.

        Args:
            *elements (tuple(Element)): one or more than one Element objects that need to be removed into the Elo object.

        Returns:
            A list of Element objects that have been removed.

        Raises:
            TypeError: at least one arguments is not Element object.
        """
        remove_list = []
        for element in elements:
            if not self.element_space.pop(element, None) is None: 
                remove_list.append(element)
        return [element for element in remove_list]

    def __contains__(self, element):
        if element in self.element_space:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.element_space)

    def score(self, element):
        """Return the rating score of an element from current rating records.

        Args:
            element (Element): one Element object that need to be removed into the Elo object.

        Returns:
            The score of this element.

        Raises:
            KeyError: the element is not found in the current Elo object.
        """
        try:
            return self.element_space[element]
        except KeyError as key_er:
            key_er.args = (f'There is no {element} in the record. ', )
            raise

    def win_prob(self, element, opponent):
        """Return the predicted probability of one element beats another
        element.

        Args:
            element (Element): one Element object.
            opponent (Element): another Element object.

        Returns:
            The predicted probability of one element wins another based on current Elo Rating scores.
        """
        return 1.0 / (1 + (10 ** ((self.score(opponent) - self.score(element)) / 400)))

    def update_rating(self, element1, element2, vote=0, K=10):
        """Update the rating score of [element1] and [element2] based on the
        racing or voting outcome.

        Args:
            element1 (Element): one Element object.
            element2 (Element): another Element object.
            vote (0, 1, or 2, optional): vote=0 tie; vote=1 element1 wins; vote=2 element2 wins. (default=0)
            K (int, optional): the parameter for the Elo Rating System. (default=10)

        Returns:
            A tuple of two updated scores for the two elements (tuple(float, float)).

        Raises:
            ValueError: the input value of ``value`` does not satisfy the requirement.
        """
        predict1 = self.win_prob(element1, element2)
        predict2 = self.win_prob(element2, element1)

        if vote == 0:
            outcome1 = 0.5
            outcome2 = 0.5
        elif vote == 1:
            outcome1 = 1
            outcome2 = 0
        elif vote == 2:
            outcome1 = 0
            outcome2 = 1
        else:
            raise ValueError(
                '[vote] can only be 0 (tie), 1 (element1 wins), or 2 (element2 wins). ')

        current_score1 = self.element_space[element1]
        current_score2 = self.element_space[element2]

        new_score1 = current_score1 + K * (outcome1 - predict1)
        new_score2 = current_score2 + K * (outcome2 - predict2)

        self.element_space[element1] = new_score1
        self.element_space[element2] = new_score2

        return (new_score1, new_score2)

    def stats(self, option='all'):
        """Calculate the statistics of current scoring outcome.

        Args:
            option ('all', 'max', 'min, or 'stdev'): option='max': returns the highest score; option='min': returns the lowest score. option='stdev': returns the standard deviation.

        Returns:
            Descriptive statistics (str).
        """
        highest = max(self.element_space.values())
        lowest = min(self.element_space.values())
        mean = statistics.mean(self.element_space.values())
        try:
            std_dev = statistics.stdev(self.element_space.values())
        except statistics.StatisticsError:
            std_dev = 0
        descriptive = f'\nHighest: {highest}\nLowest: {lowest}\nMean: {mean}\nStdev: {std_dev}'
        option_arg = {'all': descriptive,
                      'max': highest,
                      'min': lowest,
                      'stdev': std_dev}
        return option_arg[option]
