from pylogkit.config_logging import get_logger


def run() -> None:
    print("Hello world")


if __name__ == "__main__":
    logger = get_logger("meuapp")

    logger.debug("Esse é meu primeiro teste")

    run()
