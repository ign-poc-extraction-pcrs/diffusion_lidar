# pylint: disable=import-error
from fastapi import FastAPI

tags_metadata = [{"name": "hello_world", "description": "route test"}]

app = FastAPI(
    title="API pour l'interface diffusion lidar",
    description="description à completer",
    version="0.0.1",
    openapi_tags=tags_metadata,
)


@app.get("/hello_world")
def hello_world():
    """route test

    Returns:
        dict: retourne un message test
    """
    return {"hello": "world"}
