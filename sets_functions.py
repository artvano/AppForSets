def check_univers(A, B, U): #Проверка на универс изменение множеств на удовлетворяющие универсу
    flag_for_A = True
    flag_for_B = True

    new_A = [A[i] for i in range(len(A)) if A[i] in U]
    new_B = [B[i] for i in range(len(B)) if B[i] in U]

    if A != new_A:
        flag_for_A = False

    if B != new_B:
        flag_for_B = False
    
    A[:] = new_A
    B[:] = new_B

    return {
        "flag_for_A": flag_for_A,
        "flag_for_B": flag_for_B
    }


def union(A, B):  #Объединение множеств
    return list(set(A + B))


def intersection(A, B): #Пересечение множеств
    res = []

    for i in A:
        if i in B:
            res.append(i)

    return res 


def simmetry_diff(A, B): #Симметрическая разность
    intersection_1 = intersection(A, B)

    A_for_res = [i for i in A if i not in intersection_1]
    B_for_res = [i for i in B if i not in intersection_1]

    return A_for_res + B_for_res

def diff(A, B):  #Разность 
    return [i for i in A if i not in B]


def addition(A, U):    #Дополнение до универса
    return [i for i in U if i not in A]



I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

X = [2, 4, 6, 8, 10]

print(addition(X, I))