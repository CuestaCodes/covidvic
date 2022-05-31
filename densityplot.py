def graph(cleaned_dataset):
    # https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
    # https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/broken_axis.html
    import pandas as pd
    import matplotlib.pyplot as plt
    import warnings

    warnings.filterwarnings(action='once')

    # Import Data
    df = cleaned_dataset
    df2 = pd.read_csv(
        'https://github.com/selva86/datasets/raw/master/mortality.csv')

    # Define the upper limit, lower limit, interval of Y axis and colors
    y_LL = 0
    y_UL = max(df["active"]) + 100
    y_interval = 50
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    # Draw Plot and Annotate
    fig, ax = plt.subplots(1, 1, figsize=(16, 9), dpi=80)

    columns = df.columns[4:]
    for i, column in enumerate(columns):
        plt.plot(df.date, df[column], lw=1.5, color=mycolors[i])
        plt.text(df.shape[0]+1, df[column].values[-1],
                 column, fontsize=14, color=mycolors[i])

    # Draw Tick lines
    for y in range(y_LL, y_UL, y_interval):
        plt.hlines(y, xmin=0, xmax=71, colors='black',
                   alpha=0.3, linestyles="--", lw=0.5)

    # Decorations
    plt.tick_params(axis="both", which="both", bottom=False, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(.3)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(.3)
    plt.gca().spines["left"].set_alpha(.3)

    plt.title(
        'Victorian hospital COVID figures', fontsize=22)
    plt.yticks(range(y_LL, y_UL, y_interval), [
               str(y) for y in range(y_LL, y_UL, y_interval)], fontsize=12)
    plt.xticks(range(0, df.shape[0], 12), df.date[::12],
               horizontalalignment='left', fontsize=12)
    plt.ylim(y_LL, y_UL)
    plt.xlim(-2, 80)
    plt.show()


if __name__ == "__main__":
    graph()
