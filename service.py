import checker
import os


def get_decorator_name():
    decorator_name = os.environ.get("DECORATOR_NAME")
    if not decorator_name:
        raise Exception("Environment variable `DECORATOR_NAME` not found")
    print decorator_name
    return decorator_name


def get_file_names():
    files = []
    for dirname, subdirnames, file_names in os.walk("./"):
        for file_name in file_names:
            if file_name.endswith(".py"):
                files.append(os.path.join(dirname, file_name))
    return files


def get_errors(decorator_name, file_names):
    errors = []
    for file_name in file_names:
        errors.extend(checker.check_outermost_decorator(decorator_name, file_name))
    return errors


def process_errors(decorator_name, errors):
    if errors:
        # TODO: Post a comment on Github
        message = "{count} errors found while ensuring that {name} is the outermost decorator".format(
            count=len(errors),
            name=decorator_name
        )
        print message
        print errors
        raise Exception(message)
    else:
        print "No errors found"


def verify_outermost_decorator():
    decorator_name = get_decorator_name()
    file_names = get_file_names()
    errors = get_errors(decorator_name, file_names)
    process_errors(decorator_name, errors)


if __name__ == "__main__":
    verify_outermost_decorator()
