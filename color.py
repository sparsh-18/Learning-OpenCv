#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:51:13 2021

@author: sparsh
"""

import cv2
def nothing(x):
   pass

cv2.namedWindow('image')
cv2.resizeWindow('image',640,200)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.waitKey(0)