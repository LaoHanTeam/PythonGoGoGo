from pymouse import PyMouse

'''
windows 下需要安装
    python for windows extensions http://sourceforge.net/projects/pywin32/files/
    pyhook  http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
    pymouse
    注意选取的版本需要和安装的python的版本一致
'''

x = 100
y = 100

m = PyMouse()
m.position() # 获取当前坐标的位置
m.move(x,y) # 移动鼠标到x ， y 位置
m.click(x,y) # 移动并在x y 位置处点击
m.click(x,y,1|2) # 移动并且在xy 位置点击，左右键点击
