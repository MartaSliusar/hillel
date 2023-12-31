import functools


def mask_data(target_key: str, replace_with: str = "*"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if target_key in res:
                res[target_key] = replace_with * len(res[target_key])
            return res

        return wrapper

    return decorator


@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
