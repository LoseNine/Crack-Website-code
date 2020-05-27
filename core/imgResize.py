from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

#知乎验证码格式化
def reSize(path,width=150,height=60):
    #print('重置大小与清晰度:{}.....'.format(path))
    im=Image.open(path)
    out=im.resize((width,height),Image.ANTIALIAS)#知乎图片150x60
    out.save(os.path.join(path,path))
    return path