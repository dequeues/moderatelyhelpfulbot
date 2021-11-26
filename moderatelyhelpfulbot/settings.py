import os

import yaml

with open(
    os.path.join(os.path.dirname(__file__), "../settings.yaml"), "r", encoding="utf-8"
) as stream:
    settings = yaml.safe_load(stream)["default"]
