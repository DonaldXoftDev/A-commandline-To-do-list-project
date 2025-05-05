To_do_list = []

def add_task():
    still_adding_task = True
    while still_adding_task:
        task = input('What task to you want to add: ').lower().strip().capitalize()
        if task:
            To_do_list.append(task)
            print('Task have been added.')
        stop = input('Are you done? "y" or "n": ').strip()
        if stop == 'y':
            still_adding_task = False


def view_task():
    dict_view  = {}
    if not To_do_list:
        print('No task has been added yet!')
    else:
        for index,task in enumerate(To_do_list):
            print(f'{index + 1}.{task.capitalize()}.')
            dict_view[index + 1] = task
        return dict_view


def remove_task():
    if not To_do_list:
        print('The Todo list is empty and so there is nothing here to remove.')
    else:
        print('list of the things in the the To do list:')
        task_view_dict = view_task()
        item_to_remove = int(input('What task number  do you want to remove? '))
        if item_to_remove in range(len(task_view_dict)):
            popped_value = task_view_dict.pop(item_to_remove)
            To_do_list.remove(popped_value)
            print(f'You have successfully removed task{item_to_remove}: {popped_value[:20]}...')
        else:
            print('There is no such task number in your To do list')


operations_available = {
    'add task': add_task,
    'view task': view_task,
    'remove task': remove_task,
}
print('Welcome to The To do list program!')
print('You can perform any of the operation below:')

for i, operation in enumerate(operations_available):
    print(f'{i + 1 }.{operation}')

start_program  = True
while start_program:
    decide = input('What do you want to do?'
                   ' type the text of what you want to do: ').strip()
    if decide:
        if decide == 'end':
            start_program = False
            print('Goodbye, see you later.')
        else:
            if decide in operations_available:
               operations_available[decide]()
               print('\n' * 2)
            else:
                print('Invalid input, choose from add task, view task, remove task or type end to exit.')
                start_program = True






