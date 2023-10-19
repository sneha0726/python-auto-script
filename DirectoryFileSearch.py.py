from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf= afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def displaychecksum(dir_name):
    flag=os.path.isabs(dir_name)
    if flag==False:
        path=os.path.abspath(dir_name)
    exists=os.path.isdir(dir_name)
    files=os.listdir(dir_name)

    if exists:
            for  filen in files:
                path =os.path.join(dir_name,filen)
                file_hash=hashfile(path)
                print(path)
                print(file_hash)
                print("") 

def main():
    print("----marvellous infosystem ------")
    print("application name:"+argv[0])

    if (len(argv)!=2):
        print("error :invalid number of argument")
        exit()
    if (argv[1]=="-h")or (argv[1]=="-H"):
        print("this script is used to travese specific driectory and display checksum of the files")
        exit()
    
    if (argv[1]=="-u")or (argv[1]=="-U"):
        print("usage: directroychecksum.py " "demo" )
        exit()

    try:
       arr= displaychecksum(argv[1])
    except ValueError:
        print("error:invalid input",E)
    except Exception as E:
        print("error : invalid input :",E)

if __name__=="__main__":
    main()
