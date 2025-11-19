from worker import Worker

class WorkerManager:
    
    def __init__( self ):
        
        self.workerList = []
    
    def controller( self ):
        
        print( "1. feladat: Fájl beolvasása" )
        readSuccess = self.readFile()
        if( readSuccess ): print( "Sikeres beolvasás\n" )
        
        print( "2. feladat: Dolgozók számlálása")
        workers = self.countWorkers()
        print( "Dolgozók létszáma: {:^10}\n".format( workers ))
        
        print( "3. feladat: Szegedi dolgozók számlálása")
        workersSzegedi = self.countSzeged()
        print( "Szegedi dolgozók létszáma: {:^10}\n".format( workersSzegedi ))
        
        print( "4. feladat: Budapesti dolgozók fizetésének összege")
        salaryBp = self.countBpSalary()
        print( "Budapesti dolgozók fizetésének összege: {:^10,}\n".format( salaryBp ))
        
        print("5. feladat: Legtöbbet kereső ember neve ")
        highestSalaryName, highestSalaryNumber=self.highestSalary()
        print("A legtöbbet kereső ember:{:^10}\n fizetése:{:^10}\n".format(highestSalaryName,highestSalaryNumber))
        
        print("6. feladat: Legtöbbet kereső emberek neve ")
        highestMan = self.highestSalary2()
        for workername in highestMan:
            print("A legtöbbet kereső emberek:{:^10}".format(workername))
            
            
        print( "\n7. feladat: Nem kapott bonuszok száma")
        nobonusMan = self.noBonus()
        print( "Nem kapott bonuszok száma: {:^10,}\n".format( nobonusMan ))
        
        print( "8. feladat: Győri dolgozók fizetésének az átlaga")
        salaryGyoriAverage = self.countGyoriSalary()
        print( "Győri dolgozók fizetésének az átlaga: {:^10.2f}\n".format( salaryGyoriAverage ))
        
        print("9. feladat: Fájlba írni az átlagot")
        print(self.avgGyoriSalary()) 
                
        
    
    def readFile( self ):
        
        file = open( "dolgozok100.txt", "r", encoding="utf8" )
        row = file.readline()
        
        while( row ):
    
            row = file.readline()
            rowSp = row.split( ":" )
            if( len( rowSp ) > 1 ):
            
                worker = Worker( rowSp[ 0 ], rowSp[ 1 ], rowSp[ 2 ], rowSp[ 3 ],
                                rowSp[ 4 ], rowSp[ 5 ], rowSp[ 6 ])
                
                self.workerList.append( worker )
        
        return True      

    def countWorkers( self ):
        
        counter = 0
        for worker in self.workerList:
            
            counter += 1
        
        return counter    
    
    def countSzeged ( self ):
        counter = 0
        for worker in self.workerList:
            if worker.city == "Szeged":
                counter += 1 
        return counter        
    
    def countBpSalary(self):
        bpSalary = 0
        for worker in self.workerList:
            if worker.city == "Budapest":
                bpSalary += int(worker.salary)
        return bpSalary     
    
    def highestSalary(self):
        highest=None
        tempHighest=int(self.workerList[0].salary)
        for worker in self.workerList:
            if tempHighest<int(worker.salary):
                tempHighest=int(worker.salary)
                highest=worker.name
        return highest, tempHighest
    
    def highestSalary2(self):
        highestSal=790000
        HighestMan = []
        for worker in self.workerList:
            if int(worker.salary) == highestSal:
                
                HighestMan.append(worker.name)
        
        return HighestMan  
    
    def noBonus(self):
        noBonusMan = 0
        for worker in self.workerList:
            if int(worker.bonus) == 0:
                noBonusMan += 1
        return noBonusMan
    
    def countGyoriSalary(self):
        GyoriSalary = 0
        counter = 0
        for worker in self.workerList:
            if worker.city == "Győr":
                GyoriSalary += int(worker.salary)
                counter += 1
        salaryAverage = GyoriSalary / counter
        return salaryAverage
    
    def avgGyoriSalary(self):
        GyoriSalary = 0
        counter = 0
        for worker in self.workerList:
            if worker.city == "Győr":
                GyoriSalary += int(worker.salary)
                counter += 1
        salaryAverage = GyoriSalary / counter
        file = open("gyAvg.txt", "w", encoding="UTF-8")
        file.write("Győri fizetés átlag: \n")
        file.write(str(salaryAverage))
        file.close()
        return "A fájlba írás megtörtént."
    
    
                
                
               
                
                
        
            
manager = WorkerManager()
manager.controller()           
"""
0. fájl beolvasás 
1. dolgozók számolása
2. Szegedi dolgozók létszáma
3. Budapesti dolgozók fizetése
4. Legtöbbet kereső ember
5. Hányan nem kapnak jutalmat
6. Győri dolgozók fizetésének az átlaga
7. Fájlba írni az átlagot
"""