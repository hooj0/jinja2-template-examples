#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog process struct statement macro code block


# ===============================================================================
# 标题：process struct statement macro code block
# ===============================================================================
# 使用：macro 宏，一直类似自定义函数的代码段
#   # macro func(a, b, c)
#        do something
#   # endmacro
# -------------------------------------------------------------------------------
# 描述：macro 宏 可以重复使用，定义一段代码块进行执行，相当于自定义的函数
# -------------------------------------------------------------------------------
# 参考：http://jinja.pocoo.org/docs/2.10/templates/#template-inheritance
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 宏 代码方法使用
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
template = env.get_template('macro-template.html')

# 渲染模板
result = template.render(users = [{ "username": "jack" }, { "username": "老张", "hidden": True }, { "username": "tom 'kid <jim> ", "hidden": False }],
                         kenny = { "dead": "yes" },
                         list_of_user = [ { "username": "jack", "realname": "杰克" }, { "username": "老张", "realname": "laozhang", "hidden": True } ])

print(result)