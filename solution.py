import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

INPUT_FILE = "EW_Religion_Sex_Age_Ethnic_group.csv"
OUTPUT_FILE = "21087019.png"
DATA: pd.DataFrame


def read_data():
    global DATA
    DATA = pd.read_csv(INPUT_FILE, keep_default_na='')


def draw_heading(ax: plt.Axes):
    ax.text(0.5, 0.5, "UK Census 2021: Religion, Ethnicity and Age of England & Wales",
            fontsize=30, ha="center", va="center")
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(top=False, bottom=False, left=False,
                   right=False, labelleft=False, labelbottom=False)


def draw_age_barchart(ax: plt.Axes):
    df = DATA.groupby('Age Code', as_index=False)['Observation'].sum()
    sns.barplot(x='Age Code', y='Observation', data=df, ax=ax)

    # Set labels for x and y axes
    ax.set_xlabel('Age', fontsize=20)
    ax.set_ylabel('Observation', fontsize=20)

    # Remove top and right spines of the plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xticks(range(0, 91, 5))
    ax.set_xticklabels(df['Age Code'][::5])

    # Remove tick marks from x and y axes
    ax.tick_params(axis='both', which='both', length=0, labelsize=15)


def main():
    read_data()
    fig = plt.figure(figsize=(20, 12))
    gs = fig.add_gridspec(20, 12)
    draw_heading(plt.subplot(gs[:2, :]))
    draw_age_barchart(plt.subplot(gs[2:8, :]))
    plt.show()


if __name__ == "__main__":
    main()
