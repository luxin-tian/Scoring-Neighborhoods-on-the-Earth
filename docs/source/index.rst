.. Scoring Neighborhoods on the Earth documentation master file, created by
 sphinx-quickstart on Fri Dec 6 13:25:31 2019.
 You can adapt this file completely to your liking, but it should at least
 contain the root `toctree` directive.

Documentation of Scoring Neighborhoods on the Earth Project
***********************************************************
.. toctree::
 :maxdepth: 2
 :caption: Contents: 

.. contents::

Overview about this Project
===========================
This project aims at using the `Elo Rating System <https://en.wikipedia.org/wiki/Elo_rating_system>`_ to quantitatively measure urban perceptions around the world. The measurement is based on digital surveys to humans, in which users are asked to compare two street view images in terms of some dimensions, for example, safety. 

As a by-product of this project, I write a :mod:`elorating` module in Python, which can be generally used for other scoring projects that employ `Elo Rating System <https://en.wikipedia.org/wiki/Elo_rating_system>`_. Particularly, as a computational economist, I note that even though `Elo Rating System <https://en.wikipedia.org/wiki/Elo_rating_system>`_ was originally designed to measure the relative skill levels of chess players based on competition records, it can be used as a `Social Welfare Function <https://en.wikipedia.org/wiki/Social_welfare_function>`_ that reveals collective preferences from individual preferences. 

Currently, I use the survey data from `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_, which covers 56 cities from 28 countries across 6 continents and keeps ongoing. I provide the reproducible Python scripts that calculate the Elo Rating scores in the repository of this project as a demonstration of the :mod:elorating module. I also visualize the outcome on `interactive maps <https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/>`_. 

Furthermore, since `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_ retrieves street view images from `Google Maps <https://developers.google.com/maps/documentation>`_, it does not cover mainland China (Google ends their consumer services in China since 2010, see more on `Wikipedia <https://en.wikipedia.org/wiki/Google_China>`_). I plan to extend this project to cover mainland China in the future using street view images provided by `Baidu Map <https://lbsyun.baidu.com/>`_. For now, I finished a program in Python that retrieves street view images. I have included this program in the repository. 

elorating package
=================
.. automodule:: elorating
 :members:

elorating module
----------------
.. automodule:: elorating.elorating
 :members:


Scoring Neighborhoods in 56 Cities (based on `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_)
===================================================================================================

Overview
--------
`Place Pulse <http://pulse.media.mit.edu/data/>`_ is a crowdsourcing data collection project hosted by `MIT <mit.edu>`_. In this project, participants would be represented with two street view images for each time, and they would be asked to indicate their comparison between the two images in terms of one of the following questions (cited from `Place Pulse <http://pulse.media.mit.edu/data/>`_): 

 - Which Place Looks Safer?
 - Which Place Looks Wealthier?
 - Which Place Looks More Beautiful?
 - Which Place Looks More Boring?
 - Which Place Looks Livelier?
 - Which Place Looks More Depressing?

The second study `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_ "extends the data collection to 56 cities from 28 countries across 6 continents", making up a dataset containing 1,223,650 inidividual voting records. 

As a demonstration of using the :mod:`elorating` module, I calculate the urban perceptions of all the 56 cities covered by the study based on the `Place Pulse 2.0 <http://pulse.media.mit.edu/data/>`_ data. The reproducible Python scripts are included in the repository of this project. 

Interactive maps
----------------


Documentation of pp2_app
------------------------
.. automodule:: pp2_app

pp2_elorating_app reference
+++++++++++++++++++++++++++
.. automodule:: pp2_app.pp2_elorating_app
 :members:


pp2_visualization_app reference
+++++++++++++++++++++++++++++++
.. automodule:: pp2_app.pp2_visualization_app
 :members:

pp2_generate_all_maps reference
+++++++++++++++++++++++++++++++
.. automodule:: pp2_app.pp2_generate_all_maps


Scoring Neighborhoods in Mainland China (in progress)
=====================================================
**This part is still in progress.**
I plan to extend this project to cover mainland China in the future using street view images provided by `Baidu Map <https://lbsyun.baidu.com/>`_. For now, I finished a program in Python that retrieves street view images from `Baidu Map <https://lbsyun.baidu.com/>`_ within the geographical areas that the user specifies. I have include this program in the repository and provide the documentation for it. 

Documentation of baidu_app
--------------------------
.. automodule:: baidu_app

retrieve_street_view reference
++++++++++++++++++++++++++++++
.. automodule:: baidu_app.retrieve_street_view
 :members: 

baidu_api_request reference
+++++++++++++++++++++++++++
.. automodule:: baidu_app.baidu_api_request
 :members:

coordinate_generator reference
++++++++++++++++++++++++++++++
.. automodule:: baidu_app.coordinate_generator
 :members: 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

