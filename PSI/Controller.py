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

def countRank(arr):
    # Convert the array to a NumPy array
    arr = np.array(arr)

    # Get the indices that would sort the array
    sorted_indices = np.argsort(arr)[::-1]

    # Create an array of ranks
    ranks = np.empty_like(sorted_indices)
    ranks[sorted_indices] = np.arange(1, len(arr) + 1)

    return ranks


def main2():
    array_2d = [
        [0.72826087, 0.67, 1, 0.901098901, 0.825581395, 0.67, 0.8, 0.75, 0.5, 0.875, 0.7, 1, 0.397590361, 1],
        [1, 0.67, 0.715909091, 1, 0.744186047, 0.67, 0.7, 0.69, 0.5, 0.875, 1, 0.807228916, 0.492537313, 1],
        [0.902173913, 0.67, 0.715909091, 1, 0.825581395, 0.83, 0.8, 0.75, 0.67, 0.7, 0.7, 1, 0.66, 1],
        [0.72826087, 0.67, 1, 0.901098901, 0.825581395, 0.67, 0.8, 0.75, 0.5, 0.875, 0.7, 1, 0.397590361, 1],
        [1, 0.67, 0.715909091, 1, 0.744186047, 0.67, 0.7, 0.69, 0.5, 0.875, 1, 0.807228916, 0.492537313, 1],
        [0.72826087, 0.83, 1, 1, 1, 0.83, 0.8, 0.69, 0.5, 0.875, 1, 0.807228916, 1, 0.746268657],
        [0.72826087, 0.83, 1, 0.747252747, 1, 0.83, 0.7, 0.69, 0.5, 0.875, 1, 0.807228916, 1, 0.746268657],
        [1, 0.67, 0.715909091, 1, 1, 0.83, 0.8, 0.69, 0.5, 0.875, 1, 0.807228916, 1, 0.746268657],
        [0.72826087, 0.67, 0.715909091, 0.802197802, 0.918604651, 1, 1, 0.63, 0.67, 0.7, 1, 1, 0.492537313, 0.862068966],
        [0.902173913, 0.67, 0.715909091, 0.901098901, 0.825581395, 0.67, 0.9, 0.88, 0.67, 1, 0.7, 0.807228916, 0.397590361, 0.746268657],
        [0.902173913, 0.67, 0.715909091, 0.802197802, 0.825581395, 0.83, 0.8, 0.75, 0.67, 0.7, 0.7, 1, 0.66, 0.666666667],
        [0.815217391, 0.67, 0.568181818, 0.901098901, 0.825581395, 0.67, 0.6, 0.75, 0.67, 0.875, 0.7, 0.807228916, 0.397590361, 1],
        [1, 0.67, 0.715909091, 1, 0.744186047, 0.67, 0.7, 0.69, 0.5, 0.875, 1, 0.807228916, 0.492537313, 1],
        [0.815217391, 0.67, 0.715909091, 0.901098901, 0.918604651, 1, 0.7, 0.75, 0.67, 0.7, 1, 1, 0.397590361, 0.746268657],
        [0.902173913, 0.67, 1, 0.802197802, 0.918604651, 0.83, 0.7, 0.75, 0.67, 1, 0.875, 1, 0.397590361, 0.862068966],
        [1, 0.67, 0.715909091, 1, 0.744186047, 0.67, 0.7, 0.69, 0.5, 0.875, 1, 0.807228916, 0.492537313, 1],
        [0.902173913, 0.92, 0.715909091, 0.846153846, 0.825581395, 0.67, 0.7, 0.69, 0.67, 1, 1, 0.807228916, 0.33, 0.666666667],
        [0.815217391, 1, 0.715909091, 0.901098901, 0.918604651, 1, 1, 1, 0.67, 0.7, 0.7, 0.67, 0.33, 0.862068966],
        [1, 0.83, 0.715909091, 1, 1, 0.67, 0.8, 0.88, 1, 0.875, 0.7, 0.67, 0.33, 0.666666667],
        [1, 0.92, 1, 0.945054945, 1, 0.83, 0.8, 0.81, 0.83, 0.875, 0.875, 1, 0.66, 0.666666667],
        [0.902173913, 0.67, 0.715909091, 1, 0.825581395, 0.83, 0.8, 0.75, 0.67, 0.7, 0.7, 1, 0.66, 0.666666667],
        [0.72826087, 0.67, 1, 0.901098901, 0.825581395, 0.67, 0.8, 0.75, 0.5, 0.875, 0.7, 1, 0.397590361, 1],
        [0.815217391, 1, 0.715909091, 0.901098901, 0.918604651, 1, 1, 0.75, 0.67, 1, 1, 1, 0.492537313, 0.862068966],
        [1, 0.67, 0.715909091, 0.901098901, 1, 0.67, 0.8, 0.75, 1, 0.875, 0.7, 0.67, 0.397590361, 0.602409639],
        [0.815217391, 1, 0.715909091, 0.901098901, 0.918604651, 0.67, 0.8, 0.88, 0.67, 0.7, 1, 0.807228916, 0.492537313, 0.862068966],
        [1, 0.67, 0.715909091, 1, 0.744186047, 0.67, 0.7, 0.88, 0.5, 0.875, 1, 0.807228916,0.492537313,1],
        [0.72826087, 0.67, 0.715909091, 0.901098901, 0.825581395, 0.75, 0.8, 0.75, 0.67, 0.875, 0.7, 0.807228916, 0.397590361, 0.666666667],
        [0.815217391, 0.75, 0.852272727, 0.802197802, 0.825581395, 0.67, 0.8, 0.75, 0.67, 0.875, 1, 0.807228916, 0.397590361, 1],
        [0.902173913, 0.67, 0.568181818, 1, 0.825581395, 1, 0.9, 0.88, 0.83, 0.7, 0.7, 0.807228916, 0.397590361, 0.602409639],
        [0.72826087, 0.67, 0.715909091, 0.802197802, 0.825581395, 0.92, 0.9, 0.88, 0.67, 1, 0.777777778, 0.807228916, 0.397590361, 0.746268657],
        [0.902173913, 0.67, 0.715909091, 1, 0.825581395, 0.83, 0.8, 0.75, 0.67, 0.7, 0.7, 1, 0.66, 0.666666667]
    ]
    normalisasi= np.array(array_2d)

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
              
print(main2())