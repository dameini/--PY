# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2.cv2 as cv
from matplotlib import pyplot as plt
import heapq
import math

# 列数
ImgCol = 3
# 行数
ImgRow = 4

# 是不是整齐
IsEquels = True


def thresh_binary(img):
    # 二值化处理
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (9, 9), 0)
    # OTSU's binaryzation
    (ret3, th3) = cv.threshold(blur, 50, 255, cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    opening = cv.morphologyEx(th3, cv.MORPH_OPEN, kernel)
    # 看看有几个非零像素
    # cv.namedWindow("Image" + str(index), 0)
    # cv.imshow("Image" + str(index), opening)
    return opening


def hist_col(img):
    # sum the black pixel numbers in each cols
    # 将每个cols中的黑色像素数相加
    listt = []
    row, col = img.shape
    for i in range(col):
        listt.append((img[:, i] < 250).sum())
    return listt


# 纵向切图的坐标
def cut_col(img, l, filename):
    minlistt = []
    No1 = []
    No2 = []
    np_list = np.array(l) # 将列表list或元组tuple转换为 ndarray 数组

    row, col = img.shape
    avg = col / (ImgCol + 1)
    if cv.countNonZero(img) < col * row / 1.5:  # 黑底子白字
        a = max(l)
        minval = np.min(np_list[np.nonzero(np_list)])

        # print(minval)
        i = 10
        index = 0

        while i < col - 11:
            if i >= col - 11:
                i = int(i)
                if minval < np_list[i] <= np_list[i + 1:col].min():
                    minlistt.append(i)
                    break
                if i == col - 1:
                    minlistt.append(i)
                    break
            else:
                i = int(i)
                if minval < np_list[i] <= a:
                # if minval < np_list[i] <= np_list[i:i + 5].min():
                    no1 = i
                    for j in range(col)[i+100:]:
                        if a-1 < np_list[j]:

                            no2 = j+10
                            print(no1, no2)
                            if no2 - no1 > 200:
                                No1.append(no1)
                                No2.append(no2)
                                print(filename)
                                cv.imwrite("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "~" + str(i) + "-" + "lie.jpg",
                                       img[:, int(No1[index]): int(No2[index])].copy())
                                index = index + 1
                                i = no2
                                break
            i += 1
        return minlistt, row
    else:  # 白底黑字
        i = 20
        a = min(l)
        while i < col - 1:
            if i >= col - 11:
                if np_list[i] < a + 10 and np_list[i] <= np_list[i + 1:col].min():
                    minlistt.append(i)
                    break
                if i == col - 1:
                    minlistt.append(i)
                    break
            else:
                i = int(i)
                if a + 5 < np_list[i] <= np_list[i:i + 5].min():
                    if len(minlistt) == 0:
                        minlistt.append(i)
                    else:
                        x = 0
                        y = 1
                        while i + x < col - 10 and np_list[i + x] <= a + 10:
                            x += 3
                        while np_list[i - y] <= a + 10:
                            y += 1
                        minlistt.append(i + x / 2 - y / 2)
                    i += avg
            i += 1
        return minlistt, row


def cut_img(img, minlist, row, filename):
    # 切竖着的图并接着处理
    colpics = []

    for j in range(len(minlist) - 1):
        # cv.namedWindow(str(j),0)
        # cv.imshow("F:\\test\\lie\\"+filename+str(j)+"lie.jpg", img[0:row, minlist[j]:minlist[j+1]])
        if minlist[j + 1] - minlist[j] >= minlist[-1] / ImgCol * 1.8:
            cha = minlist[j + 1] - minlist[j]
            chu = cha / (minlist[-1] / ImgCol * 1.0)
            ss = sishewuru(chu)
            zhong = cha / ss
            if IsEquels:
                cv.imwrite("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "lie.jpg",
                           img[:, int(minlist[j]):int(minlist[j + 1])].copy())
                print("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "lie1.jpg")
            else:
                # 处理等距字段
                for i in range(ss):
                    colpics.append(img[int(minlist[j] + i * zhong):int(minlist[j] + (i + 1) * zhong)])
                    cv.imwrite(
                        "E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "~" + str(
                            i) + "-" + "lie.jpg",
                        img[:, int(minlist[j] + i * zhong): int(minlist[j] + (i + 1) * zhong)].copy())
                    print("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "~" + str(
                        i) + "-" + "lie2.jpg")
        else:
            cv.imwrite("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "lie.jpg",
                       img[:, int(minlist[j]):int(minlist[j + 1])].copy())
            print("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + filename + "-" + str(j) + "lie3.jpg")
            colpics.append(img[:, int(minlist[j]):int(minlist[j + 1])])
    return colpics


def hist_row(img):
    # 横着的坐标算一下
    img = thresh_binary(img.copy())
    list = []
    row, col = img.shape
    for i in range(row):
        list.append((img[i, :] < 200).sum())
    return cut_row(img, list)


def sishewuru(swr):
    # 四舍五入
    if swr - int(swr) >= 0.5:
        return int(swr) + 1
    else:
        return int(swr)


def cut_row(img, row_list):
    # 定点横着的坐标
    print(row_list)

    minlist = []
    # single_images_with_rect = []
    row, col = img.shape
    np_list = np.array(row_list)

    avg = row / (ImgRow)
    i = 0
    if cv.countNonZero(img) < col * row / 2:  # 黑底子白字
        a = max(row_list)
        while i < row:
            if i >= row - 20:
                if a - 5 < np_list[i] <= np_list[i + 1:row].min():
                    minlist.append(row)
                    break
                if i == row - 1:
                    minlist.append(i)
                    break
            elif a - 3 < np_list[i] <= np_list[i:i + 15].min():
                if len(minlist) == 0:
                    minlist.append(i)
                else:
                    x = 0
                    y = 1
                    while np_list[i + x] >= a - 3 and i + x < row - 10:
                        x += 5
                    while np_list[i - y] >= a - 3:
                        y += 1
                    minlist.append(i + x / 2 - y / 2)
                i += 100
            i += 1
            i = int(i)
    else:
        a = min(row_list)
        while i < row:
            aa = np_list[i]
            if i >= row - 20:
                if a + 5 < np_list[i] <= np_list[i + 1:row].min():
                    minlist.append(row)
                    break
                if i == row - 1:
                    minlist.append(i)
                    break
            elif a + 3 < np_list[i] <= np_list[i:i + 15].min():
                if len(minlist) == 0:
                    minlist.append(i)
                else:
                    x = 0
                    y = 1
                    while np_list[i + x] <= a + 3 and i + x < row - 10:
                        x += 5
                    while np_list[i - y] <= a + 3:
                        y += 3
                    minlist.append(i + x / 2 - y / 2)
                i += avg
            i += 1
            i = int(i)

    if row - minlist[-1] > 0.4 * avg:
        minlist.append(row)
    # print(minlist)

    return minlist, col


def single_cut(img, minlist, col, name):
    # 切横着的图
    rowpics = []
    for j in range(len(minlist) - 1):
        # uu = minlist[j] if j == 0 else minlist[+20]
        if minlist[j + 1] - minlist[j] >= minlist[-1] / ImgRow * 1.8:
            cha = minlist[j + 1] - minlist[j]
            chu = cha / (minlist[-1] / ImgRow * 1.0)
            ss = int(round(chu))
            zhong = cha / ss
            if IsEquels:
                cv.imwrite("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + name + "-" + str(j) + ".jpg",
                           img[minlist[j]:minlist[j + 1], 0:col].copy())
            else:
                for i in range(ss):
                    y1 = int(minlist[j] + i * zhong)
                    if y1 < 0:
                        y1 = 0
                    y2 = int(minlist[j] + (i + 1) * zhong)
                    cv.imwrite("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + name + "-" + str(j) + "_" + str(
                        i) + ".jpg",
                               img[y1:y2, :].copy())
        else:
            y1 = int(minlist[j])
            y2 = int(minlist[j + 1])
            if y2 < 0:
                y2 = 0
            cv.imwrite("E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege//" + name + "-" + str(j) + ".jpg",
                       img[y1:y2, :].copy())


def qietu1(filestr):
    # 切二级图
    for root, dirs, files in os.walk(filestr):
        for file in files:
            filename = os.path.join(root, file)
            img1 = cv.imread(filename)
            mlis = hist_row(img1)
            single_cut(img1, mlis[0], mlis[1], file.split(".")[0])

            # row,col,_ = img.shape
            # ehight = row/imgrow
            # for i in xrange(imgrow-1):
            #     ii = img[i*ehight:(i+1)*ehight,0:col]
            #     cv.imwrite("F:\\test\\danzi\\"+file.split(".")[0]+"-"+str(i)+'.jpg', ii.copy())


def qietu(filestr):
    # 切一级图
    dir = filestr
    for root, dirs, files in os.walk(dir):
        for file in files:
            filename = os.path.join(root, file)
            print(filename)
            img = cv.imread(filename)
            # cv.namedWindow(filename,0)
            # cv.imshow(filename, img)
            a = thresh_binary(img)
            lists = hist_col(a)
            # print(lists)
            l = cut_col(a, lists,file.split(".")[0])
            if len(l[0]) < 4:
                print(filename)
                print(l[0])
            # colpics = cut_img(img, l[0], l[1], file.split(".")[0])

        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == '__main__':

    path = 'E://Project//TestPy//ShufaTiqu//liu//liuLR//qiege'
    for i in os.listdir(path):
        path_file = os.path.join(path, i) # 取文件路径
        if os.path.isfile(path_file):
            os.remove(path_file)

    qietu(r'E:/Project/TestPy/ShufaTiqu/liu/LLL')



    print("完成")
