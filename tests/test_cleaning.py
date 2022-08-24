import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))

import warnings
warnings.filterwarnings('ignore')
import unittest

import pandas as pd


class TestDataframe(unittest.TestCase):
    def setUp(self) -> pd.DataFrame:
        try:
            data = pd.read_csv("clean_df_tel1.csv")
            self.dataframe = data
        except IOError:
            print("could not open csv file")

    def test_dataframe_shape(self):
        self.assertEqual(self.dataframe.shape, (150001, 45))
        print ("asserted hello")

    def test_columns(self):
        dataset_columns = [
            'Bearer Id', 
            'Start', 
            'Start ms', 
            'End', 
            'End ms', 
            'Dur. (ms)', 
            'IMSI',
            'MSISDN/Number',
            'IMEI', 
            'Last Location Name', 
            'Avg RTT DL (ms)',
            'Avg RTT UL (ms)', 
            'Avg Bearer TP DL (kbps)', 
            'Avg Bearer TP UL (kbps)',
            'DL TP < 50 Kbps (%)',
            '50 Kbps < DL TP < 250 Kbps (%)',
            '250 Kbps < DL TP < 1 Mbps (%)', 
            'DL TP > 1 Mbps (%)',
            'UL TP < 10 Kbps (%)', 
            '10 Kbps < UL TP < 50 Kbps (%)',
            '50 Kbps < UL TP < 300 Kbps (%)', 
            'UL TP > 300 Kbps (%)',
            'Activity Duration DL (ms)', 
            'Activity Duration UL (ms)', 
            'Dur. (ms).1',
            'Handset Manufacturer', 
            'Handset Type', 
            'Nb of sec with Vol DL < 6250B',
            'Nb of sec with Vol UL < 1250B', 
            'Social Media DL (Bytes)',
            'Social Media UL (Bytes)', 
            'Google DL (Bytes)', 
            'Google UL (Bytes)',
            'Email DL (Bytes)', 
            'Email UL (Bytes)', 
            'Youtube DL (Bytes)',
            'Youtube UL (Bytes)', 
            'Netflix DL (Bytes)', 
            'Netflix UL (Bytes)',
            'Gaming DL (Bytes)', 
            'Gaming UL (Bytes)', 
            'Other DL (Bytes)',
            'Other UL (Bytes)', 
            'Total UL (Bytes)', 
            'Total DL (Bytes)'


        ]
        self.assertEqual(self.dataframe.columns, dataset_columns)


if __name__ == "__main__":
    unittest.main()