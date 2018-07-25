oldFileName=input("please input the old file name:")
oldFile=open(oldFileName,'r')

if oldFile:
    fileFlagNum =oldFileName.rfind('.')
    if fileFlagNum > 0:
        fileFlag= oldFileName[fileFlagNum:]

    newFileName=oldFileName[:fileFlagNum]+'[copyfile]'+fileFlag

    newFile=open(newFileName, 'w')

    for linecontent in oldFile.readline():
        newFile.write(linecontent)

    oldFile.close()
    newFile.close()