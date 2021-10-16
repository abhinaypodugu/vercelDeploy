# FastAPI file creation
template1 = """
from fastapi import FastAPI
from {path} import {class_name}
import uvicorn

app = FastAPI()

{func_name}={class_name}()

@app.get("/")
def hello_world():
    msg="Welcome to my FastAPI project!\
        Please visit the /docs to see the API documentation."
    return msg\n
    """

template2 = """
app.add_api_route(
        path="/{route_path}",
        endpoint={endpoint},
        methods={http_methods},
    )\n
        """

template3 = """
if __name__ == "__main__":
    uvicorn.run(
            app=app,
            host='localhost',
            port=5000
        )\n"""
