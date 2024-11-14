import functools

def deprecated(func=None,since=None, will_be_removed=None):
    if func is None:
        return lambda f: deprecated(f, since=since, will_be_removed=will_be_removed)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        msg = f"Warning: function {func.__name__} is deprecated"
        if since is not None:
            msg += f""" since version {since}"""
        
        if will_be_removed is not None:
            msg += f""". It will be removed in version {will_be_removed}"""
        else:
            msg += f""". It will be removed in future versions.""" 
            
        print(msg)   
        return func(*args, **kwargs)

    return wrapper    