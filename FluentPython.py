#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
City = namedtuple('City', 'name country pop coord')
tokyo = City('Tokyo', 'JP', 36, (35, 139))
tokyo
tokyo.pop

City._fields
LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21, LatLong(28, 77))
delhi = City._make(delhi_data)
delhi._asdict()
for key, value in delhi._asdict().items():
    print(key + ':', value)
