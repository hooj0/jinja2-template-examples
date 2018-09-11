#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-11
# @copyright by hoojo @2018
# @changelog jinja allows basic expressions everywhere


# ===============================================================================
# 标题：template expression
# ===============================================================================
# 使用：
# -------------------------------------------------------------------------------
# 描述：表达式运算，变量声明表达式、数学运算表达式、逻辑运算表达式、IF 表达式、其他表达式
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
#
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
template = env.get_template('expression-template.html')

# 渲染模板
# 默认情况下，包含的模板可以访问活动上下文的变量
result = template.render(var = "context data", boxes = ["foo", "bar"])

print(result)