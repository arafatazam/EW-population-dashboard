import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

INPUT_FILE = "EW_Religion_Sex_Age_Ethnic_group.csv"
OUTPUT_FILE = "21087019.png"
DATA: pd.DataFrame


def read_data():
    global DATA
    DATA = pd.read_csv(INPUT_FILE, keep_default_na='')


def draw_heading(ax: plt.Axes):
    ax.text(0.5, 0.5, "England and Walse Census 2021: Religion, ethnicity and age",
            fontsize=12, ha="center")
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(top=False, bottom=False, left=False,
                   right=False, labelleft=False, labelbottom=False)


def main():
    read_data()
    fig = plt.figure()
    gs = fig.add_gridspec(20, 12)
    draw_heading(plt.subplot(gs[:2, :]))
    plt.show()


if __name__ == "__main__":
    main()
