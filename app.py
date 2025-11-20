todos = []


def add_todo():
    task = input('Enter a new task: ')
    todos.append(task)
    print('task has been added!')
    



def delete_todo():

    view_todo()
    pickANum = int(input('Enter number to be deleted : '))
    if 1 <= pickANum <= len(todos):
        removed = todos.pop(pickANum - 1)
        print(f'removed : {removed} \n')
    else : 
        print('invalid number!!! Please retry!')



def view_todo():
    print("your todos are: ")
    if len(todos) == 0:
        print('no todos yet! Please add one')
    else:
        for i, task in enumerate(todos, start=1):
            print(f'{i}. {task}')
    
def update_todo():
    view_todo()

    pickANum = int(input('Enter number to be updated : '))
    if 1 <= pickANum <= len(todos):
        new_task = input('update the task: ')
        todos[pickANum -1] = new_task
        print('task updated')
    else:
        print('invalid number!!')


def main():
    while True:
        print("this is todo app")
        print('please choose ; ')
        print('1. view todo')
        print('2. add todo')
        print('3. delete todo')
        print('4. update tood')

        num = input("choose an option: ")

        if num == '1':
            view_todo()
        elif num == '2':
            add_todo()
        elif num == '3':
            delete_todo()
        elif num == '4':
            update_todo()
        else:
            print('invalid option')



main()