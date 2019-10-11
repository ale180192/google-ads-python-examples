import yaml


def load_settings(file_name=None):
    with open(file_name) as f:
        # use safe_load instead load
        data = yaml.safe_load(f)
    return data