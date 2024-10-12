import csv

# Create the new dataset
new_dataset = []

with open('dataset.csv') as dataset_file:
    # DictReader will convert the rows into dictionaries
    reader = csv.DictReader(dataset_file)

    for row in reader:
        # For each game in the dataset, extract the platform and genre
        platform = row['platform']
        genre = row['genre']
        # Add only these two to the new dataset
        new_dataset.append({'platform': platform, 'genre': genre})
    
    allowed_platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    for game in new_dataset:
        if not game['platform'] in allowed_platforms:
            new_dataset.remove(game)
    
    for i in range(0, 10):
        print(new_dataset[i])