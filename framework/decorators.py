TEST_REGISTRY = []

def test(name=None, timeout=100):

    def decorator(func):

        TEST_REGISTRY.append({
            "name": name or func.__name__,
            "func": func,
            "timeout": timeout
        })

        return func

    return decorator