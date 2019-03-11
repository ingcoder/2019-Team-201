#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 05:00:26 2019

@author: tstone
"""
import matplotlib.pyplot as plt

import datetime
import os

import numpy as np
import pandas as pd

# for accessing UNIDATA THREDD servers
#This is not a default package, use pip to install siphon and pvlib
from siphon.catalog import TDSCatalog 
from siphon.ncss import NCSS


import pvlib
from pvlib.forecast import GFS, HRRR_ESRL, NAM, NDFD, HRRR, RAP

# Choose a location based on coordinates 
# Tucson, AZ
latitude = 32.7157
longitude = 117.1611
tz = 'US/Pacific'

start = pd.Timestamp(datetime.date.today(), tz=tz) # today's date
end = start + pd.Timedelta(days=30) # 7 days from today
print(start, end)

# GFS model, defaults to 0.5 degree resolution
model_gfs = GFS()

# retrieve data for gfs
gfs_data = model_gfs.get_data(latitude, longitude, start, end)