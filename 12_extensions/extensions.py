#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-12
# @copyright by hoojo @2018
# @changelog jinja2 template extensions framework


# ===============================================================================
# 标题：template extensions framework
# ===============================================================================
# 使用：
# -------------------------------------------------------------------------------
# 描述：扩展应用框架，一些额外的扩展功能：如国际化i18n、表达式语句、语句块、循环控制等
# 扩展开启设置：http://jinja.pocoo.org/docs/2.10/extensions/#jinja-extensions
# 扩展应用实例：http://jinja.pocoo.org/docs/2.10/templates/#extensions
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 扩展应用框架的应用
# -------------------------------------------------------------------------------
from jinja2 import Environment, select_autoescape, FileSystemLoader

# 从指定位置加载模板的环境
loader = FileSystemLoader('.')
# 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api

# 设置扩展
# 导入扩展:
# 通过启用ext.i18n.trimmed 策略，可以自动修剪换行符和周围空白
extensions = ['jinja2.ext.do', 'jinja2.ext.loopcontrols', ]

env = Environment(loader=loader,
                  autoescape=select_autoescape(['html', 'xml']),
                  extensions=extensions,
                  line_statement_prefix="#",
                  line_comment_prefix="##",
                  trim_blocks=True, keep_trailing_newline=True, lstrip_blocks=True)

# 获取模板
template = env.get_template('extensions-template.html')


class User():
    name = "hoojo"
    age = 23
    __flag = 0

# 渲染模板
result = template.render(user = User(), users = [ User(), User() ])

print(result)