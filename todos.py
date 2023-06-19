todos= []

while True:
    user=input("enter add,show, remove & edit : ")
    user.strip()
    
    match user:
        case 'add':
            todo=input("enter your todos")
            todos.append(todo)
        case 'edit':
            number=input('enter number of entry to be changed')
            number-=1
            new_entry=input('enter the replacement entry')
            todos[number]=new_entry
            for items in todos:
                print (items)
            print('entry has been updated')
        case 'show':
            for items in todos:
                print (items)
        case 'remove':
            delete=input('remove todo')
            for items in todos:
                todos.remove(delete)
                print (items)
                print(delete + ' was removed')
        case otherwise:
            print("inccorect input")

