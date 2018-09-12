#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-11
# @copyright by hoojo @2018
# @changelog if process tests statement


# ===============================================================================
# 标题：tests if process statement
# ===============================================================================
# 使用：{% if var is defined %}
# -------------------------------------------------------------------------------
# 描述：测试过滤器用于在 if 流程语句中作为判断的条件依据
# http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-tests
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 测试过滤器
# -------------------------------------------------------------------------------
from jinja2 import Environment, select_autoescape, FileSystemLoader
import math

# 从指定位置加载模板的环境
loader = FileSystemLoader('.')
# 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api
env = Environment(loader=loader,
                  autoescape=select_autoescape(['html', 'xml']),
                  line_statement_prefix="#",
                  line_comment_prefix="##",
                  trim_blocks=True, keep_trailing_newline=True, lstrip_blocks=True)


# 自定义测试器
# -------------------------------------------------------------------------------
def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

# 设置过滤器
# -------------------------------------------------------------------------------
env.tests['prime'] = is_prime



# 获取模板
template = env.get_template('tester-template.html')


class User():
    name = "hoojo"
    age = 23
    __flag = 0

# 渲染模板
result = template.render(user = User(), users = [ User(), User() ])

print(result)