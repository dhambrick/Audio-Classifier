import numpy as np 
import scipy as sp 
import scipy.io.wavfile as swav 
import scipy.io as sio 
import pandas as pd 
from sklearn import preprocessing


def LoadMetaData(path):
    meta_data_df = pd.read_csv(path)
    le = preprocessing.LabelEncoder()
    meta_data_df['label(encoded)'] = list(le.fit_transform(meta_data_df['label']))
    return meta_data_df
def LoadAudioData(meta_data_df,path):
    meta_data_df['data'] = [sio.wavfile.read(path+name)[1] for name in fnames]
    return meta_data_df
def ResampleAudioData(data_df, num_samples):
    from scipy import signal
    resampled_data = [signal.resample(sample,num_samples) 
                      for sample in data_df]
    data_df['resampled data'] = resampled_data
    return data_df



