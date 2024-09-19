import seaborn as sns
import matplotlib.pyplot as plt
# Load the penguins dataset from seaborn
penguins = sns.load_dataset("penguins")

# Create a kernel density plot with stacked distributions
sns.displot(penguins, x="flipper_length_mm", hue="species", kind="kde", multiple="stack")

sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", kind="kde")

sns.pairplot(penguins)

tips = sns.load_dataset("tips")
sns.catplot(data=tips, x="day", y="total_bill", hue="sex", kind="swarm")

plt.show()