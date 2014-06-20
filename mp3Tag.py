import os # 导入os 模块，提供文件路径，列出文件等方法
import sys # 导入sys模块，使用sys.modules 获取模块中的所有内容，提供类似反射的功能
from UserDict import UserDict

def stripnulls(data):
    "一个空字符串的处理函数"
    return data.replace("\00","").strip()

class FileInfo(UserDict):
    '''文件基类，存储文件的文件名，继承自UserDict'''
    def __init__(self,filename=None):
        UserDict.__init__(self)
        self["name"] = filename

class MP3FileInfo(FileInfo):
    "MP3文件信息类"

    tagDataMap = {
        "title":(3,33,stripnulls),
        "artist":(33,63,stripnulls),
        "album":(63,93,stripnulls),
        "year":(93,97,stripnulls),
        "comment":(97,126,stripnulls),
        "genre":(127,128,ord)
        }

    def __parse(self,filename):
        self.clear()
        try:
            #设置文件读取的指针位置，seek第二个参数2表示从文件结尾作为参考点
            fsock = open(filename,"rb",0)
            try:
                fsock.seek(-128,2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":
                #循环取出Tag信息位置信息
                for tag,(start,end,parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError: #如果出现IOError ， 则跳过继续
            pass


    def __setitem__(self,key,item):
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self,key,item)

def listDirectory(directory,fileExtList):
    
    "获取directory目录下所有满足fileExtList格式的文件"
    print directory
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory,f) for f in fileList  if os.path.splitext(f)[1] in fileExtList]
    def getFileInfoClass(filename , module=sys.modules[FileInfo.__module__]):
        "定义一个函数，获取文件信息"
        subclass = "%sFileInfo" %os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module,subclass) and getattr(module,subclass) or FileInfo

    return [getFileInfoClass(f)(f) for f in fileList]

if __name__ == "__main__":  #main 函数
    for info in listDirectory("C:\\Users\ledkk\Music", [".mp3"]):
        print "\n".join(["%s=%s" % (v,k) for v , k in info.items()])
        print
        
