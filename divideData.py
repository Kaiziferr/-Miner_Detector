def fileRead():
    file = open("moderna_procesada.txt","r")
    j = 0
    x = 0
    for i in file.readlines():
        i = i.replace('\n','')
        if j % 500 == 0 and j!=0:
            x = x+1
            print(f"/----- file{x}finish -----/")
        file_save = open(f"data{x}.txt",'a')
        file_save.write(i+'\n')
        file_save.close()
        j = j+1
        

def main():
    fileRead()
main()