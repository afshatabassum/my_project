# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:56:48 2018

@author: Afsha
"""

import pandas as pd
dat = pd.read_csv('data/gapminder_gdp_europe.csv')
oceania = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country')
