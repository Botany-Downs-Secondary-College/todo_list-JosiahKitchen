# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:56:19 2021

@author: josiah
"""
loop = 1
program_loop = 1
global to_do_list
global add_loop
global presentation_list
to_do_list = []
presentation_list = {}

def add():
    loop = 1
    while loop == 1:
        list_item = input("What would you like to add to your to do list?")
        if list_item in to_do_list:
            print("This is already in your list")
            
        elif list_item not in to_do_list:
            to_do_list.append(list_item)
            loop = 2

def remove():
    global to_do_list
    remove_value_input = input("Would you like to remove a listing? (Yes/No) ")
    if remove_value_input == "Yes":
        loop = 1
        while loop == 1:
            remove_value = (int(input("Please enter the number listing you wish removed ")) - 1)
            try:
                to_do_list = to_do_list.pop(to_do_list[int(remove_value)])
            except IndexError:
                print("Please enter a the number of a valid listing")
                continue
            
            view()
            break
    elif remove_value_input == "No":
        pass
    else:
        remove()

def view():
    x = 0
    global to_do_list
    presentation_list = {}
    while x < len(to_do_list):
        presentation_list[(int(len(presentation_list) + 1))] = to_do_list[int(x)]
        x += 1
    print(presentation_list)
    remove()
        
def return_to_menu():
    question = 1
    global add_loop
    while question == 1:
        munu_return = input("Type 'Done' to return to menu")
        if munu_return == "Done":
            question = 2
            add_loop = 2
        else:
            break
        
print("Welcome to the to do list")
while program_loop == 1:
    menu = input('''
      Please select what you would like to do by the numbers below
      
      1. Add to list 2. View list 3. Exit''')
    try:
        menu = int(menu)
    except:
        print("Please enter a number")
        continue
         
    if menu == 1:
        add_loop = 1
        while add_loop == 1:
            add()
            return_to_menu()
            
           
    elif menu == 2:
        view()
        
    elif menu == 3:
        print("Thank you for using the to do list")
        program_loop = 2
