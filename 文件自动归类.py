# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  递归文件.py
# 日期时间：2021/8/11，17:46
import os
import glob
import shutil
from gooey import Gooey, GooeyParser

path = 'C:\\Users\\cuite\\Desktop\\test\\待整理文件夹\\folder'
# 定义一个文件字典，不同的文件类型，属于不同的文件夹，一共9个大类。
file_suffix_dict = {
    '图片': ['jpg', 'png', 'gif', 'webp'],
    '视频': ['rmvb', 'mp4', 'avi', 'mkv', 'flv'],
    "音频": ['cd', 'wave', 'aiff', 'mpeg', 'mp3', 'mpeg-4'],
    '文档': ['xls', 'xlsx', 'csv', 'doc', 'docx', 'ppt', 'pptx', 'pdf', 'txt'],
    '压缩文件': ['7z', 'ace', 'bz', 'jar', 'rar', 'tar', 'zip', 'gz'],
    '常用格式': ['json', 'xml', 'md', 'xmimd'],
    '程序脚本': ['py', 'java', 'html', 'sql', 'r', 'css', 'cpp', 'c', 'sas', 'js', 'go'],
    '可执行程序': ['exe', 'bat', 'lnk', 'sys', 'com'],
    '字体文件': ['eot', 'otf', 'fon', 'font', 'ttf', 'ttc', 'woff', 'woff2']
}


# 定义一个函数，传入每个文件对应的后缀。判断文件是否存在于字典file_dict中；
# 如果存在，返回对应的文件夹名；如果不存在，将该文件夹命名为"未知分类"；
def func(suffix):
    for name, type_list in file_suffix_dict.items():
        if suffix.lower() in type_list:
            return name
    return "未知分类"


# for curDir, dirs, files in os.walk(path):
#     for file in files:
#         filename_suffix = file.split(".")[-1]
#         file_type = func(filename_suffix)
#         file_type_folder = os.path.join(path, file_type)
#         # 根据每个文件分类，创建各自对应的文件夹。
#         if not os.path.exists(file_type_folder):
#             os.mkdir(file_type_folder)
#         # 移动文件
#         shutil.move(os.path.join(curDir, file), os.path.join(curDir, file_type_folder))


for file_path in glob.glob(f"{path}/**", recursive=False):
    if not os.path.isdir(file_path):
        # print(file_path)
        filename = os.path.basename(file_path)
        filename_suffix = filename.split(".")[-1]
        file_type = func(filename_suffix)
        file_type_folder = os.path.join(path, file_type)
        # 根据每个文件分类，创建各自对应的文件夹。
        if not os.path.exists(file_type_folder):
            os.mkdir(file_type_folder)
        try:
            if os.path.exists(os.path.join(file_type_folder, filename)):
                print("<%s> 在 '%s' 目录中已经存在!" % (filename, file_type_folder))
            else:
                # 移动文件
                shutil.move(file_path, file_type_folder)
        except Exception as e:
            print(e)
print("整理完成!")
