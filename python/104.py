import time
import random

f = open('danezadanie104.txt', 'r')
my_list = f.read()
f.close()
A = ''.join(my_list)
A = A.split('\n')
B = ''.join(my_list)
B = B.split('\n')
C = ''.join(my_list)
C = C.split('\n')


# Bubble Sort
def bubbleSort(A):
    poczatek = time.time()
    for i in range(len(A) - 1):
        for j in reversed(range(i + 1, len(A))):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    koniec = time.time() - poczatek
    return koniec


czasBubble = bubbleSort(A)
file1 = open('wyjscieBubble104.txt', 'w')
for i in range(len(A)):
    file1.write(A[i] + '\n')
file1.close()


# InsertSort
def insertSort(B):
    poczatek = time.time()
    for j in range(1, len(B)):
        klucz = B[j]
        i = j - 1
        while i >= 0 and B[i] > klucz:
            B[i + 1] = B[i]
            i -= 1
        B[i + 1] = klucz

    koniec = time.time() - poczatek
    return koniec


czasInsert = insertSort(B)
file2 = open('wyjscieInsert104.txt', 'w')
for i in range(len(B)):
    file2.write(B[i] + '\n')
file2.close()


# QuickSort
def partition(A, p, k):
    x = A[k]
    i = p - 1
    for j in range(p, k):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[k], A[i + 1] = A[i + 1], A[k]
    return i + 1


def quicksort(A, p, k):
    if p < k:
        q = partition(A, p, k)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, k)


start = time.time()
quicksort(C, 0, 4)
koniecQ = time.time() - start
file3 = open('wyjscieQuick104.txt', 'w')
for i in range(len(C)):
    file3.write(C[i] + '\n')
file3.close()