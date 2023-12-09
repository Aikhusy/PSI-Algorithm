import pandas as pd
import numpy as np

np.set_printoptions(precision=4, suppress=True)

def toList(npArray):
    return npArray.tolist()

def verticalSum(array):
    return np.sum(array,axis=0)

def horizontalSum(array):
    sum=np.sum(array,axis=1)
    return sum.tolist()

def toNumpy(array):
    return np.array(array)

def average (array):
    return np.mean(array,axis=0)

def variansiPreferensi(normArray, avgArray):
    
    variansi_array = np.abs(normArray - avgArray) ** 2

    return variansi_array

def simpangan(array):
    vSum= verticalSum (array)
    s= 1-vSum

    return s 

def priorityWeight(array):
    hSum=np.sum(array)
    weight = array/hSum

    return weight

def countResult(array, priorityWeight):
    result = array * priorityWeight

    return result

def main(array):
    # konversi ke numpy
    normalisasi = toNumpy(array)
    # menghitung rata rata
    averages = average(normalisasi)
    # menghitung variansi preverensi
    varians = variansiPreferensi(normalisasi, averages)
    vSum = simpangan(varians)
    weight = priorityWeight(vSum)
    # menghitung simpangan nilai preferensi
    # menghitung nilai tiap alternatif
    result = countResult(normalisasi, weight)
    # menghitung perangkingan
    hSum = horizontalSum(result)
    
    # Merubah return statement menjadi dictionary dengan key "normalisasi"
    return {"normalisasi": normalisasi.tolist(), 
            "averages": averages.tolist(), 
            "varians": varians.tolist(), 
            "vSum": vSum.tolist(), 
            "weight": weight.tolist(), 
            "result": result.tolist(), 
            "hSum": hSum.tolist()
            }
