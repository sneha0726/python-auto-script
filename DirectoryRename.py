from sys import *
import os
import hashlib




def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName) 
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")

def printResults(dict1):
   results = list(filter(lambda x: len(x) > 1, dict1.values()))
   ifound = 0
   log_filename = "Logfile.txt"

   if len(results) > 0:
        with open(log_filename, "w") as log_file:
            log_file.write("Duplicates Found:\n")
            for result in results:
                for subresult in result:
                    ifound += 1
                    log_file.write(subresult + "\n")
        print("totoal file found display",ifound)
   else:
        print("No duplicate files found.")
    
def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and delete duplicate files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
      
        arr = findDup(argv[1])
        printResults(arr)
       
        
        

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()
