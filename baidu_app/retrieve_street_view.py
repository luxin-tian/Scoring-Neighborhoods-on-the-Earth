from baidu_app.baidu_api_request import get_street_view
from baidu_app.coordinate_generator import coordinate_generator


def main(
    a,
    b,
    c,
    d,
    lat_resolution,
    lon_resolution,
    ak,
    width=1024,
    height=512,
        fov=360):
    """Retrive the street view images within a specific area from Baiud Map.

    Args:
        a (str, float): lower bound of latitude
        b (str, float): upper bound of latitude
        c (str, float): lower bound of longitude
        d (str, float): upper bound of longitude
        lat_resolution (int): the difference between the latitudes of two coordinates.
        lon_resolution (int): the difference between the longitudes of two coordinates.
        ak (str): Baidu developer API ak token.
        width (int): the width of the street view image. (default=1024)
        height (int): the height of the street view image. (default=512)
        fov (int): the horizontol view range of the street view image. Can be integars in [10, 360]. (default=360)

    Exports:
        Image files will be saved to ./street_image/
    """
    gen = coordinate_generator(a, b, c, d, lat_resolution, lon_resolution)

    while True:
        try:
            get_street_view(ak, next(gen), width=1024, height=512, fov=180)
        except StopIteration:
            break


if __name__ == '__main__':
    main(input('lower bound of latitude: '),
         input('upper bound of latitude: '),
         input('lower bound of longitude: '),
         input('upper bound of longitude: '),
         int(input('lat_resolution: ')),
         int(input('lon_resolution: ')),
         input('ak: '))
