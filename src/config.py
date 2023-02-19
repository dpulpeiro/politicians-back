import os


class Config:
    DEBUG = False
    # For development
    HOST = "0.0.0.0"
    PORT = 8000
    PAGE_SIZE = 10
    ELASTICSEARCH_URL = "http://elasticsearch:9200"

    def __init__(self):
        Config.DEBUG = Config.get_from_env(
            "DEBUG", default=Config.DEBUG, must_exist=False, astype="bool"
        )
        Config.PAGE_SIZE = Config.get_from_env(
            "PAGE_SIZE", default=Config.PAGE_SIZE, must_exist=False, astype="int"
        )
        Config.ELASTICSEARCH_URL = Config.get_from_env(
            "ELASTICSEARCH_URL",
            default=Config.ELASTICSEARCH_URL,
            must_exist=False,
        )
        Config.HOST = Config.get_from_env("HOST", default=Config.HOST, must_exist=False)
        Config.PORT = Config.get_from_env(
            "PORT", default=Config.PORT, must_exist=False, astype="int"
        )

    @staticmethod
    def cast(string, astype):
        if astype == "str":
            return string
        if astype == "int":
            return int(string)
        if astype == "bool":
            return string.lower() in [True, "true", "1", "t", "y", "yes"]

        raise Exception(f"'{string}' invalid cast")

    @staticmethod
    def get_from_env(variable, default=None, must_exist=False, astype="str"):
        variable_from_env = os.environ.get(variable, None)
        if variable_from_env:
            return Config.cast(variable_from_env, astype)

        secret_file = os.environ.get(variable + "_FILE", None)
        if secret_file:
            return Config.cast(Config.load_from_file(secret_file), astype)
        if must_exist:
            raise Exception(f"'{variable}' must exist")

        return default

    @staticmethod
    def load_from_file(file):
        with open(file, "r") as f:
            return f.readline()


settings = Config()
