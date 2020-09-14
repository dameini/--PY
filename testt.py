import os
import numpy as np
import cv2.cv2 as cv
from matplotlib import pyplot as plt
import heapq
import math
import re


def thresh_binary(img):
    # 二值化处理
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (9, 9), 0)
    (ret3, th3) = cv.threshold(blur, 50, 255, cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    opening = cv.morphologyEx(th3, cv.MORPH_OPEN, kernel)
    return opening


def Judge(shuzu, Base):
    n = 0
    for j in range(len(shuzu)):
        if shuzu[j] > Base:
            n += 1
    if n > 0:
        return True
    else:
        return False


FilePath = 'E://Project//TestPy//Photo//卜商帖//lie//'
FileList = os.listdir(FilePath)
for lieTemp in range(len(FileList)):
    liePhotoPath = FilePath +"//" + FileList[lieTemp]
    Photo = cv.imdecode(np.fromfile(liePhotoPath, dtype=np.uint8), cv.IMREAD_UNCHANGED)
    ErZhiImg = thresh_binary(Photo)
    listt = []
    row, col = ErZhiImg.shape

    for BlackTemp in range(row):
        listt.append((ErZhiImg[BlackTemp, :] < 250).sum())
        if listt[-1]< 10:
            listt[-1] = 0
    No1 = []
    No2 = []
    maxValue = max(listt) # 数组中最大值
    np_list = np.array(listt)  # 将列表list或元组tuple转换为 ndarray 数组
    minValue = np.min(np_list[np.nonzero(np_list)])

    i = int(0)
    index = 0
    while i < row - 1:
        # i = int(i)
        if minValue + 10 < np_list[i] < maxValue:
            no1 = i
            for j in range(row)[i + 100:]:
                if maxValue - 20 < np_list[j]:
                    derta = j
                    NextHang = []
                    if derta > row - 21:
                        derta = row - 21
                    for derta in range(derta + 20)[derta:]:
                            NextHang.append(np_list[derta])
                    Flag = Judge(NextHang, maxValue - 5) # 每一行黑色点数量大于Base，则Flag = True
                    if Flag:
                        no2 = j + 30
                        no1 = i - 0
                        No1.append(no1)
                        No2.append(no2)
                        hangPhotoPath = "E://Project//TestPy//hang//"
                        roww, coll = ErZhiImg[int(No1[index]): int(No2[index]), :].shape
                        if (cv.countNonZero(ErZhiImg[int(No1[index]): int(No2[index]), :]) / (coll * roww)) < 0.035:
                            i = j
                            index = index + 1
                            break
                        else:
                            cv.imencode('.jpg', Photo[int(No1[index]): int(No2[index]), :].copy())[1].tofile(
                                hangPhotoPath + ''.join(re.findall(r'[\u4e00-\u9fa5]', liePhotoPath)) + "-" + str(
                                    index + 1) + "-" + str(no1) + "-" + str(no2) + "hang.jpg")
                            # re.findall(r'[\u4e00-\u9fa5]', liePhotoPath)
                            index = index + 1
                            print(hangPhotoPath + str(lieTemp) + "-" + str(index + 1) + "-" + str(no1) + "-" + str(
                                no2) + "hang.jpg")
                            i = j
                            break
                    else:
                        break
        i += 1
