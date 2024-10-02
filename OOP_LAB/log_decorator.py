def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"Method called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
