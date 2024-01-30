i=7
numer =[2,1,3,4,5,3,9]
def bubble_sort(numer):
    for i in range(len(numer)):
        maximo = numer[i]
        for j in range(i+1, len(numer)):
            if numer[j] > maximo:
                numer[i],numer[j]=numer[j],numer[i]
                maximo = numer[i]
bubble_sort(numer)
print(numer)   
   
            




    

    