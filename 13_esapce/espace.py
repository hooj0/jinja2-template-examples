#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-12
# @copyright by hoojo @2018
# @changelog template output auto esapce


# ===============================================================================
# 标题：template output auto esapce
# ===============================================================================
# 使用：{% autoescape false %}
# -------------------------------------------------------------------------------
# 描述：模板输出自动转义，在一段代码块中开启或关闭转义，避免频繁使用内置过滤器做转义处理
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 转义标签的使用
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
template = env.get_template('espace-template.html')

class User():
    name = "hoojo"
    age = 23
    __flag = 0

# 渲染模板
result = template.render(user = User(), users = [ User(), User() ])

print(result)