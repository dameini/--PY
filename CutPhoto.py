import os, sys
import re
import cv2.cv2 as cv
import numpy as np


# 图像二值化
def thresh_binary(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (9, 9), 0)
    (ret3, th3) = cv.threshold(blur, 50, 255, cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    opening = cv.morphologyEx(th3, cv.MORPH_OPEN, kernel)
    return opening


# 按列切割
def cutlie_black(Path, Number, LiePath):
    Photo = cv.imdecode(np.fromfile(Path, dtype=np.uint8), cv.IMREAD_UNCHANGED)
    ErZhiImg = thresh_binary(Photo)
    row, col = ErZhiImg.shape
    listt = []
    for BlackTemp in range(col):
        listt.append((ErZhiImg[:, BlackTemp] < 250).sum())
        if listt[-1]< 10:
            listt[-1] = 0

    No1 = []
    No2 = []
    np_list = np.array(listt)  # 将列表list或元组tuple转换为 ndarray 数组

    if cv.countNonZero(ErZhiImg) < col * row / 1.5:  # 黑底子白字
        MaxValue = max(listt)
        MinValue = np.min(np_list[np.nonzero(np_list)])

        i = int(0)
        index = 0

        while i < col - 1:
            if MinValue+20 < np_list[i] <= MaxValue:
                no1 = i
                for j in range(col)[i + 100:]:
                    if MaxValue - 60 < np_list[j]:
                        no2 = j + 20
                        no1 = i
                        if no2 - no1 > 200:
                            No1.append(no1)
                            No2.append(no2)
                            # roww, coll = ErZhiImg[:, int(No1[index]): int(No2[index])].shape
                            # if cv.countNonZero(ErZhiImg[:, int(No1[index]): int(No2[index])]) < coll * roww / 1.5:  # 黑底子白字
                            cv.imencode('.jpg', Photo[:, int(No1[index]): int(No2[index])].copy())[1].tofile(
                                LiePath + Number + "-" + str(index+1) + "lie.jpg")
                            index = index + 1
                            i = j
                            break
            i += 1


# 删除文件夹下所有文件
def delete_file(path):
    list = os.listdir(path)
    for Num in range(len(list)):
        FilePath = path + "//" + list[Num]
        # print(FilePath)
        os.remove(FilePath)


# 将图像按列切割
def qiege_lie(WenJianJiaPath):
    PhotoList = os.listdir(WenJianJiaPath)
    for PhotoTemp in range(len(PhotoList)):
        if PhotoList[PhotoTemp].endswith('.jpg'):
            number = re.findall(r"\d+", PhotoList[PhotoTemp])[0]
            # print(WenJianJiaPath + PhotoList[j])
            # print(WenJianJiaPath + number + ".jpg")
            os.rename(WenJianJiaPath + PhotoList[PhotoTemp], WenJianJiaPath + number + ".jpg")
            LiePath = WenJianJiaPath + "lie//"
            # DeleteFile(LiePath)
            # LiePath = FilePath + "lie//"
            cutlie_black(WenJianJiaPath + number + ".jpg", FileList[WenjianjiaTemp] + number, LiePath)
    # print(WenJianJiaPath + str(PhotoTemp) + "按列切割成功。" + str(WenjianjiaTemp+1))


def Judge(shuzu, Base):
    n = 0
    for j in range(len(shuzu)):
        if shuzu[j] > Base:
            n += 1
    if n > 0:
        return True
    else:
        return False


# 按行切割
def qiege_hang(WenJianJiaPath):
    FilePath = WenJianJiaPath + "lie//"
    FileList = os.listdir(FilePath)
    Num = 0
    for lieTemp in range(len(FileList)):
        liePhotoPath = FilePath + FileList[lieTemp]
        Photo = cv.imdecode(np.fromfile(liePhotoPath, dtype=np.uint8), cv.IMREAD_UNCHANGED)
        ErZhiImg = thresh_binary(Photo)
        listt = []
        row, col = ErZhiImg.shape

        for BlackTemp in range(row):
            listt.append((ErZhiImg[BlackTemp, :] < 250).sum())
            if listt[-1] < 10:
                listt[-1] = 0
        No1 = []
        No2 = []
        maxValue = max(listt)  # 数组中最大值
        np_list = np.array(listt)  # 将列表list或元组tuple转换为 ndarray 数组
        minValue = np.min(np_list[np.nonzero(np_list)])

        i = int(0)
        index = 0
        while i < row - 1:
            # i = int(i)
            if minValue + 10 < np_list[i] < maxValue:
                no1 = i
                for j in range(row)[i + 100:]:
                    if maxValue - 10 < np_list[j]:
                        derta = j
                        NextHang = []
                        if derta > row - 21:
                            derta = row - 21
                        for derta in range(derta + 20)[derta:]:
                            NextHang.append(np_list[derta])
                        Flag = Judge(NextHang, maxValue - 5)  # 每一行黑色点数量大于Base，则Flag = True
                        if Flag:
                            no2 = j + 30
                            no1 = i - 0
                            No1.append(no1)
                            No2.append(no2)
                            roww, coll = ErZhiImg[int(No1[index]): int(No2[index]), :].shape
                            if (cv.countNonZero(ErZhiImg[int(No1[index]): int(No2[index]), :]) / (coll * roww)) < 0.035:
                                # 剔除全黑图片
                                i = j
                                index = index + 1
                                break
                            else:
                                cv.imencode('.jpg', Photo[int(No1[index]): int(No2[index]), :].copy())[1].tofile(
                                    WenJianJiaPath + "hang//" + ''.join(re.findall(r'[\u4e00-\u9fa5]', WenJianJiaPath)) + "-" + str(Num + 1) + ".jpg")
                                index = index + 1
                                Num = Num + 1
                                i = j
                                break
                        else:
                            break
            i += 1


# FilePath = "E://Project//TestPy//ShufaTiqu//Photo//"
if __name__ == '__main__':
    FilePath = "E://Project//TestPy//Photo//"
    FileList = os.listdir(FilePath)
    for WenjianjiaTemp in range(len(FileList)):
        WenJianJiaPath = FilePath + FileList[WenjianjiaTemp] + "//"
        try:
            os.makedirs(WenJianJiaPath + "lie")
            pass
        except BaseException as msg:
            pass
        try:
            os.makedirs(WenJianJiaPath + "hang")
            pass
        except BaseException as msg:
            pass
        LiePath = WenJianJiaPath + "lie//"
        HangPath = WenJianJiaPath + "hang//"
        delete_file(LiePath)
        delete_file(HangPath)
        qiege_lie(WenJianJiaPath)
        qiege_hang(WenJianJiaPath)
