import csv
import os

def load_dataset():
    script =  os.path.dirname(__file__)
    dataset_path = os.path.join(script, '..', 'dataset.csv')

    with open(dataset_path) as dataset_file:
        new_dataset = []
        reader = csv.DictReader(dataset_file)

        for row in reader:
            print(row)
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
# print(dataset)