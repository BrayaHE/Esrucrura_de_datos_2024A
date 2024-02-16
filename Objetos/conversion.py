#import Nodo
'''Implementador'''        
'''CON IF '''  
# from Nodo import Nodo
# e = [1, 2, 3, 4, 5]
# i=0
# if __name__ == '__main__':
#     head = Nodo()
#     curr = head
#     for i in e:
#         curr.val = i
#         curr.next = Nodo()
#         curr = curr.next      
#     while head:
#         print(head)
#         head = head.next
        
# '''Codigo en clase  while'''
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

'''Listas doblemente ligadas'''
# import nodo

# e = [1, 2, 3, 4, 5]
# i = 0

# if _name_ == '_main_':
#     head = nodo.nodo()  
#     curr = head
    
#     while i < len(e):
#         curr.val = e[i]
#         if i < len(e) - 1:  
#             curr.nextn = nodo.nodo()  
#             curr.nextn.prevn = curr  # Establecer el nodo actual como el anterior del siguiente nodo
#             curr = curr.nextn
#         i += 1

#     curr = head
#     while curr is not None:
#         print("Nodo actual:", curr.val, end=" ")
#         if hasattr(curr, 'prevn') and curr.prevn:
#             print(", Anterior:", curr.prevn.val, end=" ")
#         if hasattr(curr, 'nextn') and curr.nextn:
#             print(", Siguiente:", curr.nextn.val, end=" ")
#         print()
#         curr = curr.nextn

'''Listas ligadas cirulares'''
# from Nodo import Nodo
# e = [1, 2, 3, 4, 5]
# i=0
# if __name__ == '__main__':
#     head = Nodo()
#     curr = head
#     for i in e:
#         curr.val = i
#         curr.next = Nodo()
#         curr = curr.next 
        
#         curr.next=head 
        
#     curr = head
#     for _ in range(len(e)):
#         print(curr.val)
#         curr = curr.next        































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
