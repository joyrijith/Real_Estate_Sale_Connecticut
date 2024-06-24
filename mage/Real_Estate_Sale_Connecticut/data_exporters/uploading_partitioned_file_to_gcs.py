##importing these libraries to help partition the files and then upload it 
##in gcs
import pyarrow as pa
import pyarrow.parquet as pq 
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

##need to set where the credentials to connect to google cloud can be found
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= "/home/src/astute-backup-427300-m6-4cb85eb4a947.json"

## setting the bucket name and the project_id
bucket_name = 'real_estate_sale_connecticut'
project_id='astute-backup-427300-m6'

#setting the table name that the py arrow library will use for partitioning
table_name="real_estate_sale_connecticut"

root_path= f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    
    #here we're creating a new column just month and year
    #which will be used for partitioning the file
    data['Date_Recorded_Month_Year']=data['Date_Recorded'].dt.to_period('M').astype(str)

    #in pyarrow we need to define the table
    #reading the dataframe into a pyarrow table
    table=pa.Table.from_pandas(data)

    
    gcs=pa.fs.GcsFileSystem()

    #using this to write to the Dataset
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['Date_Recorded_Month_Year'],
        filesystem=gcs

    )