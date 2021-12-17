import ast

def file_contents(ast_filename):
    with open(ast_filename) as fd:
        file_contents = fd.read()
    return file_contents

def funcs_from_file_contents(file_contents):
    module = ast.parse(file_contents)
    function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

    return function_definitions

def simple_print(func_defs):
    for f in func_defs:
        print('---')
        print(f.name)
        print('---')
        print(ast.get_docstring(f))



if __name__ == '__main__':
    fname = 'samplemodule.py'
    file_contents = file_contents(fname)
    funcs_defs = funcs_from_file_contents(file_contents)
    simple_print(funcs_defs)