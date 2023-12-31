
#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]['last_name']='Bryant'
print(students[0])
sports_directory['soccer'][0]= 'Andres'
print(sports_directory['soccer'])
z[0]['y']=30
print(z)

#Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'} 
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)


def iterateDictionary(some_list):
    for i in range (len(some_list)):
        print(f"first_name {some_list[i]['first_name']} , last_name {some_list[i]['last_name']}")
iterateDictionary(students)

#Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('first_name', students)     
iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    dojoKeys=[] 
    dojoValues=[]   
    dojoKeys=list(dojo.keys())  
    for i in range (len(dojoKeys)):
        print(len(dojoKeys[i]), dojoKeys[i])        
        dojoValues=list(dojo[dojoKeys[i]])
        for j in range (len(dojoValues)):
            print(dojoValues[j])

printInfo(dojo)
