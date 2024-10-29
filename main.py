import functools

def deprecated(func=None,since=None, will_be_removed=None):
    if func is None:
        return lambda f: deprecated(f, since=since, will_be_removed=will_be_removed)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        msg = "Warning: function foo is deprecated. It will be removed in future versions."
        if since is not None and will_be_removed is not None:
            msg = f"""Warning: function {func.__name__} is deprecated since version {since}. It will be removed in version {will_be_removed}"""
        elif since is not None:
            msg = f"""Warning: function {func.__name__} is deprecated since version {since}. It will be removed in future versions."""
        elif will_be_removed is not None:
            msg = f"""Warning: function {func.__name__} is deprecated. It will be removed in version {will_be_removed}"""
         
        print(msg)   
        return func(*args, **kwargs)

    return wrapper    