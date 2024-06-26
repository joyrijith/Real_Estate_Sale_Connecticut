if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    #updating column related work in this transformer

    #assigning data to a new dataframe variable df
    df=data

    
    #deleting columns Sales Ratio, Assessor Remarks, OPM remarks and Location as they are not useful for the analysis
    df=df.drop(['Sales Ratio','Assessor Remarks','OPM remarks','Location'], axis=1)
    
    #gettning the sale amount column number in a variable 
    #using this we can create sold to Assessed column always after Sale Amount column
    sale_amount_column_number=df.columns.get_loc('Sale Amount')
    #addinga  new column called sold to assessed which gives an idea of the percentage increase
    df.insert(loc=sale_amount_column_number+1,column='Sold to Assessed Percentage',value=((df['Sale Amount'] / df['Assessed Value'])*100))

    df['Sold to Assessed Percentage'] = df['Sold to Assessed Percentage'].apply(lambda x: round(x, 2))

    #updating column names and replacing space with underscore
    df.columns=df.columns.str.replace(" ","_")

    

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
