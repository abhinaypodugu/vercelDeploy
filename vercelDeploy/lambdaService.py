import inspect
import os
from vercelDeploy.inferenceAPI import InferenceAPI
from vercelDeploy.template import *

class LambdaService:

    def create_fastapi_file(self, module_name):
        class_name = self.__name__
        apis_list = []

        #gets all the @api functions in the current class and add it to the api_list
        for _, function in inspect.getmembers(
            self,
            predicate=lambda x: inspect.isfunction(x) or inspect.ismethod(x),
        ):
            if hasattr(function, "_is_api"):
                api_name = getattr(function, "_api_name")
                route = getattr(function, "_api_route", None)
                http_methods = getattr(function, "_http_methods")
                user_func = function.__get__(self)
                apis_list.append(
                    InferenceAPI(
                        self,
                        api_name,
                        user_func=user_func,
                        http_methods=http_methods,
                        route=route,
                    )
                )

        store_path = os.path.abspath(os.curdir) + '\\build\\fast_api.py'
        func_name = class_name.lower() + "_func"
        complete_template = template1.format(
            path=module_name,
            class_name=class_name,
            func_name=func_name
        )

        # Add the routes, http_methods and the endpoints for the functions with @api decorator
        for api in apis_list:
            complete_template += template2.format(
                route_path=api.route,
                endpoint=f"{func_name}.{api._name}",
                http_methods=api._http_methods
            )

        # Set the host and port
        complete_template += template3

        # Write the above created template to a file. Here it is fast_api.py file
        try:
            with open(store_path, "w") as f:
                f.write(complete_template)
        except FileExistsError:
            raise Exception("The FastAPI file already exists")
