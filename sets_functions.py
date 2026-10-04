#Здесь хранятся функции для работы с множествами

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