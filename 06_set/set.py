#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-11
# @copyright by hoojo @2018
# @changelog inner scope variable assignments


# ===============================================================================
# 标题：inner scope variable assignments
# ===============================================================================
# 使用： {% set key, value = {'key': 2334} %}
# -------------------------------------------------------------------------------
# 描述： 可以在部分流程语句或模板中定义局部的变量进行引用使用
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 声明简单的变量进行使用
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
template = env.get_template('set-template.html')

# 渲染模板
result = template.render(seq = ['foo', 'bar'], items = ['foo', None, 235], message = "is a message text")

print(result)