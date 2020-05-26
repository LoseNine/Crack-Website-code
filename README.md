# CODE-OCR

识别微博验证码，分辨率100x40
![](https://github.com/LoseNine/Crack-Website-code/blob/master/testimg/wbtest_2bc2w.png)

识别网易验证码，分辨率80x26
![](https://github.com/LoseNine/Crack-Website-code/blob/master/testimg/wytest_2anq.bmp)

识别一号店验证码，分辨率124x50
![](https://github.com/LoseNine/Crack-Website-code/blob/master/testimg/yhdtest_2ejm.bmp)

识别常规英数店验证码，分辨率70x20
![](https://github.com/LoseNine/Crack-Website-code/blob/master/testimg/natest_1ACE.jpg)

## 开放OCR.dll方法
```
  getOCR(mcg,img)
```

## 实例
```python
from core import test

if __name__ == '__main__':
    ocr=test.OCR()
    print('result:', ocr.getOCR("D:/codes/DLL/dat/wy.dat", "D:/codes/DLL/wytest_2anq.bmp"))
    #返回识别结果
```

