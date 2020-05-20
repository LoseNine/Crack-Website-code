# WEIBO-OCR
训练模型ResNet_LSTM_CTC

1.识别微博验证码，模型weibo.dat，分辨率100x40，识别率95%
![](https://github.com/LoseNine/Decryption-Website-code/blob/master/wbtest_2bc2w.png)


2.识别网易验证码，模型wy.dat，分辨率80x26，识别率91%
![](https://github.com/LoseNine/Decryption-Website-code/blob/master/wytest_2anq.bmp)



## 开放OCR.dll方法
```
  getOCR(mcg,img)
```

## 实例
```python

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
    #返回识别结果
```

