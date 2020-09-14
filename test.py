import os, sys
import re
import cv2.cv2 as cv
import numpy as np
from PIL import Image


FilePath = "E://Project//TestPy//Photo//"
WenjianjiaList = os.listdir(FilePath)
# print(WenjianjiaList)
print(len(WenjianjiaList))
for WenjianjiaTemp in range(len(WenjianjiaList)):
    PhotoList = FilePath + WenjianjiaList[WenjianjiaTemp] + "//hang//"
    # print(PhotoList)
    Photo = os.listdir(PhotoList)
    for PhotoTemp in range(len(Photo)):
        # print(Photo[PhotoTemp])
        totalCount = re.sub("\D", "", Photo[PhotoTemp])
        # print(totalCount)
        # os.rename(src, dst)
        try:
            os.rename(PhotoList + Photo[PhotoTemp], PhotoList + totalCount + ".jpg")
        except BaseException as msg:
            print(PhotoList + Photo[PhotoTemp])
        # print(PhotoList + totalCount + ".jpg")
        try:
            im1 = cv.imdecode(np.fromfile(PhotoList + totalCount + ".jpg", dtype=np.uint8), cv.IMREAD_UNCHANGED)
            im2 = cv.resize(im1, (512, 512), )  # 为图片重新指定尺寸
            cv.imencode('.jpg', im2[:, :].copy())[1].tofile(PhotoList + totalCount + ".jpg")
        except BaseException as msg:
            print(PhotoList + totalCount + ".jpg")
    print(WenjianjiaList[WenjianjiaTemp] + str(WenjianjiaTemp) + "over")
    # FilePath = "E://Project//TestPy//Photo//卜商帖//hang//"
    # FileList = os.listdir(FilePath)
    # for WenjianjiaTemp in range(len(FileList)):
    #     print(FileList[WenjianjiaTemp])
    #     totalCount = re.sub("\D", "", FileList[WenjianjiaTemp])
    #     print(totalCount)
    #     # os.rename(src, dst)
    #     os.rename(FilePath + FileList[WenjianjiaTemp], FilePath + totalCount + ".jpg")
