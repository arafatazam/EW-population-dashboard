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
    ax.text(0.5, 0.5, "England & Wales Census 2021: Religion, Ethnicity and Age",
            fontsize=30, ha="center", va="center")
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


def draw_religion_piechart(ax: plt.Axes):
    df = DATA.groupby('Religion', as_index=False)['Observation'].sum(
    ).sort_values(by='Observation', ascending=False)
    colors = sns.color_palette('muted')[0:10]
    ax.pie(df['Observation'], colors=colors,
           autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '', startangle=210)
    ax.axis('equal')
    ax.legend(df['Religion'], loc='center left')
    ax.set_title('Distribution by Religion', fontsize=20)


def draw_ethnicity_piechart(ax: plt.Axes):
    df = DATA.groupby('Ethnic Group', as_index=False)[
        'Observation'].sum().sort_values(by='Observation', ascending=False)
    colors = sns.color_palette('muted')[4:]
    ax.pie(df['Observation'], colors=colors,
           autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '', startangle=40)
    ax.axis('equal')
    ax.legend(df['Ethnic Group'], loc='center right')
    ax.set_title('Distribution by Ethnic Group', fontsize=20)


def main():
    read_data()
    fig = plt.figure(figsize=(16, 25))
    fig.set_facecolor('lightblue')
    gs = fig.add_gridspec(nrows=25, ncols=16, wspace=2, hspace=1)
    draw_heading(plt.subplot(gs[:2, :]))
    draw_age_barchart(plt.subplot(gs[2:5, :]))
    draw_religion_piechart(plt.subplot(gs[6:10, :8]))
    draw_ethnicity_piechart(plt.subplot(gs[6:10, 8:]))
    fig.savefig(OUTPUT_FILE, dpi=300)


if __name__ == "__main__":
    main()
