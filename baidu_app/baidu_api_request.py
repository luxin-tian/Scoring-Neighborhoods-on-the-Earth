import requests
import os


def get_street_view(ak, location, width=1024, height=512, fov=360):
    """Request a static panorama street image from Baidu Map.

    Args:
        ak (str): Baidu developer API ak token.
        location (str): a string contains the geographical coordinates of a location '<longitude>,<latitude>'.
        width (int): the width of the street view image. (default=1024)
        height (int): the height of the street view image. (default=512)
        fov (int): the horizontol view range of the street view image. Can be integars in [10, 360]. (default=360)

    Exports:
        Image file will be saved to ./street_image/{location}.jpg
    """
    url = f'http://api.map.baidu.com/panorama/v2?ak={ak}&width={width}&height={height}&location={location}&fov={fov}'
    response = requests.get(url)
    os.makedirs('street_image/', exist_ok=True)
    with open(f'./street_image/{location}.jpg', mode='wb') as im:
        im.write(response.content)
