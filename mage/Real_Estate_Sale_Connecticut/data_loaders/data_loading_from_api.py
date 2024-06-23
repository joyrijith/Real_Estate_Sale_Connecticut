import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/joyrijith/DEZoomcamp_2024/releases/download/Data/Real_Estate_Sales_2008-2021_GL.zip'
    
    
    real_estate_dtypes= {
                          'Serial Number':pd.Int64Dtype(),
                          'List Year':pd.Int64Dtype(),
                          'Date Recorded':object,
                          'Town':object,
                          'Address':object,
                          'Assessed Value':pd.Int64Dtype(),
                          'Sale Amount':float,
                          'Sales Ratio':float,
                          'Property Type':object,
                          'Residential Type':object,
                          'Non Use Code':object,
                          'Assessor Remarks':object,
                          'OPM remarks':object,
                          'Location':object

        }

   
                
    return pd.read_csv(url,sep=",",compression="zip",dtype=real_estate_dtypes)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
