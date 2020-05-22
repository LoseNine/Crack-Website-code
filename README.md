# WEIBO-OCR
新浪微博的验证码识别（样本1万），训练模型ResNet_LSTM_CTC

识别微博验证码，分辨率100x40
![](https://github.com/LoseNine/WEIBO-OCR/blob/master/wbtest_2bc2w.png)

识别网易验证码，分辨率80x26
![](https://github.com/LoseNine/WEIBO-OCR/blob/master/wytest_2anq.bmp)
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

