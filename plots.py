import numpy as np
import matplotlib.pyplot as plt
from limpieza import *
from wv_data import *

vegetacion1 = ["adelfas", "flor_adelfas", "romero", "cesped", "cesped_seco", "hoja_roja"]
vegetacion2 = ["hortensia_azul", "musgo", "palmerita", "tronco_humedo", "tronco_romero"]
suelos =["asfalto_seco", "charco", "cos_blanca", "minusvalido"]




def raw_plot(rows = 3, columns = 5):
    """
    Todas las gráficas de todas las superficies, ya pre procesadas
    """

    fig, axs = plt.subplots(rows, columns)

    for i in range(rows):
        for j in range(columns):
            idx = columns * i + j
            axs[i, j].plot(wavelength_space, wavelength_dict[types[idx]])
            axs[i, j].set_ylim(0, 1)
            axs[i, j].set_title(types[idx])
        
    plt.tight_layout()

def plot_ordered_type(ordered):
    """
    Gráficas con las superficies en una lista "ordered"
    """

    for item in ordered:
        plt.errorbar(wavelength_space, wavelength_dict[item], yerr = std[item], color = "gray", alpha = 0.2)
        plt.plot(wavelength_space, wavelength_dict[item], label = item)

    plt.xlabel(r"Longitud de onda $\lambda \ (nm)$ ")
    plt.ylabel(r"Reflectancia")
    plt.legend()
    plt.tight_layout()
    

def plot_vs_wv(ordered):
    """
    Gráficas con la superposición de las bandas del WorldView-2
    """
    fig = plt.figure(figsize=(13, 7))

    for item in ordered:
        plt.plot(wavelength_space, wavelength_dict[item], label = item)
    
    for banda in bands:
        plt.plot(WL, wv_dict[banda], label = banda)
    
    plt.xlabel(r"Longitud de onda $\lambda \ (nm)$ ")
    plt.ylabel("Reflectancia")
    plt.xlim(350, max(WL))
    plt.legend(loc = "upper right")
    plt.tight_layout()
