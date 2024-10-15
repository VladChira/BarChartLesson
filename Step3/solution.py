import csv
import os

import seaborn as sns
sns.set_theme() 
import matplotlib.pyplot as plt
import pandas as pd

def load_dataset():
    script =  os.path.dirname(__file__)
    dataset_path = os.path.join(script, '..', 'dataset.csv')

    with open(dataset_path) as dataset_file:
        new_dataset = []
        reader = csv.DictReader(dataset_file)

        for row in reader:
            platform = row['platform']
            genre = row['genre']
            new_dataset.append({'platform': platform, 'genre': genre})
        
        allowed_platforms = ['PS4', 'XOne', 'PC', 'WiiU']
        new_dataset = [game for game in new_dataset if game['platform'] in allowed_platforms]

        grouped_dict = {}
        for game in new_dataset:
            key = (game['platform'], game['genre'])
            if key in grouped_dict:
                grouped_dict[key] += 1
            else:
                grouped_dict[key] = 1

        result = [{'platform': platform, 'genre': genre, 'count': count} 
                for (platform, genre), count in grouped_dict.items()]

        return result
    
dataset = load_dataset()

def sort_key(game):
    platform_priority = {'PS4': 0, 'XOne': 1, 'PC': 2, 'WiiU': 3}
    return (platform_priority.get(game['platform'], 4), game['genre'])

# Sort the array using the custom sorting function
dataset = sorted(dataset, key=sort_key)

df = pd.DataFrame(dataset)
sns.catplot(data=df, x='platform', y='count', hue='genre', kind='bar')
plt.text(x=0, y=140, s="Video game sales", fontsize=16, color="black")
plt.show() # Display the chart