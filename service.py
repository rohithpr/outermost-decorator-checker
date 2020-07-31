import os


def get_decorator_name():
    decorator_name = os.environ.get("DECORATOR_NAME")
    if not decorator_name:
        raise Exception("Environment variable `DECORATOR_NAME` not found")
    print decorator_name
    return decorator_name


def verify_outermost_decorator():
    decorator_name = get_decorator_name()


if __name__ == "__main__":
    verify_outermost_decorator()
