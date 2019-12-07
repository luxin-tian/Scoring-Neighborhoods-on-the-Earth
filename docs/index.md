# Scoring Neighborhoods on the EARTH

This project aims at using the [Elo Rating System](https://en.wikipedia.org/wiki/Elo_rating_system) to quantitatively measure urban perceptions around the world. The measurement is based on digital surveys to humans, in which users are asked to compare two street view images in terms of some dimensions, for example, safety. 

As a by-product of this project, I write a ``elorating`` module in Python, which can be generally used for other scoring projects that employ [Elo Rating System](https://en.wikipedia.org/wiki/Elo_rating_system). Particularly, as a computational economist, I note that even though [Elo Rating System](https://en.wikipedia.org/wiki/Elo_rating_system) was originally designed to measure the relative skill levels of chess players based on competition records, it can be used as a `[Social Welfare Function](https://en.wikipedia.org/wiki/Social_welfare_function) that reveals collective preferences from individual preferences. 

Currently, I use the survey data from [Place Pulse 2.0](http://pulse.media.mit.edu/data/), which covers 56 cities from 28 countries across 6 continents and keeps ongoing. I provide the reproducible Python scripts that calculate the Elo Rating scores in the repository of this project as a demonstration of the ``elorating`` module. I also visualize the outcome on [interactive maps](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/). 

Furthermore, since [Place Pulse 2.0](http://pulse.media.mit.edu/data/) retrieves street view images from [Google Maps](https://developers.google.com/maps/documentation), it does not cover mainland China (Google ends their consumer services in China since 2010, see more on [Wikipedia](https://en.wikipedia.org/wiki/Google_China)). I plan to extend this project to cover mainland China in the future using street view images provided by [Baidu Map](https://lbsyun.baidu.com). For now, I finished a program in Python that retrieves street view images. I have included this program in the repository. 



## Interactive Maps
There are six dimensions used for measuring the perception of a city. Choose one to explore: 
- [Safety](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/safety)
- [Lively](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/lively)
- [Wealthy](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/wealthy)
- [Beautiful](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/beautiful)
- [Depressing](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/depressing)
- [Boring](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/boring)

## Algorithm and Methods
[Elo Rating System](https://en.wikipedia.org/wiki/Elo_rating_system)


## Documentation
[Documentation of Scoring Neighborhoods on the EARTH](https://luxin-tian.github.io/Scoring-Neighborhoods-on-the-Earth/build/html/index.html)

## About me
[Luxin Tian](https://luxin-tian.github.io/profile/) at the University of Chicago

## Computational Social Science
Learn more about the impact of [computational social sciences](https://macss.uchicago.edu) in the digital age. 