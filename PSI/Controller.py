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

def countRank(matrix):
    # Membuat salinan array 2D asli
    matrix_copy = np.array(matrix)

    # Menggunakan argsort untuk mendapatkan indeks dari nilai terurut
    sorted_indices = np.argsort(matrix_copy.ravel())[::-1]

    # Membuat array 2D untuk menyimpan rank
    rank_matrix = np.unravel_index(sorted_indices, matrix_copy.shape)

    # Increment untuk mengubah dari indeks (dimulai dari 0) menjadi rank (dimulai dari 1)
    rank_matrix = np.array(rank_matrix) + 1

    return rank_matrix

def main(array):
    # konversi ke numpy
    normalisasi = toNumpy(array)#tolist
    # menghitung rata rata
    averages = average(normalisasi)
    # menghitung variansi preverensi
    varians = variansiPreferensi(normalisasi, averages)#tolist
    vSum = simpangan(varians)#tolist
    weight = priorityWeight(vSum)#tolist
    # menghitung simpangan nilai preferensi
    # menghitung nilai tiap alternatif
    result = countResult(normalisasi, weight)#tolist
    # menghitung perangkingan
    hSum = horizontalSum(result)
    
    rank= countRank(hSum)
    # Merubah return statement menjadi dictionary dengan key "normalisasi"
    return {"normalisasi": normalisasi.tolist(), 
            "averages": averages.tolist(), 
            "varians": varians.tolist(), 
            "vSum": vSum.tolist(), 
            "weight": weight.tolist(), 
            "result": result.tolist(),
            "hSum": hSum,
            "rank": rank.tolist()
            }
            
            
