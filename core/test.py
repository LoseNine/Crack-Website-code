import ctypes
import os
from core import imgResize

class OCR:
    def __init__(self):
        self.dll=None
        self.path=os.getcwd()
        self.setDll()
    def setDll(self):
        #加载DLL
        self.dll=ctypes.CDLL("./dat/OCR.dll")

    def getOCR(self, mcg: str, img: str) -> str:
        """输入dat地址和图片地址
            mcg:zhihu 知乎
                wangyi 网易
                yihaodian 一号店
                weibo 微博
                na 常规英文数字

            img:图片路径
        """
        if mcg=="zhihu":
            imgResize.reSize(img,150,60)
            mcg=os.path.join(self.path,'dat/zhihu.dat')
        elif mcg=="wangyi":
            imgResize.reSize(img, 80, 26)
            mcg = os.path.join(self.path, 'dat/wy.dat')
        elif mcg == "yihaodian":
            imgResize.reSize(img, 124, 50)
            mcg = os.path.join(self.path, 'dat/yhd.dat')
        elif mcg == "weibo":
            imgResize.reSize(img, 100, 40)
            mcg = os.path.join(self.path, 'dat/weibo.dat')
        else:
            imgResize.reSize(img, 70, 20)
            mcg = os.path.join(self.path, 'dat/na.dat')

        imgPath = img.encode('utf8')
        img = ctypes.create_string_buffer(imgPath)
        mcgPath = mcg.encode('utf8')
        mcg = ctypes.create_string_buffer(mcgPath)
        result=ctypes.string_at(self.dll.getOCR(mcg, img))
        return result.decode('gb2312')

