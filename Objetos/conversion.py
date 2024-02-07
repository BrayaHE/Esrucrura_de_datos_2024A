#import Nodo
'''Implementador'''        
'''CON IF '''  
from Nodo import Nodo
e = [1, 2, 3, 4, 5]
i=0
if __name__ == '__main__':
    head = Nodo()
    curr = head
    for i in e:
        curr.val = i
        curr.next = Nodo()
        curr = curr.next          
    while head:
        print(head)
        head = head.next
        
'''Codigo en clase  while'''
# from Nodo import Nodo

# e = [1, 2, 3, 4, 5]
# i=0
# if __name__ == '__main__':
#     head = Nodo()
#     curr = head
# while i < len(e):
#     curr.val = e[i]
#     if i < len(e):
#         curr.next = Nodo()
#         curr = curr.next
#         i += 1   

#     temp = head
#     while temp:
#         print(temp)
#         temp = temp.next


















'''Codigo en clase'''      
# if __name__ == '__main__':
#     head = Nodo()
#     curr = head
#     lista = list(range(1,6))
#     head = Nodo()
#     curr = head
    
#     for i in lista[:-1]:
#         curr.val = i
#         curr.next = Nodo()
#         curr = curr.next
#     curr.val = lista[-1]
    
#     e = [1,2,3,4,5]
#     for i in e:
#         curr.val=i
#         if i != e[-1]:
#             curr.next = Nodo()
#             curr = curr.next    
#     print(head)
