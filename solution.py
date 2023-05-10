import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

INPUT_FILE = "EW_Religion_Sex_Age_Ethnic_group.csv"
OUTPUT_FILE = "21087019.png"
FIG_WIDTH = 16
FIG_LENGTH = 25
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
    df = df[df['Observation'] > 0]
    colors = sns.color_palette('muted')[0:10]
    ax.pie(df['Observation'], colors=colors,
           autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '', startangle=210)
    ax.axis('equal')
    ax.legend(df['Religion'], loc='center left', fontsize=14)
    ax.set_title('Distribution by Religion', fontsize=20)


def draw_ethnicity_piechart(ax: plt.Axes):
    df = DATA.groupby('Ethnic Group', as_index=False)[
        'Observation'].sum().sort_values(by='Observation', ascending=False)
    df = df[df['Observation'] > 0]
    colors = sns.color_palette('muted')[4:]
    ax.pie(df['Observation'], colors=colors,
           autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '', startangle=40)
    ax.axis('equal')
    ax.legend(df['Ethnic Group'], loc='center right', fontsize=14)
    ax.set_title('Distribution by Ethnic Group', fontsize=20)


def draw_description_box(txt: str, ax: plt.Axes, ha: str = 'left'):
    bb = ax.get_tightbbox()
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5, pad=0.75)
    mtext = ax.text(0.01, 0.5, txt, wrap=True, va='center', color='gray',
                    bbox=props, ha=ha, fontsize=18, fontweight='bold')
    mtext._get_wrap_line_width = lambda: (abs(bb.x0-bb.x1)*72*2/300)

    # make the ticks and spines go away
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(top=False, bottom=False, left=False,
                   right=False, labelleft=False, labelbottom=False)


def main():
    read_data()
    plt.rcParams['font.family'] = ['DejaVu Sans', 'Helvetica', 'Arial']
    fig = plt.figure(figsize=(FIG_WIDTH, FIG_LENGTH), dpi=300)
    gs = fig.add_gridspec(
        nrows=FIG_LENGTH, ncols=FIG_WIDTH, wspace=2, hspace=1)
    draw_heading(plt.subplot(gs[:2, :]))

    description = 'England and wales age distribution barplot is narrower in the beginning indicating a falling birth-rate. ' +\
        'Then there are higher bars in the working age portion 16-64 which indicates an aging population and the effect of ' +\
        'net migration'
    draw_description_box(description, plt.subplot(gs[2, :]))
    draw_age_barchart(plt.subplot(gs[3:8, :]))

    description = 'Christianity(46.2%) is the largest religion in England & Wales, ' +\
        'followed by no religion(37.2%). Islam(6.5%) is the second largest among those who follows religion.'
    draw_religion_piechart(plt.subplot(gs[9:14, :10]))
    draw_description_box(description, plt.subplot(gs[9:14, 10:]))

    description = 'England & Wales is a ethnically diverse place. White ethnicities(81.7%) are the largest ethnic group,' +\
        'followed by Asian ethnicities(9.3%) and Black ethnicities(4%)'
    draw_description_box(description, plt.subplot(gs[15:20, :6]))
    draw_ethnicity_piechart(plt.subplot(gs[15:20, 6:]))
    fig.savefig(OUTPUT_FILE)


if __name__ == "__main__":
    main()
