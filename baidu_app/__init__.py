# __init__.py
'''
Installation
++++++++++++

Clone the repository of this project to your workplace. 

Install the :mod:`elorating` package. 

>>> pip install /path/to/this/project

Install package dependencies

>>> pip install -r /path/to/this/project/baidu_app/package_requirement.txt


Tutorial
++++++++
To retrive the static panorama street views within a specific area in mainland China, run from terminal: 

>>> cd /path/to/this/project
>>> python3 baidu_app/retrieve_street_view.py
lower bound of latitude: 39.9465
upper bound of latitude: 39.9720
lower bound of longitude: 116.3281
upper bound of longitude: 116.3614
lat_resolution: 5 
lon_resolution: 5
ak: ************************
>>> ls street_image
116.3281,39.9465.jpg            116.336425,39.9465.jpg          116.34475,39.9465.jpg           116.353075,39.9465.jpg          116.3614,39.9465.jpg
116.3281,39.952875.jpg          116.336425,39.952875.jpg        116.34475,39.952875.jpg         116.353075,39.952875.jpg        116.3614,39.952875.jpg
...
'''

# A square area in Beijing. Renmin University - Jimen Bridge - National Library - Xizhimen 
a = '39.9465'
b = '39.9720'
c = '116.3281' 
d = '116.3614'
