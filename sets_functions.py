#Здесь хранятся функции для работы с множествами

def check_univers(A, B, U):
    new_A = [A[i] for i in range(len(A)) if A[i] in U]
    new_B = [B[i] for i in range(len(B)) if B[i] in U]

    A[:] = new_A
    B[:] = new_B



A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
U = [1, 2, 5, 6]

check_univers(A, B, U)

print(f"A: {A}")
print(f"B: {B}")