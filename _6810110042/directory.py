import pathlib


def create_directory(name=1):
    """
    xxx
    """
    path = pathlib.Path(name)
    if not check_directory(path):
        path.mkdir(parents=True)

    return path


def check_directory(path):
    return path.exists()
