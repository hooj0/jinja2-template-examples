#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog process struct statement for loop


# ===============================================================================
# 标题：process struct statement for loop
# ===============================================================================
# 使用：for 循环流程语句，控制模板的结构流程
# -------------------------------------------------------------------------------
# 描述：使用循环做一些流程化的控制
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 循环模板
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
template = env.get_template('for-template.html')

user = [
    {"username": "jack"},
    {"username": "老张", "hidden": True},
    {"username": "tom 'kid <jim> ", "hidden": False}
]

sitemap = [
    {"item": "foo", "href": "foo/a.htm"},
    {
        "item": "bar", "href": "bar/a.htm",
        "children": [{ "item": "bar-1", "href": "bar-1/a.htm"}]
    }
]

# 渲染模板
result = template.render(users = user,
                         my_dict = dict(name = 'tom', age = 22, address = 'china'),
                         my_dict2 = { 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) },
                         rows = [ "a", "b", "c", "c" ],
                         sitemap = sitemap
                         )

print(result)