from typing import List

#api decorator which will be used by sub classes
def api(
    *args,
    api_name: str = None,
    route: str = None,
    http_methods: List[str] = None,
    **kwargs,
):

    def decorator(func):
        _api_name = func.__name__ if api_name is None else api_name
        _api_route = _api_name if route is None else route
        _http_methods = http_methods if http_methods else ['GET']
        setattr(func, "_is_api", True)
        setattr(func, "_api_name", _api_name)
        setattr(func, "_api_route", _api_route)
        setattr(func, "_http_methods", _http_methods)
        return func

    return decorator
