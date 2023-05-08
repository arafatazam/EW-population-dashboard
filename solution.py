import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

INPUT_FILE = "EW_Religion_Sex_Age_Ethnic_group.csv"
OUTPUT_FILE = "21087019.png"
DATA:pd.DataFrame

def read_data():
    global DATA
    DATA = pd.read_csv(INPUT_FILE, keep_default_na='')

def draw_population_pyramid(ax:plt.Axes):
    pass

def draw():
    # Create a figure and a gridspec with two rows and two columns
    fig = plt.figure(figsize=(8, 8))
    gs = gridspec.GridSpec(nrows=2, ncols=2)

    # Define the data for the plots
    x = np.arange(0, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.exp(x)

    # Create the first subplot in the first row and first column
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(x, y1, color='red')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Sine')

    # Create the second subplot in the first row and second column
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(x, y2, color='green')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Cosine')

    # Create the third subplot in the second row and first column
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.plot(x, y3, color='blue')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_title('Tangent')

    # Create the fourth subplot in the second row and second column
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.plot(x, y4, color='purple')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_title('Exponential')

    # Adjust the spacing between subplots and save the figure
    fig.tight_layout()
    # plt.savefig('four_subplots.png')
    plt.show()



def main():
    read_data()
    df = DATA.groupby(['Sex','Age Code', 'Age'], as_index=False)['Observation'].sum()
    print(df[['Age Code']])



if __name__ == "__main__":
    main()
