class InferenceAPI:

    def __init__(
        self,
        service,
        name,
        user_func: callable,
        route=None,
        http_methods=None,
    ):
        self._service = service
        self._name = name
        self._user_func = user_func
        self._http_methods = http_methods
        self.route = name if route is None else route
