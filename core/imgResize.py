from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

#知乎验证码格式化
def zhihu(path):
    print('重置大小与清晰度:{}.....'.format(path))
    files=os.listdir(path)
    print(files)
    for f in files:
        if f.endswith('jpg'):
            file_path = os.path.join(path, f)
            im=Image.open(file_path)
            out=im.resize((150,60),Image.ANTIALIAS)
            out.save(os.path.join(path,f))