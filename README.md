## Gooey实战 | 几行代码转换Python程序为图形界面应用！



### 1.概述

今天发现公众号的一个作者大大用Python写了个小工具, 发现还挺好玩, 而且代码已经分享给大家了。在文章末尾提到还没有为这段代码制作一个`可视化界面`。同时，我还希望大家可以`将程序打包`，到时候直接发给其他人，就可以直接使用了。

如果有哪位朋友，愿意开发自己的一个小工具，可以拿着这段代码去修改。哈哈, 我就喜欢改别人的代码, 而且还有赠书活动, 于是, 话不多说, 直接开干!

我要用到一个第三方包可以一行代码将Python程序转换为图形界面应用。加上装饰器函数就可以了, 添加几个参数就可以了。



### 2.Gooey介绍

[Gooey Github地址]([chriskiehl/Gooey: Turn (almost) any Python command line program into a full GUI application with one line (github.com)](https://github.com/chriskiehl/Gooey))

[一行代码将Python程序转换为图形界面应用](https://zhuanlan.zhihu.com/p/352100156)

Gooey 是一个 Python GUI 程序开发框架，基于 wxPython GUI 库，其使用方法类似于 Python 内置 CLI 开发库 argparse，用一行代码即可快速将控制台程序转换为GUI应用程序。

#### 2.1安装方式

```python
pip install Gooey
```

#### 2.2简单示例

```python
from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description="My GUI Program!")
	parser.add_argument('Filename', widget="FileChooser")      # 文件选择框
	parser.add_argument('Date', widget="DateChooser")          # 日期选择框
	args = parser.parse_args()                                 # 接收界面传递的参数
	print(args)

if   __name__ == '__main__':
    main()
```

#### 2.3基本组件

上面已经看到了两个简单的控件：`FileChooser`和 `DateChooser·`，分别提供了一个“`文件选择器`”和 “`日期选择器`”。现在支持的 chooser 类控件有：

|      控件名      |  控件类型  |
| :--------------: | :--------: |
|   FileChooser    | 文件选择器 |
| MultiFileChooser | 文件多选器 |
|    DirChooser    | 目录选择器 |
| MultiDirChooser  | 目录多选器 |
|    FileSaver     |  文件保存  |
|   DateChooser    |  日期选择  |
|    TextField     | 文本输入框 |
|     Dropdown     |  下拉列表  |
|     CheckBox     |   复选框   |
|    RadioGroup    |   单选框   |

#### 2.4全局配置

配置参数主要是对Gooey界面做全局配置，配置方法如下：

```python
@Gooey(program_name='Demo')
def function():
    pass
```

和program_name参数配置一样，Gooey 还支持很多其它配置，下面是它支持的参数列表：

|        参数         |   类型    |                             简介                             |
| :-----------------: | :-------: | :----------------------------------------------------------: |
|      advanced       |  Boolean  |              切换显示全部设置还是仅仅是简化版本              |
|     show_config     |  Boolean  |                  跳过所有配置并立即运行程序                  |
|      language       |    str    |          指定从 gooey/languages 目录读取哪个语言包           |
|    program_name     |    str    |         GUI 窗口显示的程序名。默认会显 sys.argv[0]。         |
| program_description |    str    | Settings 窗口顶栏显示的描述性文字。默认值从 ArgumentParser 中获取。 |
|    default_size     | (600,400) |                        窗口默认大小。                        |
|    required_cols    |     1     |                      设置必选参数行数。                      |
|    optional_cols    |     2     |                      设置可选参数行数。                      |
|  dump_build_config  |  Boolean  |        将设置以 JSON 格式保存在硬盘中以供编辑/重用。         |
|  richtext_controls  |  Boolean  | 打开/关闭控制台对终端控制序列的支持（对字体粗细和颜色的有限支持） |



### 3.程序改造

在原来程序的基础上, 将需要输入的路径信息封装成一个函数``start()``, 在函数上加上我们的装饰器@Gooey()

函数主体里边添加一个``path``的参数, 在界面上通过**文件夹选择器组件**进行目录选择, 就完成了我们的程序GUI改造

```python
from gooey import Gooey, GooeyParser

# encoding:指定编码方式 program_name:程序名称 language:语言(默认英语)
# 作为一个装饰器添加在函数的前面(核心)
@Gooey(encoding='utf-8', program_name="整理文件小工具-V1.0.0", language='chinese')
def start():
    parser = GooeyParser()
    # "path": 要传递的参数变量 help:提示信息 widget:控件类型(这里使用的是文件夹选择器)
    parser.add_argument("path", help="请选择要整理的文件路径：", widget="DirChooser")  # 一定要用双引号 不然没有这个属性
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = start()
    # 解析传递回来的参数变量
    path = args.path
    # 使用参数变量
    print(path)
```



### 4.打包为exe

打包的时候, 就用我们最常用的``pyinstaller``吧

```python
# 安装
pip install pyinstaller

# 打包时执行命令 (其中F为大写，w为小写)
pyinstaller -F 文件自动归类.py -w
```



