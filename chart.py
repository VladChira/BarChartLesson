import pandas as pd
df = pd.read_csv('dataset.csv')

platform_filter = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_df = df[df['platform'].isin(platform_filter)]

final_df = filtered_df.groupby(['platform', 'genre']).size().reset_index(name='count')
final_df['platform'] = pd.Categorical(final_df['platform'], platform_filter)
final_df = final_df.sort_values(by=['platform', 'genre'])
print(final_df)
import seaborn as sns
sns.set_theme() 
sns.catplot(data=final_df, x="platform", y="count", hue="genre", kind="bar")

import matplotlib.pyplot as plt
plt.show()