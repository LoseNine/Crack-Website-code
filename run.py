from core import test

if __name__ == '__main__':
    ocr=test.OCR()
    print('result:', ocr.getOCR("D:/codes/DLL/dat/wy.dat", "D:/codes/DLL/wytest_2anq.bmp"))