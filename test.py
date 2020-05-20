import ctypes
class OCR:
    def __init__(self):
        self.dll=None
        self.setDll()
    def setDll(self):
        #加载DLL
        self.dll=ctypes.CDLL("./OCR.dll")
    def getOCR(self,mcg,img):
        #输入dat地址和图片地址
        imgPath = img.encode('utf8')
        img = ctypes.create_string_buffer(imgPath)

        mcgPath = mcg.encode('utf8')
        mcg = ctypes.create_string_buffer(mcgPath)
        result=ctypes.string_at(self.dll.getOCR(mcg, img))
        return result.decode('gb2312')

if __name__ == '__main__':
    c=OCR()
    print('result:',c.getOCR("D:/codes/DLL/dat/wy.dat","D:/codes/DLL/wytest_2anq.bmp"))