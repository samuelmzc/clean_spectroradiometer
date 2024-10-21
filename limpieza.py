import os
import numpy as np
import matplotlib.pyplot as plt

# Tipos de superficies
types = ["adelfas", "asfalto_seco", "cesped_seco", "cesped", "charco", "cos_blanca", "flor_adelfas", 
         "hoja_roja", "hortensia_azul", "minusvalido", "musgo", "palmerita", "romero", "tronco_humedo",
         "tronco_romero"]

# Se crea la lista con cada uno de los archivos del directorio
data_path = "data/medidas_20241016"
directorio = os.listdir(data_path)

# Algunos datos de importancia
n_files_pertype = 20
wavelength_start = 350
wavelength_end = 2500
wavelength_range = wavelength_end - wavelength_start
wavelength_space = np.linspace(wavelength_start, wavelength_end, wavelength_range + 1)


def mean_wavelenght(type_):
    """
    Calcula la media de la firma espectral dado un tipo de superficie.

    Argumentos:
    type_ -- str elemento de la lista types

    Devuelve:
    mean_wavelength -- array promedio de longitudes de onda
    """
    
    type_array = np.zeros(wavelength_range + 1)
    std = np.zeros(wavelength_range + 1)
    for file_ in directorio:
        root = data_path + "/" + file_
        if file_[:(len(type_))] == type_:
            local_wavelengths = np.loadtxt(root, unpack = True, usecols = 1, skiprows = 1)
            type_array += local_wavelengths
    
    mean_wavelenght = type_array/n_files_pertype

    for file_ in directorio:
        root = data_path + "/" + file_
        if file_[:(len(type_))] == type_:
            local_wavelengths = np.loadtxt(root, unpack = True, usecols = 1, skiprows = 1)
            std += (local_wavelengths - mean_wavelenght)**2
    
    std = np.sqrt(std/len(std))


    return mean_wavelenght, std


# Se crea un diccionario que contiene los arrays para cada superficie
wavelength_dict = {}
std = {}
for type_ in types:
    wavelength_dict[type_], std[type_] = mean_wavelenght(type_)


# A las bandas de absorción de agua les asignamos valor el valor nan
absortionband_1 = np.arange(1350, 1460, 1)
absortionband_2 = np.arange(1760, 2100, 1)
absortionband_3 = np.arange(2360, 2502, 1)



for type_ in types:
    for i in range(len(wavelength_dict[type_])):
        if (351 + i in absortionband_1) or (351 + i in absortionband_2) or (351 + i in absortionband_3):
            wavelength_dict[type_][i] = float("NaN")
            #std[type_][i] = float("NaN")

