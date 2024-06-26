"""
  In this block I will be cleaning up the non use code column
  - Clean the null value columns with Not applicable 
  - Deleting non use code above number 30 as the support doc only has non use code upto 30
"""

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

#storing all the Non Use code that is available from the State of Connecticut website
#in a list 
non_use_code_list=['01 - Family','02 - Love and Affection','03 - Inter Corporation','04 - Correcting Deed','05 - Deed Date', '06 - Portion of Property','07 - Change in Property','08 - Part Interest','09 - Tax', '10 - A Will',  '11 - Court Order','12 - Non Buildable Lot','13 - Bankrupcy','14 - Foreclosure', '15 - Government Agency','16 - Charitable Group','17 - Two Towns','18 - In Lieu Of Foreclosure','19 - Easement', '20 - Cemetery','21 - Personal Property Exchange', '22 - Money and Personal Property','23 - Zoning','24 - Plottage', '25 - Other',  '26 - Rehabilitation Deferred', '27 - CRUMBLING FOUNDATION ASSESSMENT REDUCTION', '28 - Use Assessment', '29 - No Consideration', '30 - Auction','00 - Data Unavailable'    ]

@transformer
def transform(data, *args, **kwargs):
    
    non_use_code_column_number=data.columns.get_loc('Non_Use_Code')

    df=data

    #setting the rows in property type field which does not have data
    #and have sale value > 0 to Data unavailable
    #or if the value in the row is different from what is present in the non list code
    #updating that to Data unavailable
    for row in range(df.shape[0]):
        if  df.iat[row,non_use_code_column_number] not in non_use_code_list:
            df.iat[row,non_use_code_column_number]='00 - Data Unavailable'    

  
    
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'