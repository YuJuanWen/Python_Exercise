'''
import os

funFlag = 1  # 1表示添加标志  2表示删除标志

folderName = './renameDir/'

# 获取指定路径的所有文件名字
dirList = os.listdir(folderName)

# 遍历输出所有文件名字
for name in dirList:
    print
    name

    if funFlag == 1:
        newName = '[东哥出品]-' + name
    elif funFlag == 2:
        num = len('[东哥出品]-')
        newName = name[num:]
    print
    newName

    os.rename(folderName + name, folderName + newName)
'''
