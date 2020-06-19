import os
import pandas as pd

from urllib.request import urlretrieve

Fremont_URL="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_fremont_data(filename="Fremont.csv",url=Fremont_URL,force_download=False):
    """Download and cache Fremont data

        Parameters
        ----------
        filename : string (optional)
            location to save the data
        url : string (optional)
            web location of data
        force_download : boolean (optional)
            if True, force redownload of data

        Returns
        -------
        data : pandas.DataFrame
            The Fremont Bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)

    data=pd.read_csv(filename,header=0,index_col="Date",parse_dates=True)
    data.columns=["Total","East","West"]                             
    
    return data
