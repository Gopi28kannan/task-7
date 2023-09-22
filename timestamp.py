import time
ts=time.time()
import datetime
x = datetime.datetime.now()
k = open("file1.txt","a")
k.write(str(x)+'  '+str(ts)+'\n')
k.close()
k = open("file1.txt", "r")
print(k.read())
k.close()
