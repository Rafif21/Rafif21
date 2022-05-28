from os import system
import msvcrt
import random
class InfoKursi:
    def __init__(self):
        self.nokursi = [None]*8
        self.statuskursi = [0]*8
        self.pesan = {
            "nama" : [None]*8,
            "ID" : [None]*8,
            "kode" : [None]*8
        }

class Gerbong:
    def __init__(self, ngb):
        self.ngb = ngb
        self.gb = InfoKursi()
        self.next = None
        self.prev = None
    
    def Initiate(self):
        grb = self.gb
        i = 0
        while(i<8):
            grb.nokursi[i] = i+1
            i = i + 1
        Gerbong.printout(self)
        return grb
    
    def printout(self):
        grb = self.gb
        i = 0
        while(i<8):
            if(i == 4):
                print("\n")
            print(grb.nokursi[i], "-", grb.statuskursi[i], end="")
            print(end = "  ")
            i = i + 1
        print("\n\n")
    
    def traversment(self):
        node = self
        ngb = 1
        while(node!=None):
            print("Gerbong-", node.ngb)
            Gerbong.Initiate(node)
            node = node.next

gb1 = Gerbong(1)
gb2 = Gerbong(2)
gb3 = Gerbong(3)
gb1.next = gb2
gb2.prev = gb1
gb2.next = gb3
list = gb1

def subprocess():
    _ = system('cls')

def launch():
    subprocess()
    list.traversment()
    print("Input anykey to back ")
    subm = msvcrt.getch()
    main()

def pesan(gnb):
    ps = [None]*4
    if(gnb == 1):
        grb = gb1
    elif(gnb == 2):
        grb = gb2
    elif(gnb == 3):
        grb = gb3
    else:
        pesan()
    no = int(input("No.Kursi : "))
    grb.gb.pesan["nama"][no-1] = input("Atas nama \t: ")
    grb.gb.pesan["ID"][no-1] = int(input("ID \t\t: "))
    grb.gb.statuskursi[no-1] = 1
    i = 0
    while(i<4):
        ps[i] = random.randint(0,9)
        i = i + 1
    grb.gb.pesan["kode"][no-1] = ps
    subprocess()
    print("Pemesanan Berhasil")
    print("Atas Nama \t: ",grb.gb.pesan["nama"][no-1])
    print("Kode Pemesanan \t: ", end="") 
    for i in grb.gb.pesan["kode"][no-1]:
        print(i, end="")
    print("\n")
    print("Input anykey to back ")
    subm = msvcrt.getch()
    main()

def canceling(gnb, ps):
    found = False
    a = 0
    if(gnb == 1):
        grb = gb1
    elif(gnb == 2):
        grb = gb2
    elif(gnb == 3):
        grb = gb3
    else:
        main()
    while(found!=True):
        if(grb.gb.pesan["kode"][a]==ps):
            found = True
            grb.gb.pesan["nama"][a] = None
            grb.gb.pesan["ID"][a] = None
            grb.gb.pesan["kode"][a] = None
            grb.gb.statuskursi[a] = 0
            print(">> Pesanan Berhasil dibatalkan")
        else:
            a = a + 1
    main()
    

def main():
    subprocess()
    print("-----Ticketing Machine----")
    print("Menu : \n1. See Availabel Chair\n2. Buy Ticket\n3. Canceling Order")
    print("4. Print Out Ticket (Comming Soon)\n5. Exit")
    menu = int(input(">> "))
    if menu == 1:
        launch()
    elif menu == 2:
        subprocess()
        print("-----Pemesanan-----")
        gnb = int(input("Gerbong [1-3] \t: "))
        pesan(gnb)
    elif menu == 3:
        subprocess()
        b = input("Are you sure [y/n] ? ")
        if(b =='n'or b =='N'):
            main()
        subprocess()
        print("-----Pembatalan-----")
        gnb = int(input("Gerbong \t: "))
        psn = input("Kode Pemesanan : ")
        ps = []
        for i in psn:
            ps.append(int(i))
        canceling(gnb, ps)
    elif menu == 5:
        exit
    else :
        main()
    return 0

if __name__ == '__main__':
    main()
