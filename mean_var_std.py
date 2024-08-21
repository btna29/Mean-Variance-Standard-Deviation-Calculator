import numpy as np 

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.reshape(list, (3,3))

    calculations = {}

    calculations['mean'] = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix.flatten()).tolist()]
    calculations['variance'] = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix.flatten()).tolist()]
    calculations['standard deviation'] = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix.flatten()).tolist()]
    calculations['max'] = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix.flatten()).tolist()]
    calculations['min'] = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix.flatten()).tolist()]
    calculations['sum'] = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix.flatten()).tolist()]

    return calculations