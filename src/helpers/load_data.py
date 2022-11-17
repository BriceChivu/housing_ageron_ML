import pandas as pd

from src.helpers import helper_functions


def load_housing_raw_data():
    project_path = helper_functions.get_project_path()
    return pd.read_excel(project_path / "data" / "raw" / "housing.xlsx")
