#include <iostream>
#include <fstream>
#include <string>
using namespace std;
// command untuk compile
// g++ main.cpp -o ../bin/main.exe

int main() {
    cout << "Metode input:" << endl;
    cout << "1. Input file (.txt)" << endl;
    cout << "2. Input CLI" << endl;
    cout << "Pilih metode:" << endl;
    int opsi;
    cin >> opsi;
    while(opsi != 1 && opsi != 2){
        cout << "Masukkan 1 atau 2!!" << endl;
        cin >> opsi;
    }
    if(opsi == 1){
        cout << "Masukkan nama file:" << endl;
        string nameFile;
        cin >> nameFile;
        cout << "Membaca file ..." << endl;
        ifstream file(nameFile);
        string myText;
        // while(getline(file, myText)){
        //     cout << myText << endl;
        // }
        string strBuffer;
        getline(file, strBuffer); 
        int nBuffer = stoi(strBuffer);

        string sizeMatrix;
        getline(file, sizeMatrix); 
        int tempNum = 0;
        int xMatrix, yMatrix;
        for(int i = 0; i < sizeMatrix.length(); i++){
            if(sizeMatrix[i] == 32){
                xMatrix = tempNum;
                tempNum = 0;
            }else{
                tempNum *= 10;
                tempNum += (sizeMatrix[i])-48;
            }
        }
        yMatrix = tempNum;

        string mainMatrix[yMatrix][xMatrix];
        for(int i = 0; i < yMatrix; i++){
            string tempRow;
            getline(file, tempRow); 
            for(int j = 0; j < xMatrix; j++){
                mainMatrix[i][j] = tempRow[3*j];
                mainMatrix[i][j] += tempRow[3*j+1];
            }
        }
        string strNSeq;
        getline(file, strNSeq); 
        int nSeq = stoi(strNSeq);
        for(int i = 0; i < nSeq; i++){
            string strSeq;
            getline(file, strSeq); 
            
        }
    }else{
        int nToken, nBuffer, xMatrix, yMatrix, nSeq, lenSeq;
        cin >> nToken;
        string token[nToken];
        for(int i = 0; i < nToken; i++){
            string tempToken;
            cin >> tempToken;
            token[i] = tempToken;
        }
        cin >> nBuffer;
        cin >> xMatrix;
        cin >> yMatrix;
        cin >> nSeq;
        cin >> lenSeq;
    }
}