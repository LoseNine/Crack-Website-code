from core import test

if __name__ == '__main__':
    ocr=test.OCR()
    print('result:', ocr.getOCR("D:/codes/DLL/dat/yhd.dat", "D:/codes/DLL/testimg/yhdtest_2ejm.bmp"))