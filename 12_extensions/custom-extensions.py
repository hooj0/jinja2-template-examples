#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-12
# @copyright by hoojo @2018
# @changelog user custom extension template


# ===============================================================================
# 标题：custom extension template
# ===============================================================================
# 使用：http://jinja.pocoo.org/docs/2.10/extensions/#example-extension
# -------------------------------------------------------------------------------
# 描述：自定义扩展，并在模板中使用
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 自定义扩展
# -------------------------------------------------------------------------------
from jinja2 import Environment, select_autoescape, FileSystemLoader
from ext.custom_ext_pygments import PygmentsExtension

# 从指定位置加载模板的环境
loader = FileSystemLoader('.')
# 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api

# 设置自定义扩展
extensions = [PygmentsExtension]

env = Environment(loader=loader,
                  autoescape=select_autoescape(['html', 'xml']),
                  extensions=extensions,
                  line_statement_prefix="#",
                  line_comment_prefix="##",
                  trim_blocks=True, keep_trailing_newline=True, lstrip_blocks=True)

# 获取模板
template = env.get_template('custom-extension-template.html')

# 渲染模板
result = template.render()

print(result)