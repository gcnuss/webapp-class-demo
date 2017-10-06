import pandas as pd

class DataModel(object):
    def __init__(self):
        self.data = pd.read_csv("data/baby_sizes.csv")
        self.idx_data = self.data.set_index(self.data['week'], drop=True, inplace=False)

    def get_food(self, week):
        row = self.idx_data.loc[week].to_dict()
        return row
