from core import test

if __name__ == '__main__':
    ocr=test.OCR()
    img="D:/codes/DLL/testimg/wytest_2anq.bmp"
    
    print('result:', ocr.getOCR("wangyi",img))