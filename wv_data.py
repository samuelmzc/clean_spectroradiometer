import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = "data/medidas_20241016/WV2.txt"
WL, WV2CB, WV2B, WV2G, WV2Y, WV2R, WV2RE, WV2NIR1, WV2NIR2 = np.loadtxt(data_path, unpack = True, skiprows=1)

wv_dict = {
    "WV2CB" : WV2CB,
    "WV2B" : WV2B,
    "WV2G" : WV2G,
    "WV2Y" : WV2Y,
    "WV2R" : WV2R,
    "WV2RE" : WV2RE,
    "WV2NIR1" : WV2NIR1,
    "WV2NIR2" : WV2NIR2
}

bands = []
for name, _ in wv_dict.items():
    bands.append(name)

n_bands = len(bands)
"""
for band in bands:
    plt.plot(WL, wv_dict[band], label = band)"""

