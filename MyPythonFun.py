# 导入os模块
import os

from pip import main
 
# Get_FileName_IN_Dir函数说明：
# 将path下的所有文件的文件名读入,格式为一行一个文件名，并以filelist.txt存储在path下
def Get_FileName_IN_Dir(path):  
    file_name_list = os.listdir(path)
 
    # 转为转为字符串
    file_name = str(file_name_list)
    
    # replace替换"["、"]"、" "、"'"
    file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")
    
    # 创建并打开文件list.txt
    f = open(path + "\\" + "filelist.txt", "a")
    
    # 将文件下名称写入到"文件list.txt"
    f.write(file_name)
    return file_name
