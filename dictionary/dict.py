# key value pairs- key is immutable
data = {1:"Yash", 2:"Ujjwal", 4:"Harit"}
print(data)
print(data[1])
# print(data[3]) error 
print(data.get(2))
print(data.get(3))
print(data.get(4, 'Not Found'))#returns data at key 1
print(data.get(3, 'Not Found')) #if value is not found

keys = ['Raj','Ravi','Harshit']
values = ['Python','Java','JS']
dict = dict(zip(keys,values)) #merge two list in a dict
print(dict)
print(dict['Raj'])
dict['Monika']='C#' #add data
print(dict)

del dict['Ravi'] #use key to delete data
print(dict)

prog = {'JS':'Atom', 'C#':'VS', 'Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}
print(prog) 
print(prog['JS']) 
print(prog['Python']) 
print(prog['Python'][1]) 
print(prog['Java']) 
print(prog['Java']['JEE']) 
print(prog['Java']['JSE']) 

