#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog template variable used


# ===============================================================================
# 标题：template variable used
# ===============================================================================
# 使用：{{ foo.bar }} 或 {{ foo['bar'] }} 读取变量
# -------------------------------------------------------------------------------
# 描述：模板变量的使用
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 在模板中使用变量
# -------------------------------------------------------------------------------
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

# 从指定位置加载模板的环境
loader = FileSystemLoader('.')
# 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api
env = Environment(loader=loader,
                  autoescape=select_autoescape(['html', 'xml']),
                  line_statement_prefix="#",
                  line_comment_prefix="##")



# 获取模板
template = env.get_template('template.html')

# 渲染模板
result = template.render(title = "template variable used", a_variable = "this is a var", navigation = [{"href": "a/b/c.htm", "caption": "link a"}, {"href": "a/b/b.htm", "caption": "link b"}], seq = ["foo", "bar"])

print('template result: ', result)
