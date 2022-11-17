import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.helpers import helper_functions

project_path = helper_functions.get_project_path()
visual_path = project_path / "images"

format = "png"
resolution = 300


def plot_correlation(df: pd.DataFrame, format="png", resolution=300):
    fig, ax = plt.subplots(figsize=(20, 10))
    corr = df.corr()
    ax = sns.heatmap(corr, square=True, ax=ax, annot=True, cmap="coolwarm")
    ax.set_title("Correlation of each feature")
    plt.tight_layout()
    plt.savefig(
        visual_path / "correlation", format=format, resolution=resolution
    )
