def graph(cleaned_dataset):
    # https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
    # !pip install brewer2mpl
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings(action='once')

    large = 22
    med = 16
    params = {'axes.titlesize': large,
              'legend.fontsize': med,
              'figure.figsize': (16, 10),
              'axes.labelsize': med,
              'axes.titlesize': med,
              'xtick.labelsize': med,
              'ytick.labelsize': med,
              'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')
    sns.set_style("white")

    # Import Data

    # Draw Plot
    plt.figure(figsize=(16, 10), dpi=80)
    sns.kdeplot(cleaned_dataset["active"], shade=True,
                color="g", label="Active", alpha=.7)
    sns.kdeplot(cleaned_dataset["icu"], shade=True,
                color="deeppink", label="ICU", alpha=.7)
    sns.kdeplot(cleaned_dataset["ventilator"], shade=True,
                color="dodgerblue", label="Ventilator", alpha=.7)
    sns.kdeplot(cleaned_dataset["cleared"], shade=True,
                color="orange", label="cleared", alpha=.7)

    # Decoration
    plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    graph()
