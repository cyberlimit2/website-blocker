# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:05:36 2020
@author: DELL
"""



import csv

import os
namafile = 'menu_makanan.csv'


def inputdaftarmenu():
    kodemenu = int(input("Masukkan Kode Menu : "))
    namamenu = input("Masukkan Nama Menu: ")
    hargamenu = int(input("Harga Menu: "))
     
    csvheader = ['Kode', 'Menu', 'Harga']


    with open(namafile, 'a', newline='\n') as filecsv:


        dictmenu = {'Kode': kodemenu, 'Menu': namamenu, 'Harga': hargamenu}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)


        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
        
        writer.writerow(dictmenu)

def cekdaftarmenu():
    with open (namafile) as filecsv:
        readCSV = csv.reader (filecsv,delimiter = ',')
        line_count = 0
    
        for row in readCSV:
            if line_count == 0:
                print (f"Nama Kolom: \n{row}")
                line_count += 1
        
            else:
                line_count += 1
                print (row)
                jmldata = int(line_count - 1)
        print ("Jumlah Daftar Menu: ", jmldata)     
        
def programkasir():
    with open(namafile, newline='') as filecsv:
        reader = csv.reader(filecsv)
        datamenu = list(reader)

    cekdaftarmenu()
    totalharga = 0
    listjmlpesan= []
    print ("")
    print ("Masukkan KODE berikut pada Kode Makanan untuk:")
    print ("Input (1) untuk TOTAL PEMBAYARAN")
    print ("Input (2) untuk Melayani pembeli baru/Keluar dari Program Kasir")
    print ("")
    pilihanmenu = input("Kode makanan dipesan: ")
    while pilihanmenu != ("2"):
        match = 0
        for i in datamenu:
            if pilihanmenu == i[0]:
                match += 1
                try:
                    jml_pesan = int(input("Jumlah dipesan: "))
                except ValueError:
                    print ("Input salah. Masukkan jumlah pesanan")
                    jml_pesan = int(input("Jumlah dipesan: "))
                hargamenu = int(i[2])*jml_pesan
                totalharga += hargamenu
                print (i[1],"\t Rp",hargamenu)
                entry = [i[1], jml_pesan,hargamenu]
                
                listjmlpesan.append(entry)
                print (listjmlpesan)
                
        if pilihanmenu == "1":
            match += 1
            print ("Total Pembelian: Rp ", totalharga)
            uangbayar = int(input("Masukkan uang dari pembeli: Rp "))
            uangkembalian = uangbayar - totalharga
            if uangbayar < totalharga:
                print ("UANG TIDAK CUKUP")
                
            else:
                uangkembalian = uangbayar - totalharga
                print ("Uang kembalian: Rp ", uangkembalian)
                print ("")
            print("\n===================================")
            print("===============N O T A=============")
            print("===================================")
            print("Pesanan :".format(len(listjmlpesan)))
            
            for pesanan in listjmlpesan:
                print (pesanan)
            print("Total     : Rp ", totalharga)
            print("Uang      : Rp ", uangbayar)
            print("Kembalian : Rp ",uangkembalian)
            print("====== Selamat Datang Kembali======")
            print("===================================")   
        if match == ("a"):
            print ("Input salah, ulangi input")
        pilihanmenu = input("Kode makanan dipesan: ")
    
    print ("Melayani pembeli baru? ")
    print ("Klik (1) YA")
    print ("Klik (2) TIDAK")
    ulangkasir = input("> ")
    if ulangkasir == ("1"):
        programkasir()
        
    elif ulangkasir == ("2"):
        None
        
while True:
    print("================================================")
    print("=============PROGRAM KASIR RESTORAN=============")
    print("======RESTORAN MURAH MERIAH PAS DI KANTONG======")
    print("================================================")
    print("======SILAKAN PILIH SEBELUM MASUK PROGRAM=======")
    print("")
    print("           Klik (1) Program Kasir               ")
    print("           Klik (2) Menambah Menu               ")
    print("           Klik (3) Tampilkan Menu              ")
    print("           Klik (4) Keluar Program              ")
    mulai = input("> ")
    if mulai == ("1"):
        print("================================================")
        print("=============PROGRAM KASIR RESTORAN=============")
        print("======RESTORAN MURAH MERIAH PAS DI KANTONG======")
        print("================================================")
        print("                  PROGRAM KASIR                 ")
        print("")
        programkasir()

    elif mulai == ("2"):
        print("================================================")
        print("=============PROGRAM KASIR RESTORAN=============")
        print("======RESTORAN MURAH MERIAH PAS DI KANTONG======")
        print("================================================")
        print("              MENAMBAH DAFTAR MENU              ")                      
        print("")
        inputdaftarmenu()
        
    elif mulai == ("3"):
        print("================================================")
        print("=============PROGRAM KASIR RESTORAN=============")
        print("======RESTORAN MURAH MERIAH PAS DI KANTONG======")
        print("================================================")
        print("            MENAMPILKAN DAFTAR MENU             ")
        print("")
        cekdaftarmenu()
        
    elif mulai == ("4"):
        print ("")
        print ("PROGRAM TERHENTI!")
        print ("")
        break
        
    else:
        print ("")
        print ("Input SALAH!")
        print ("PROGRAM TERHENTI!")
        print ("")
        break