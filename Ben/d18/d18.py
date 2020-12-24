
import ast

class AST_swap_sub_mult(ast.NodeTransformer):
    def visit_Sub(_,node): 
        return ast.copy_location(ast.Mult(),node)

class AST_swap_mult_add(ast.NodeTransformer):
    def visit_Mult(self, node): 
        return ast.copy_location(ast.Add(),node)

    def visit_Add(self, node): 
        return ast.copy_location(ast.Mult(),node)

def p1(line, translate, transformer):
    # replace * with - to keep ast structure and replace - later
    line = line.translate(line.maketrans(translate))
    # parse the line as a python expression into an AST
    line_ast = ast.parse(line,'','eval')
    # transform the AST to replace - with *
    #   which keeps the ast structure (therefore the operator precedence)
    line_ast = transformer().visit(line_ast)
    # compile the transformed ast
    c = compile(line_ast,'','eval')
    # eval the ast
    return eval(c)

with open("input.txt", "r") as f:
    data = f.read()
    a1 = sum([p1(line, {'*':'-'}, AST_swap_sub_mult) for line in data.split('\n')])
    print('a1',a1)
    a2 = sum([p1(line, {'*':'+', '+':'*'}, AST_swap_mult_add) for line in data.split('\n')])
    print('a2',a2)

