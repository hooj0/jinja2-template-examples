#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog template extend used



# ===============================================================================
# 标题：template extend
# ===============================================================================
# 使用：在子模板文件中 {% extends "basic-template.html" %} 继承 应用模板
# -------------------------------------------------------------------------------
# 描述：模板继承，利用继承的方法定义公共的模板代码块，可以大量复用代码，降低重复工作
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 继承填充公共代码块
# -------------------------------------------------------------------------------
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

# 从指定位置加载模板的环境
loader = FileSystemLoader('.')
# 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api
env = Environment(loader=loader,
                  autoescape=select_autoescape(['html', 'xml']),
                  line_statement_prefix="#",
                  line_comment_prefix="##",)
                  # 删除换行或空白
                  ##keep_trailing_newline=True, lstrip_blocks=True, trim_blocks=True)



# 获取模板
template = env.get_template('block-template.html')

# 渲染模板
result = template.render(seq = ["foo", "bar"])

print(result)