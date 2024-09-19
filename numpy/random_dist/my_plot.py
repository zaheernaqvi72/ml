import matplotlib.pyplot as plt
import seaborn as sns

dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)

plt.show()



sns.displot([0, 1, 2, 3, 4, 5, 6,7,8,9,10], hist=True, kde=True, bins=10)

plt.show()




