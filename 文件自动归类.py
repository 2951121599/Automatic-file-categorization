# -*-coding:utf-8-*- 
# 作者：   Taylor
# 文件名:  文件自动归类.py
# 日期时间：2021/8/11，19:50
import os
import glob
import shutil
from gooey import Gooey, GooeyParser

# 定义一个文件字典，不同的文件类型，属于不同的文件夹，一共9个大类。
file_suffix_dict = {
    '图片': ['jpg', 'png', 'jpeg', 'gif', 'webp'],
    '视频': ['mp4', 'avi', 'mkv', 'flv', 'ts'],
    "音频": ['wave', 'aiff', 'mpeg', 'mp3'],
    '文档': ['xls', 'xlsx', 'csv', 'doc', 'docx', 'ppt', 'pptx', 'pdf', 'txt'],
    '压缩文件': ['7z', 'rar', 'zip'],
    '常用格式': ['json', 'xml', 'md', 'xmimd'],
    '程序脚本': ['py', 'java', 'html', 'sql', 'r', 'cpp', 'c', 'js', 'go'],
    '可执行程序': ['exe', 'bat', 'lnk'],
}


def get_file_type(suffix):
    """
    传入每个文件对应的后缀。判断文件是否存在于字典file_dict中
    如果存在，返回对应的文件夹名
    如果不存在，将该文件夹命名为"未知分类"
    :param suffix: 传入每个文件对应的后缀
    :return: 返回文件属于的类型
    """
    for file_type_name, file_type_list in file_suffix_dict.items():
        if suffix.lower() in file_type_list:
            return file_type_name
    return "未知分类"


@Gooey(encoding='utf-8', program_name="整理文件小工具-V1.0.0 - Taylor", language='chinese')
def start():
    parser = GooeyParser()
    parser.add_argument("path", help="请选择要整理的文件路径：", widget="DirChooser")  # 一定要用双引号 不然没有这个属性
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    var = start()
    path = var.path
    for file_path in glob.glob(f"{path}/**", recursive=False):
        if not os.path.isdir(file_path):
            filename = os.path.basename(file_path)
            filename_suffix = filename.split(".")[-1]
            file_type = get_file_type(filename_suffix)
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
