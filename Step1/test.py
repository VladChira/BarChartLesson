import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
penguins = sns.load_dataset("penguins")
sns.pairplot(data=penguins, hue="species")

plt.show()