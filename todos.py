todos= []

while True:
    user=input("enter add,show / remove : ")
    
    match user:
        case 'add':
            todo=input("enter your todos")
            todos.append(todo)
        case 'show':
            for items in todos:
                print (items)
        case 'remove':
            delete=input('remove todo')
            for items in todos:
                todos.remove(delete)
                print (items)
                print(delete' was removed')

