import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())

from Vnet.model_attention_vnet3d import AttenGatVnet3dModule
import numpy as np
import pandas as pd


def attengantrain():
    '''
    Preprocessing for dataset
    '''
    # Read  data set (Train data from CSV file)
    csvdata = pd.read_csv('dataprocess\\data/trainSegmentation.csv')
    maskdata = csvdata.iloc[:, 1].values
    imagedata = csvdata.iloc[:, 0].values
    # shuffle imagedata and maskdata together
    perm = np.arange(len(imagedata))
    np.random.shuffle(perm)
    imagedata = imagedata[perm]
    maskdata = maskdata[perm]

    AttenGatVnet3d = AttenGatVnet3dModule(256, 256, 16, channels=1, costname=("tversky_loss",))
    AttenGatVnet3d.train(imagedata, maskdata, "AttenGatVnet3d.pd", "log\\attengatsegmeation\\tversky_loss\\", 0.001,
                         0.5, 10, 1)


attengantrain()
