### Function to extract spectra from json files 

import os
import pandas as pd

def spectra(file):
    sn_name, file_extension = os.path.splitext(file)
    df = pd.read_json(file)
    spectra = df[sn_name]['spectra']
    df_spec = pd.DataFrame.from_dict(spectra)
    
    wave

    return df_spec