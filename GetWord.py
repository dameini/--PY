import os
import numpy as np
import cv2.cv2 as cv
from matplotlib import pyplot as plt
import heapq
import math


def ClipPhoto(path, index, FilePath):
    Photo = cv.imread('E://Project//TestPy//ShufaTiqu//liu//1.jpg')
    # Photo = cv.imread(path)
    # img = img[:, : (img.shape[1]//2)*1]
    LeftImg = Photo[825:, : 1400]
    RightImg = Photo[:, 1650:]

    K_SuoFang = 0.4
    LeftImg = cv.resize(LeftImg, None, fx=K_SuoFang, fy=K_SuoFang, interpolation=cv.INTER_AREA)
    RightImg = cv.resize(RightImg, None, fx=K_SuoFang, fy=K_SuoFang, interpolation=cv.INTER_AREA)

    # print(LeftImg.shape)
    # print(RightImg.shape)
    # cv.imwrite(FilePath + str(index) + "L.jpg", LeftImg)
    # cv.imwrite(FilePath + str(index) + "R.jpg", RightImg)
    return LeftImg


for index in range(53):
    FilePath = "E://Project//TestPy//ShufaTiqu//liu//"
    path = FilePath + str(index + 1) + ".jpg"
    # print(path)
    # print(FilePath)
    # ClipPhoto(path,index + 1,FilePath)

    FilePath = "E://Project//TestPy//ShufaTiqu//liu2//"
    path = FilePath + str(index + 1) + ".jpg"
    # print(path)
    # print(FilePath)
    # ClipPhoto(path,index + 1,FilePath)

    FilePath = "E://Project//TestPy//ShufaTiqu//ou//"
    path = FilePath + str(index + 1) + ".jpg"
    # print(path)
    # print(FilePath)
    # ClipPhoto(path,index + 1,FilePath)

    FilePath = "E://Project//TestPy//ShufaTiqu//ou2//"
    path = FilePath + str(index + 1) + ".jpg"
    # print(path)
    # print(FilePath)
    # ClipPhoto(path,index + 1,FilePath)
    LeftImg = ClipPhoto(path,index + 1,FilePath)

    # print(index)

cv.namedWindow('LeftImg', cv.WINDOW_AUTOSIZE)
cv.imshow('LeftImg', LeftImg)
# cv.namedWindow('RightImg', cv.WINDOW_AUTOSIZE)
# cv.imshow('RightImg', RightImg)
cv.waitKey(0)
cv.destroyAllWindows()
