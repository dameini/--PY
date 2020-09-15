import os
import re
import shutil
import re
import cv2.cv2 as cv
import numpy as np

if __name__ == '__main__':
    FilePath = "E://Project//TestPy//Photo//"
    WenjianjiaList = os.listdir(FilePath)
    # print(WenjianjiaList)
    print(len(WenjianjiaList))
    sum = 0
    for WenjianjiaTemp in range(len(WenjianjiaList)):
        PhotoList = FilePath + WenjianjiaList[WenjianjiaTemp] + "//hang//"
        print(FilePath + WenjianjiaList[WenjianjiaTemp] + "//QieGe")
        try:
            os.makedirs(FilePath + WenjianjiaList[WenjianjiaTemp] + "//QieGe//")
        except BaseException as msg:
            pass
        # print(PhotoList)
        Photo = os.listdir(PhotoList)
        temp = 0
        for PhotoTemp in range(len(Photo)):
            # print(Photo[PhotoTemp])
            # totalCount = re.sub("\D", "", Photo[PhotoTemp])
            # print(totalCount)
            temp += 1
        #     shutil.copyfile(PhotoList + totalCount + ".jpg", FilePath + WenjianjiaList[WenjianjiaTemp] + "//QieGe//" + str(temp) + ".jpg")
        #     try:
        #         # os.rename(PhotoList + Photo[PhotoTemp], PhotoList + totalCount + ".jpg")
        #         print(PhotoList + str(temp) + ".jpg")
        #     except BaseException as msg:
        #         print(PhotoList + Photo[PhotoTemp])
        #     # print(PhotoList + totalCount + ".jpg")
        #     # try:
        #         im1 = cv.imdecode(np.fromfile( FilePath + WenjianjiaList[WenjianjiaTemp] + "//QieGe//" + str(temp) + ".jpg", dtype=np.uint8), cv.IMREAD_UNCHANGED)
        #         im2 = cv.resize(im1, (512, 512), )  # 为图片重新指定尺寸
        #         cv.imencode('.jpg', im2[:, :].copy())[1].tofile( FilePath + WenjianjiaList[WenjianjiaTemp] + "//QieGe//" + str(temp) + ".jpg")
        #     except BaseException as msg:
        #         print( FilePath + WenjianjiaList[WenjianjiaTemp] + "//QieGe//" + str(temp) + ".jpg")
        # print(WenjianjiaList[WenjianjiaTemp] + str(WenjianjiaTemp) + "over")
        sum = sum + temp
    print(sum)
