import sys
import os
import json
import pandas as pd
import unittest

sys.path.append(os.path.abspath(os.path.join("../..")))
sys.path.append(".")
# from defaults import *

#from extract_dataframe import read_json
from info_df import DataFrame_Info
files1 = "./tests/clean_df_tel1.csv"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
df = pd.read_csv(files1)


class TestDataFrame_Info(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = DataFrame_Info(df)
        # tweet_df = self.df.get_tweet_df()
    def test_dataframe_shape(self):
        shape = (150001, 45)
        info=self.df.shape_info()
        # self.assertEqual(self.df.shape_info(),shape)
        print(info)

        print ("asserted hello")
    # def test_find_friends_count(self):
    #     friends_count = [2621, 272, 392, 392, 2608]
    #     self.assertEqual(self.df.find_friends_count(), friends_count)

if __name__ == "__main__":
    unittest.main()
