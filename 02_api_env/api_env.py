#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog API basic env context used


# ===============================================================================
# 标题：API basic env context
# ===============================================================================
# 使用：模板引擎的环境变量和上下文使用
# -------------------------------------------------------------------------------
# 描述：环境和上下文能使得不同的文件之间共享一些相同的数据
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 模板的中心对象Environment。此类的实例用于存储配置和全局对象，并用于从文件系统或其他位置加载模板。
# -------------------------------------------------------------------------------

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

# 从指定位置加载模板的环境
# loader = PackageLoader('commons', 'templates')
loader = FileSystemLoader('templates')
env = Environment(loader=loader, autoescape=select_autoescape(['html', 'xml']))


# 获取模板
template = env.get_template('my-template.html')

# 渲染模板
result = template.render(title = "Template Env", content = "template env used")

print('template result: ', result)