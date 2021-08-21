'''
    Code By : Sairaj Bhise
    Topic : Data Structures and Algorithms (Hash Table Data Structure Basic) 
'''

# Declare the max length of Hash Table
HashTable = [[],] * 10

def checkPrime(n) :
    if n == 0 or n == 1 :
        return 0
    
    for i in range(2,n//2) :
        if n%i == 0 :
            return 0
    return 1

# We get prime from here
def getPrime(n)  :
    if n%2 == 0 :
        n = n + 1
    while not checkPrime(n)  :
        n += 2
    return n
    
# Hash index here
def hashFunction(key) :
    capacity = getPrime(10)
    return key%capacity

# Insert Function here
def insert(key,value) :
    index = hashFunction(key) 
    HashTable[index] = [key,value]
    
def delete(key) :
    index = hashFunction(key)
    HashTable[index] = 0
    
# Print Empty table
print('Empty Hashtable\n',HashTable)
insert(123,'Sairaj')
insert(234,'Raviraj')
insert(345,'Pruthviraj')
insert(456,'Shreya')
insert(567,'Shraddha')
insert(678,'Enemy')

# Print table after insertion
print('\nTable after insertion\n',HashTable)

delete(678)
print('\nAfter deleting\n',HashTable)











