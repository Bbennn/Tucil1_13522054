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
        print("C:\Kuliah\Tingkat 2\Semester 4\Stima\Tucil1_13522054\test\input.txt")
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
    test.remove(str(nBuffer))

    sizeMatrix = str(test[0])
    test.remove(str(sizeMatrix))
    sizeMatrix = sizeMatrix.split(" ")
    xMatrix = int(sizeMatrix[0])
    yMatrix = int(sizeMatrix[1])

    mainMatrix = []
    for i in range(yMatrix):
        temp = test[0]
        test.remove(temp)
        temp = temp.split(" ")
        mainMatrix.append(temp)

    nSeq = int(test[0])
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
    # print("debug")
    # print(nBuffer)
    # print(xMatrix)
    # print(yMatrix)
    # print(mainMatrix)
    # print(nSeq)
    # print(seqs)
    # print(bonus)
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
    xMatrix = int(sizeMatrix[0])
    yMatrix = int(sizeMatrix[1])
    nSeq = int(input())
    lenSeq = int(input())
    mainMatrix = []
    for i in range(yMatrix):
        temp = []
        for j in range(xMatrix):
            temp.append(random.choice(tokens))
        mainMatrix.append(temp)
    seqs = []
    bonus = []
    for i in range(nSeq):
        temp = []
        for j in range(random.randint(2,lenSeq)):
            temp.append(random.choice(tokens))
        seqs.append(temp)
        bonus.append(random.randint(-100,100))
    # print("debug")
    # print(nToken)
    # print(tokens)
    # print(nBuffer)
    # print(sizeMatrix)
    # print(nSeq)
    # print(lenSeq)
    print("Matriks: ")
    for i in range(yMatrix):
        print(" ".join(mainMatrix[i]))
    print("Sequences beserta bonusnya:")
    for i in range(nSeq):
        print(" ".join(seqs[i]))
        print(bonus[i])
    print("")

resultPoints = []
resultTokens = []
resultBonus = 0
### Fungsi-fungsi

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

def findBonus(seqs, bonus, bufferPoints):
    result = 0
    for i in range(len(seqs)):
        if(subBuffer(seqs[i], bufferPoints)):
            result += bonus[i]
    return result

def subBuffer(sub, main):
    # check sebuah seq adalah sub-buffer (bagian dari buffer)
    sub = " ".join(sub)
    main = " ".join(main)
    return sub in main

def makeBuffer(digit, lenBuffer, buffer, slot):
    # membuat buffer
    if digit == lenBuffer:
        points = convertPoint(buffer)
        if(isCorrectBuffer(points)):
            tokens = convertBuffer(points)
            tempBonus = findBonus(seqs, bonus, tokens)
            # print(tempBonus)
            global resultBonus
            global resultPoints 
            global resultTokens 
            if(tempBonus > resultBonus):
                resultPoints = points
                resultTokens = tokens
                resultBonus = tempBonus
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
start = time.time() # Waktu awal
for x in range(nBuffer):
    buffer = [0] * (x+1)  # Initialize loop counters
    slot = []
    for i in range(x+1):
        if(i % 2 == 0):
            slot.append(xMatrix)
        else:
            slot.append(yMatrix)

    makeBuffer(0, x+1, buffer, slot)
end = time.time() # waktu akhir

# Output CLI
print("Result: ")
print(resultBonus)
print(" ".join(resultTokens))
for i in range(len(resultPoints)):
    temp = resultPoints[i].copy()
    temp[0] += 1
    temp[1] += 1
    print(temp)
print("Time: ",(end-start) * 10**3, "ms")

# Output file
print("Apakah ingin menyimpan solusi? (y/n)")
keluar = str(input())
while(keluar != 'y' and keluar != 'n'):
    print("Masukkan y atau n!")
    keluar = str(input())
if(keluar == 'y'):
    fileOut = open("hasil.txt", "w")
    if(opsi == 2):
        fileOut.write("Matriks: ")
        fileOut.write("\n")
        for i in range(yMatrix):
            fileOut.write(" ".join(mainMatrix[i]))
            fileOut.write("\n")
        fileOut.write("Sequences beserta bonusnya:")
        fileOut.write("\n")
        for i in range(nSeq):
            fileOut.write(" ".join(seqs[i]))
            fileOut.write("\n")
            fileOut.write(str(bonus[i]))
            fileOut.write("\n")
    fileOut.write("")
    fileOut.write("Result: ")
    fileOut.write("\n")
    fileOut.write(str(resultBonus))
    fileOut.write("\n")
    fileOut.write(" ".join(resultTokens))
    fileOut.write("\n")
    for i in range(len(resultPoints)):
        temp = resultPoints[i].copy()
        temp[0] += 1
        temp[1] += 1
        fileOut.write(str(temp))
        fileOut.write("\n")
    duration = "Time: " + str((end-start) * 10**3) + " ms"
    fileOut.write(duration)   
    fileOut.close()
    print("File disimpan dengan nama hasil.txt")
### Exit
print("Press enter to exit")
input() #agar program tidak tertutup

# Notes:
# 1. Ada beberapa input dari user yang pasti benar
