def coordinate_generator(a, b, c, d, lat_resolution, lon_resolution):
    """Yields the evenly distributed geographical coordinates within a square
    area.

    For example, if lat_resolution=100 and long_resolution=150, this will 
    generate 100*150 geographical coordinates. This generator yields discrete 
    geographical coordinates within a square area.

    Args:
        a (str, float): lower bound of latitude
        b (str, float): upper bound of latitude
        c (str, float): lower bound of longitude
        d (str, float): upper bound of longitude
        lat_resolution (int): the difference between the latitudes of two coordinates.
        lon_resolution (int): the difference between the longitudes of two coordinates.

    Returns:
        A geographical coordinates (str): '<longitude>, <latitude>'.
    """
    len_lat = float(b) - float(a)
    len_long = float(d) - float(c)
    for vertical in range(lat_resolution):
        for horizontal in range(lon_resolution):
            yield f'{float(c) + len_long * (horizontal/(lon_resolution-1))},{float(a) + len_lat * (vertical/(lat_resolution-1))}'
