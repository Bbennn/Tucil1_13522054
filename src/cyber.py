import random
import time
import os

### Input data
## Pilih metode input
print("Metode input:")
print("1. Input file (.txt)")
print("2. Input CLI")
print("Pilih metode:" )
opsi = int(input())
while(opsi != 1 and opsi != 2):
    print("Masukkan 1 atau 2!")
    opsi = int(input())
print("=======================================")
if(opsi == 1):
    # Input lewat teks
    print("Masukkan path file dengan lengkap!")
    print("Contoh:")
    print("C:\Kuliah\Tingkat 2\Semester 4\Stima\Tucil1_13522054\src\input.txt")
    print("Path file: ")
    namaFile = str(input())
    while(not os.path.isfile(namaFile)):
        print("FILE TIDAK DITEMUKAN!!!")
        print("=======================================")
        print("Masukkan path file dengan lengkap!")
        print("Contoh:")
        print("C:\Kuliah\Tingkat 2\Semester 4\Stima\Tucil1_13522054\src\input.txt")
        print("Path file: ")
        namaFile = str(input())
    print("Membaca file ...")
    test = ""
    f = open(namaFile, "r")
    for x in f:
        test += x
    f.close()
    test = test.split("\n")
    nBuffer = int(test[0])
    print(nBuffer)
    test.remove(str(nBuffer))

    sizeMatrix = str(test[0])
    test.remove(str(sizeMatrix))
    sizeMatrix = sizeMatrix.split(" ")
    xMatrix = int(sizeMatrix[0])
    yMatrix = int(sizeMatrix[1])
    print(xMatrix)
    print(yMatrix)

    mainMatrix = []
    for i in range(yMatrix):
        temp = test[0]
        test.remove(temp)
        temp = temp.split(" ")
        mainMatrix.append(temp)
    print(mainMatrix)

    nSeq = int(test[0])
    print(nSeq)
    test.remove(str(nSeq))

    seqs = []
    bonus = []
    for i in range(nSeq):
        temp = test[0]
        test.remove(temp)
        temp = temp.split(" ")
        seqs.append(temp)
        temp = test[0]
        test.remove(temp)
        bonus.append(int(temp))
    print(seqs)
    print(bonus)
else:
    # Input dari CLI
    print("Masukkan command dengan format:")
    print("jumlah_token_unik")
    print("token")
    print("ukuran_buffer")
    print("ukuran_matriks")
    print("jumlah_sekuens")
    print("ukuran_maksimal_sekuens")
    print("")
    print("Contoh:\n5\nBD 1C 7A 55 E9\n7\n6 6\n3\n4")
    print("")
    nToken = int(input())
    tokens = str(input())
    tokens = tokens.split(" ")
    nBuffer = int(input())
    sizeMatrix = str(input())
    sizeMatrix = sizeMatrix.split(" ")
    nSeq = int(input())
    lenSeq = int(input())
    print("debug")
    print(nToken)
    print(tokens)
    print(nBuffer)
    print(sizeMatrix)
    print(nSeq)
    print(lenSeq)


### Fungsi-fungsi
result = []

def convertPoint(arr):
    # merubah buffer translasi menjadi point buffer
    temp = [0,0]
    points = []
    for i in range(len(arr)):
        if(i % 2 == 0):
            temp[0] += arr[i]
            temp[0] %= xMatrix
        else:
            temp[1] += arr[i]
            temp[1] %= yMatrix
        points.append(temp.copy()) # biar temp di points tidak diganggu
    return points

def isCorrectBuffer(buffer):
    # mengecek apakah points buffer adalah sebuah set
    tempBuffer = []
    for i in range(len(buffer)):
        if(buffer[i] in tempBuffer):
            pass
        else:
            tempBuffer.append(buffer[i])
    return len(buffer) == len(tempBuffer)

def convertBuffer(arr):
    # mengubah points buffer menjadi token buffer
    tokenBuffer = []
    for point in (arr):
        tokenBuffer.append(mainMatrix[point[1]][point[0]])
    return tokenBuffer

def subBuffer(sub, main):
    # check sebuah seq adalah sub-buffer (bagian dari buffer)
    sub = " ".join(sub)
    main = " ".join(main)
    return sub in main

fileOut = open("hasil1.txt", "w")
def makeBuffer(digit, lenBuffer, buffer, slot):
    # membuat buffer
    if digit == lenBuffer:
        points = convertPoint(buffer)
        if(isCorrectBuffer(points)):
            tokens = convertBuffer(points)
            if(subBuffer(seqs[1],tokens) and subBuffer(seqs[2],tokens)):
                fileOut.write(" ".join(map(str, points)) + "\n")
                fileOut.write(" ".join(map(str, tokens)) + "\n")
    else:
        if (digit == 0):
            for i in range(slot[digit]):
                buffer[digit] = i
                makeBuffer(digit + 1, lenBuffer, buffer,slot)
        else:
            for i in range(1,slot[digit]):
                buffer[digit] = i
                makeBuffer(digit + 1, lenBuffer, buffer,slot)


### Memproses fungsi dan output
buffer = [0] * nBuffer  # Initialize loop counters
slot = []
for i in range(nBuffer):
    if(i % 2 == 0):
        slot.append(xMatrix)
    else:
        slot.append(yMatrix)

start = time.time() # Waktu awal
makeBuffer(0, nBuffer, buffer, slot) 
fileOut.close()
end = time.time() # waktu akhir
print("The time of execution of above program is: ",(end-start) * 10**3, "ms")


### Exit
print("Press enter to exit")
input() #agar program tidak tertutup

# Notes:
# 1. Belum handle optimasi untuk pembangkit acak
# 2. Belum handle kasus nBuffer < nMaxBuffer (belum optimal)
# 3. Koordinatnya belum benar (perlu ditambah (1, 1))
# 4. Output ke file belum finish


# Untuk testcase
'''
C:\Kuliah\Tingkat 2\Semester 4\Stima\Tucil1_13522054\src\1.txt
'''