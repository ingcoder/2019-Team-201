#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 05:00:26 2019

@author: tstone
"""
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import pvlib
from pvlib.forecast import GFS #, HRRR_ESRL, NAM, NDFD, HRRR, RAP

location_path = "../streetlight_locations_datasd.csv"
sll = pd.read_csv(location_path)

# Choose a location based on coordinates 
# San Diego, CA
latitude = 32.7157
longitude = -117.1611
tz = 'US/Pacific'

#Create times to retrieve archive data
end = pd.Timestamp.today(tz=tz) 
start = end - pd.Timedelta(days=14)

# GFS model, defaults to 0.5 degree resolution
model_gfs = GFS()

# retrieve data for gfs
raw_data = model_gfs.get_data(latitude, longitude, start, end)
data = model_gfs.process_data(raw_data)

