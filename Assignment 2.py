student_dict={}
def add():
    name=input("Please enter the name:")
    marks=input("Please enter the marks:")
    student_dict[name]=marks
    print("The updated new list is:")
    print(student_dict)
def update():
     name=input("Please enter the name:")
     marks=input("Please enter the marks:")
     if name in student_dict.keys():
        student_dict.update({name:marks})
        print("The updated new list is:")
        print(student_dict)
     else:
        print("The name doesn't exist")
        
def delete():
     name=input("Please enter the name:")
     if name in student_dict.keys():
        student_dict.pop(name)
        print("The updated new list is:")
        print(student_dict)
     else:
        print("The name doesn't exist")
        
def search():
     name=input("Please enter the name:")
     if name in student_dict.keys():
        print("The stundent's details are:"+name+" "+student_dict[name])
     else:
        print("The name doesn't exist")
    
add()
update()
search()
delete()
