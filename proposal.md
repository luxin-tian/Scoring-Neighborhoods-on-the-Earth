# Scoring Neighborhoods in Beijing
An Application of the Elo Rating System in Revealing Collective Preferences 

## Overview
Beijing is making significant progress in city renewal. While many neighborhoods have undergone tremendous changes with the efforts made by the government and social organizations, many others remain unsatisfactory. This project aims at scoring the perceived livability of neighborhoods within certain areas in Beijing based on binary voting results collected from volunteers and, ideally, visualizing the results on the map. 

## Technical Breakdowns
The main part of these projects is expected to include the following components. 

### ```EloRating``` Package

This package would provide a toolkit that employs the [Elo Rating System](https://en.wikipedia.org/wiki/Elo_rating_system) algorithm for revealing the collective preferences among a set of elements based on individual binary voting outcomes. 

### ```BinaryVote``` Package
This function presents two randomly selected elements from the set and queries the users to make comparisons, and then it stores the voting outcomes into a file. 

### Scoring Neighborhoods in Beijing
As an application of these toolkits, I plan to crawl static street view images from [Baidu Maps](https://lbsyun.baidu.com/), which provides free APIs, and engage my friends as volunteers to use a program calling the ```BinaryVote``` package and cast their votes on sample street view images. Then I will use the ```EloRating``` package to generate the ranking of the sample neighborhoods in terms of perceived livability by calculating their Elo ratings. Finally, I will try to visualize the results on the map. To summarize the steps: 

- Making API calls
- Voting data collection
- Elo Rating
- Geographical data visualization

The following third-party packages are expected to be useful: 
- ```Selenium```
- ```Request```
- ```NumPy```
- ```Pandas```

## Feasibility Assessment and Backup Plans
 Predicting collective preferences from revealed individual preferences is a common problem in social sciences. Therefore, the proposed ```EloRating``` package and ```BinaryVote``` package can be used for general purposes on inferring collective choices. In case that calling APIs and visualizing geographical data require much more advanced techniques beyond my capability, I would turn to use the public data from the [Place Pulse](http://pulse.media.mit.edu/data/) study, which includes individual voting outcomes on six dimensions of characteristics of 56 cities, and present the ranking result of geographical positions in a city in terms of some characteristics as a demonstration of using the packages. Apart from calling APIs and visualizing geographical data, this backup plan would also involve reading and writing files, and making use of functions, classes, and packages. 