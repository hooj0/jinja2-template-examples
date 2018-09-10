#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog process struct statement if


# ===============================================================================
# 标题：process struct statement if
# ===============================================================================
# 使用：if 进行逻辑运算判断
# -------------------------------------------------------------------------------
# 描述：通过判断进入不同的业务逻辑结构
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 判断语句
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
template = env.get_template('if-template.html')

# 渲染模板
result = template.render(users = [{ "username": "jack" }, { "username": "老张", "hidden": True }, { "username": "tom 'kid <jim> ", "hidden": False }],
                         kenny = { "dead": "yes" })

print(result)