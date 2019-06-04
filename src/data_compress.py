import pandas as pd
import numpy as np

# stolen from https://github.com/CuteChibiko/TalkingData/blob/master/scripts/read_data.py
dtypes = {
        'ip'            : 'uint32',
        'app'           : 'uint16',
        'device'        : 'uint16',
        'os'            : 'uint16',
        'channel'       : 'uint16',
        'is_attributed' : 'uint8',
}

df = pd.read_csv('../data/train.csv', dtype=dtypes, parse_dates=['click_time', 'attributed_time'])

class0 = df.loc[df.is_attributed == 0, :]

class1 = df.loc[df.is_attributed == 1, :]

class0 = class0.sample(frac=.1)

class0 = class0.reset_index(drop=True)

class1 = class1.reset_index(drop=True)

df.to_feather('../data/all_data.feather')

class0.to_feather('../data/10pct_class0.feather')
class1.to_feather('../data/class1.feather')
