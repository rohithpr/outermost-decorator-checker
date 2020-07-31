import ast
import functools


def get_code(file_name):
    with open(file_name) as fp:
        return fp.read()


def get_tree(code):
    return ast.parse(code)


def get_decorator_name(decorator):
    if hasattr(decorator, "id"):
        return decorator.id

    if hasattr(decorator, "attr"):
        return decorator.attr

    if hasattr(decorator, "func"):
        return get_decorator_name(decorator.func)


def has_decorator(decorator_name, function):
    for decorator in function.decorator_list:
        if get_decorator_name(decorator) == decorator_name:
            return True
    return False


def get_incompliant_functions(decorator_name, tree, file_name):
    functions = filter(lambda x: type(x) == ast.FunctionDef, tree.body)
    decorator_checker = functools.partial(has_decorator, decorator_name)
    gateway_exposed_functions = filter(decorator_checker, functions)
    return filter(
        lambda x: get_decorator_name(x.decorator_list[0]) != decorator_name,
        gateway_exposed_functions
    )


def get_message(decorator_name, function_name):
    return "`@{decorator_name}` is not the outermost decorator on the function `{name}`.".format(
        decorator_name=decorator_name,
        name=function_name
    )


def generate_error_commands(decorator_name, incompliant_functions, file_name):
    return map(lambda x: {
        "lineno": x.lineno,
        "message": get_message(decorator_name, x.name),
        "file_name": file_name,
    }, incompliant_functions)


def check_outermost_decorator(decorator_name, file_name):
    code = get_code(file_name)
    tree = get_tree(code)
    incompliant_functions = get_incompliant_functions(decorator_name, tree, file_name)
    errors = generate_error_commands(decorator_name, incompliant_functions, file_name)
    return list(errors)
