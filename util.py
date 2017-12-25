from urllib.request import urlopen
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

def retry(times):
    def tryIt(func):
        def f(*args):
            attempts = 0
            while attempts < times:
                try:
                    return func(*args)
                except Exception as e:
                    attempts += 1
                    print(e)
        return f
    return tryIt


def parse_js(data):
	parser = Parser()
	tree = parser.parse(data)
	fields = {
		getattr(node.left, 'value', ''): 
		getattr(node.right, 'value', '') for node in nodevisitor.visit(tree) if isinstance(node, ast.Assign)
	}
	return fields

# @retry(3)
# def test():
# 	html = urlopen("www.baidu.com")
# 	print(html.read())

# test()