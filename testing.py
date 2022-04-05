
import pandas as pd
from pprint import pprint






if __name__ == '__main__':
    print('Starting program')
    place_tiles_filepath = 'data/2017/place_tiles.csv'
    # get data from csv file with pandas
    print("Reading data from csv file")
    df = pd.read_csv(place_tiles_filepath)

    # print the first 5 rows of the dataframe
    pprint(df.head())


    


    
