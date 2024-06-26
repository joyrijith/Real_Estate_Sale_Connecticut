"""
    In this block I am doing the following clean up
    - Deleting rows that have sale value as 0  
    -For Property Type- Commercial, Vacant land, Industrial, Public Utility setting Residential type as Not applicable
    -Filling rows in Property type column having null values to 'Data Unavailable'
    -Updating Residential type as Apartments for Property Type Apartments
    - Changing the following Property type to Residential 
        Apartments
        Condo
        Single Family
        Two Family
        Three Family
        Four Family
       
    """



if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

#method for cleaning up the property and residential type coloumns
def cleaning_property_and_residential_type(dataFrame):
    #getting the column number for property type and residential type fields
    #even if the order of the column changes will not affect the script
    property_column_number=dataFrame.columns.get_loc('Property_Type')
    residential_column_number=dataFrame.columns.get_loc('Residential_Type')

    #setting the rows in property type field which does not have data
    #and have sale value > 0 to Data unavailable
    for row in range(dataFrame.shape[0]):
        if pd.isnull(dataFrame.iat[row,property_column_number]):
            dataFrame.iat[row,property_column_number]='Data Unavailable'
            dataFrame.iat[row,residential_column_number]='Data Unavailable'

    #Updating the Residential type row values to Apartments for rows
    #which has property type Apartments.
    for row in range(dataFrame.shape[0]):
        if dataFrame.iat[row,property_column_number]=='Apartments':
           dataFrame.iat[row,residential_column_number]='Apartments'          
 
    #The below for loop converts the rows having property type as 'Apartments',
    #'Condo', 'Single Family', 'Two Family', 'Three Family', 'Four Family' to Residential
    #These property type have residential type same as them so coverting property type to
    #residential will help with easy grouping and analysis
    for row in range(dataFrame.shape[0]):
        if dataFrame.iat[row,property_column_number]=='Apartments':
             dataFrame.iat[row,property_column_number]='Residential' 
   
        elif dataFrame.iat[row,property_column_number]=='Condo':
             dataFrame.iat[row,property_column_number]='Residential'   

        elif dataFrame.iat[row,property_column_number]=='Single Family':
            dataFrame.iat[row,property_column_number]='Residential'    

        elif dataFrame.iat[row,property_column_number]=='Two Family':
            dataFrame.iat[row,property_column_number]='Residential' 

        elif dataFrame.iat[row,property_column_number]=='Three Family':
            dataFrame.iat[row,property_column_number]='Residential' 

        elif dataFrame.iat[row,property_column_number]=='Four Family':
            dataFrame.iat[row,property_column_number]='Residential'                      

    #updating the residential column field for Property Type = Commercial
    #The character '_C' indicates that the property type is Commercial
    for row in range(dataFrame.shape[0]):
        if dataFrame.iat[row,property_column_number]=='Commercial':
           dataFrame.iat[row,residential_column_number]='Not Applicable_C'    

    #updating the residential column field for Property Type = Vacant Land
    #The character '_V' indicates that the property type is Vacant Land
    for row in range(dataFrame.shape[0]):
        if dataFrame.iat[row,property_column_number]=='Vacant Land':
           dataFrame.iat[row,residential_column_number]='Not Applicable_V'         

    
    #updating the residential column field for Property Type = Industrial
    #The character '_I' indicates that the property type is Industrial
    for row in range(dataFrame.shape[0]):
        if dataFrame.iat[row,property_column_number]=='Industrial':
           dataFrame.iat[row,residential_column_number]='Not Applicable_I'    

    
    #updating the residential column field for Property Type = Public Utility
    #The character '_PU' indicates that the property type is Public Utility
    for row in range(dataFrame.shape[0]):
        if dataFrame.iat[row,property_column_number]=='Public Utility':
           dataFrame.iat[row,residential_column_number]='Not Applicable_PU'    
    return dataFrame

@transformer
def transform(data, *args, **kwargs):
   
    
    
    df=data

    ## Deleting rows that have sale value as 0
    df=df[df['Sale_Amount']!=0]

    ##calling the method created above to transform the dataframe   
    cleaning_property_and_residential_type(df)
    
   
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'