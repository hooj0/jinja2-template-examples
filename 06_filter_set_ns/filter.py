#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog jinja2 template filter execution inner func


# ===============================================================================
# 标题：template filter execution inner func
# ===============================================================================
# 使用：使用 filter 关键字，处理标签块内部中的数据
# -------------------------------------------------------------------------------
# 描述：filter 标签块允许处理内部的字符串，进行内部函数的处理
# -------------------------------------------------------------------------------
# 内置过滤器列表：http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-filters
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# filter 标签块的字符串转换演示
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
template = env.get_template('filter-template.html')

# 渲染模板
result = template.render()

print(result)