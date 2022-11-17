from pathlib import Path


def get_project_path():
    """
    Get the path of the root project
    :return: Path
    """
    return Path(__file__).parents[2].resolve()
