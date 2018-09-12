#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-12
# @copyright by hoojo @2018
# @link http://www.bjhee.com/jinja2-extension.html
# @changelog user custom extension


# ===============================================================================
# 标题：利用 pygments 库开发 jinja2 template的扩展，做到代码高亮的效果
# ===============================================================================
# 使用：pip install pygments
# -------------------------------------------------------------------------------
# 描述：Pygments是Python提供语法高亮的工具，官网是pygments.org。
# http://pygments.org/docs/
# -------------------------------------------------------------------------------
from jinja2 import nodes
from jinja2.ext import Extension

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import guess_lexer, get_lexer_by_name


# -------------------------------------------------------------------------------
# 创建一个自定义扩展类，继承jinja2.ext.Extension
# -------------------------------------------------------------------------------
class PygmentsExtension(Extension):

    # 定义该扩展的语句关键字，这里表示模板中的{% code %}语句会该扩展处理
    tags = set(['code'])

    def __init__(self, environment):
        # 初始化父类，必须这样写
        super(PygmentsExtension, self).__init__(environment)

        # 在Jinja2的环境变量中添加属性，
        # 这样在Flask中，就可以用app.jinja_env.pygments来访问
        environment.extend(
            pygments=self,
            pygments_support=True
        )

    # 重写jinja2.ext.Extension类的parse函数
    # 这是处理模板中{% code %}语句的主程序
    def parse(self, parser):
        # 进入此函数时，即表示{% code %}标签被找到了
        # 下面的代码会获取当前{% code %}语句在模板文件中的行号
        lineno = next(parser.stream).lineno

        # 获取{% code %}语句中的参数，比如我们调用{% code 'python' %}，
        # 这里就会返回一个jinja2.nodes.Const类型的对象，值为'python'
        lang_type = parser.parse_expression()

        # 将参数封装为列表
        args = []
        if lang_type is not None:
            args.append(lang_type)

            # 下面的代码可以支持两个参数，参数之间用逗号分隔，不过本例中用不到
            # 这里先检查当前处理流的位置是不是个逗号，是的话就再获取一个参数
            # 不是的话，就在参数列表最后加个空值对象
            # if parser.stream.skip_if('comma'):
            #     args.append(parser.parse_expression())
            # else:
            #     args.append(nodes.Const(None))

        # 解析从{% code %}标志开始，到{% endcode %}为止中间的所有语句
        # 将解析完后的内容存在body里，并将当前流位置移到{% endcode %}之后
        body = parser.parse_statements(['name:endcode'], drop_needle=True)

        # 返回一个CallBlock类型的节点，并将其之前取得的行号设置在该节点中
        # 初始化CallBlock节点时，传入我们自定义的"_pygmentize"方法的调用，
        # 两个空列表，还有刚才解析后的语句内容body
        return nodes.CallBlock(self.call_method('_pygmentize', args), [], [], body).set_lineno(lineno)


    # 这个自定义的内部函数，包含了本扩展的主要逻辑。
    # 其实上面parse()函数内容，大部分扩展都可以重用
    def _pygmentize(self, lang_type, caller):
        # 初始化HTML格式器
        formatter = HtmlFormatter(linenos='table')

        # 获取{% code %}语句中的内容
        # 这里caller()对应了上面调用CallBlock()时传入的body
        content = caller()

        # 将模板语句中解析到了lang_type设置为我们要高亮的语言类型
        # 如果这个变量不存在，则让Pygmentize猜测可能的语言类型
        lexer = None
        if lang_type is None:
            lexer = guess_lexer(content)
        else:
            lexer = get_lexer_by_name(lang_type)

        # 将{% code %}语句中的内容高亮，即添加各种<span>, class等标签属性
        return highlight(content, lexer, formatter)