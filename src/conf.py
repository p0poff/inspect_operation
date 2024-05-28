import yaml

def getConf(path: str) -> dict:
    with open(path) as f:
        conf = yaml.safe_load(f)

    return conf