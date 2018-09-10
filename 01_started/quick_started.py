#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog quick started use jinja2 python template framework


# ===============================================================================
# 标题：quick started use jinja2 python template framework
# ===============================================================================
# 使用：install jinja2 framework
#               pip install Jinja2
# 官方文档：http://jinja.pocoo.org/docs/2.10/intro/#basic-api-usage
# -------------------------------------------------------------------------------
# 描述：快速开始使用 jinja2 python 模板框架
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 测试安装
# -------------------------------------------------------------------------------
from jinja2 import Template

template = Template("hello {{ name }}")
result = template.render(name = "Jinja2")

print(result)   # hello Jinja2
