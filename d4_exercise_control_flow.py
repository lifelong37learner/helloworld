#for in 9*9 乘法表

for i in range(1,10):
    for j in range(1,i+1):
      print("%d * %d= %2d" % (i,j,i*j),end=" ")
    print(" ")
    
   
#while实现乘法表

i=1
while i<=9:
    j=1
    while j<=i:
        if i % 2 !=0:
            #print("%d * %d = %d"%(i,j,i*j),end='\t')
            print('{}*{}={}\t'.format(i,j,i*j),end='')
            #print(i,'*',j,'=',i*j,end='\t')
            j+=1
    print()
    i+=1
