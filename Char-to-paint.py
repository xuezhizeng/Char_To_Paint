#_*_encoding:utf-8 _*_
"""
@Software: PyCharm
@Python: 3.X   X==5
@Time: 2017.8.22
@Contact:520@skyne.cn
@Author: SKYNE
"""
"""导入所需的第三库"""
from PIL import Image
from termcolor import *
from random import choice

 ### char :"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ascii_char = list("$@%8&#*oahkbdpqwmzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")   ###字符列表

"""定义图片像素RGB值与字符的对应关系"""
def get_char(r,g,b,alpha = 256):
    if alpha == 0:              ###图片区域为白色时，返回空白
        return ' '
    length = len(ascii_char)
    gary = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gary/unit)]
### 随机转化字符颜色
def Print_color(char):
    Color_term = ['grey','red','green','yellow','blue','magenta','cyan','white']
    Color = colored(char , choice(Color_term))
    return Color

def run():
    im = Image.open('test.png')
    im = im.resize((64,64),Image.NEAREST)     ####重置图片大小，过大屏幕显示不全
    txt = " "
    for i in range(64):
        for j in range(64):
            txt += Print_color(get_char ( *im.getpixel ( (j, i) ) ))
            ### im.getpixel可以获取对应j，i处的元组类型的RGB值，*代表解开元组。
        txt += '\n'

    print(txt)
    ### 因为转换为彩色字符了，保存下来的都是一系列的字符串，不再具有字符画的样子了。故不作保存。
    #if txt :
        #with open("output.txt",'w') as f:
            #f.write(txt)

if __name__ == '__main__':
    run()



"""
#### 下面是实验楼上的源代码，有兴趣可以自己看看 ####
from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
"""