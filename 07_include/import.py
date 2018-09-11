#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-11
# @copyright by hoojo @2018
# @changelog import template file macro to this template use


# ===============================================================================
# 标题：import external files macro
# ===============================================================================
# 使用：{% import 'forms.html' as forms %}
# -------------------------------------------------------------------------------
# 描述：导入外部文件中的 宏（函数） 到当前模板中，然后在模板中使用外部文件的宏。外部文件宏不能使用
# 当前模板上下文的局部变量，但可以使用全局的变量
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 导入外部文件宏进行复用
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
template = env.get_template('import-template.html')

# 渲染模板
# 默认情况下，包含的模板可以访问活动上下文的变量
result = template.render(var = "context data", boxes = ["foo", "bar"])

print(result)