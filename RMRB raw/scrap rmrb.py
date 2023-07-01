# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:41:25 2020

@author: dingq
"""


import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np

#import sys
#print(sys.path)

path = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete\2007_2012'
os.chdir (path)

driver = webdriver.Chrome()

driver.get("http://eproxy2.lib.tsinghua.edu.cn")
# 2016311445
# Wsa545397916


page_link = driver.find_element_by_xpath("/html/body/div/div")

page_link = page_link.find_element_by_xpath("//div[@id = 'container']")


