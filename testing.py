import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint






if __name__ == '__main__':
    print('Starting program')
    place_tiles_filepath = 'data/2017/place_tiles.csv'
    # get data from csv file with pandas
    print("Reading data from csv file")
    df = pd.read_csv('data/2017/place_tiles.csv')
    #remove rows where x_coordinate or y_coordinate is NaN
    df = df.dropna(subset=['x_coordinate', 'y_coordinate'])
    max_x_coordinate = df['x_coordinate'].max()
    max_y_coordinate = df['y_coordinate'].max()
    print("Max x coordinate: {}".format(df['x_coordinate'].max()))
    print("Max y coordinate: {}".format(df['y_coordinate'].max()))
    print("Max timestamp: {}".format(df['ts'].max()))
    print("Min timestamp: {}".format(df['ts'].min()))

    #loop through all rows of dataframe and add up the usage of each tile
    total_usage = np.zeros((1050, 1050))
    progress = 0
    total_rows = df.shape[0]
    for index, row in df.iterrows():
        total_usage[int(row['y_coordinate'])][int(row['x_coordinate'])] += 1
        print("Progress: {}%".format(round(progress/total_rows*100, 1)))
        progress += 1
        

    plt.imshow(total_usage, cmap='hot', interpolation='nearest')
    plt.show()

    


    # print the first 5 rows of the dataframe
    pprint(df.head())


    


    
