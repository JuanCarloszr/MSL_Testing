
from pathlib import Path

def writefile():
    f = open ('ejemplo.txt','w')
    f.write('Juan Carlos Chávez Ramírez')
    f.close()


def readfile():
    f = open ('ejemplo.txt','r')
    leer = f.read()
    print(leer) 
    f.close()


def automatizacion():
   
   directory = Path('C:/Users/jcarlos/Documents/testingMSL/IBM/')
   filepath = Path('C:/Users/jcarlos/Documents/testingMSL/IBM/prueba.txt')

   directory.mkdir(parents=True, exist_ok=True)
   filepath.touch(exist_ok=True)

   f = open('C:/Users/jcarlos/Documents/testingMSL/IBM/prueba.txt', 'w')
   f.write('International Business Machines') 
   f.close()

   new_file_path = Path('C:/Users/jcarlos/Documents/testingMSL/IBM/new_prueba.txt')
   filepath.rename(new_file_path)

   directory.rename(Path('C:/Users/jcarlos/Documents/testingMSL/MSL_Test'))
   

if __name__=='__main__':
   automatizacion() 

   


