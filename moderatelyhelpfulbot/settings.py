import yaml

with open("../my_settings.yaml", "r", encoding="utf-8") as stream:
    settings = yaml.safe_load(stream)["default"]
