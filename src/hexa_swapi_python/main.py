import inspect
import logging

from hexa_swapi_infra.controllers.api import make_app
import uvicorn

logger = logging.getLogger(__name__)


def main() -> None:
    module = inspect.getmodule(make_app)
    config = uvicorn.Config(
        app=f"{module.__name__}:{make_app.__name__}",  # type: ignore  # noqa: PGH003
        host="localhost",
        port=8080,
        log_level=logging.DEBUG,
    )
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main()
