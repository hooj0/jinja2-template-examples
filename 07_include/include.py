#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-11
# @copyright by hoojo @2018
# @changelog include template file content to this file


# ===============================================================================
# 标题：include external files
# ===============================================================================
# 使用：{% include 'header.html' %}
# -------------------------------------------------------------------------------
# 描述：导入外部文件内容到当前文件，可以重复利用，将固定重复的内容定义为单独的文件进行复用
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 复用外部文件
# -------------------------------------------------------------------------------
from jinja2 import Environment, select_autoescape, FileSystemLoader

# 从指定位置加载模板的环境
loader = FileSystemLoader('.')

# 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api
env = Environment(loader=loader,
                  autoescape=select_autoescape(['html', 'xml']),
                  line_statement_prefix="#",
                  line_comment_prefix="##",
                  trim_blocks=True, keep_trailing_newline=True, lstrip_blocks=True)


# 获取模板
template = env.get_template('body-template.html')

# 渲染模板
# 默认情况下，包含的模板可以访问活动上下文的变量
result = template.render(var = "context data")

print(result)