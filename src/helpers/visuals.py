from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Path: src\helpers\visuals.py
def plot_correlation(
    df: pd.DataFrame,
    save_path=Path.cwd() / "images",
    format_img="png",
    resolution=300,
) -> None:
    """
    Plot the correlation matrix of a dataframe and save it to the images folder

    Args:
        df: dataframe from which to plot the correlation matrix
        save_path: path to save the plot to
        format_img: format of the image to save
        resolution: resolution of the image to save
    """
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, square=True, annot=True, cmap="coolwarm")
    # add title
    plt.title("Correlation Matrix")
    plt.savefig(
        save_path / f"correlation_matrix.{format_img}",
        dpi=resolution,
    )
    plt.show()
