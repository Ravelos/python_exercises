# def find_elements(elem, arr):
#     found = False
#     for i in range(len(arr)):
#         if arr[i] == elem:
#             found = True
        
#     if found == False:
#         print('We found the name ' + elem)
#     else:
#         print('We did not find the name ' + elem)


# names = ["Carlos", "Raul", "Fernando", "Juan"]

# find_elements("Fernando", names)

# Mariana, Fernanda, Jefferson, Oswaldo

def find_elements_input(arr):
    elem = input("Digite o nome do elemento: ")
    found = False
    for i in range(len(arr)):
        if arr[i] == elem:
            found = True
        
    if found == True:
        print('We found the name: ' + elem)
    else:
        print('We did not find the name: ' + elem)


names = ["Carlos", "Raul", "Fernando", "Juan"]

find_elements_input(names)