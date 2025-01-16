import json
# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
DATABASE_NAME = 'phonebook.json'

def addition():
    contact = {}
    while True:
        number = input('Enter number: ')
        if number.isdigit():
            contact['number'] = number
            break
        else:
            print('Please enter only number')
    
    while True:
        answer = input('If you want to add a first_name, then write: first_name\n'
            'If you want to add a last_name, then write: last_name\n'
            'If you want to add a city, then write: city\n'
            'If you want to add a state, then write: state\n'
            "If tha'ts all you wanted to add, then write: stop\n")
  
        if 'first_name' == answer:
            answer = input('Enter first name: ')
            contact['first name'] = answer

  
        elif 'last_name' == answer:
            answer = input('Enter last name: ')
            contact['last name'] = answer

  
        elif 'city' == answer:
            answer = input('Enter city: ')
            contact['city'] = answer

  
        elif 'state' == answer:
            answer = input('Enter state: ')
            contact['state'] = answer


        elif 'stop' == answer:
            break
  
        else:
            print('Please enter only variant underneath') 
        if 'first name' in contact and 'last name' in contact:
            contact['full name'] = contact['first name'] + ' ' + contact['last name']
        print(contact)

    try:
        with open(DATABASE_NAME, 'r') as file:
            add_contact = json.load(file)
            add_contact.append(contact)
    except (FileNotFoundError, AttributeError):
        contacts = []
        contacts.append(contact)
        add_contact = contacts
    with open(DATABASE_NAME, 'w') as file:
        json.dump(add_contact, file)

def search(search_object):
    with open(DATABASE_NAME, 'r') as file:
        book = json.load(file)
        number = 0
        for contact in book:
            for data in contact.values():
                if search_object == data:
                    number += 1
                    print(f'Contact number: {number}')
                    for key, value in contact.items():
                        print(key, ':', value)
                    print('')


def remove_contact(removable_object):
    number = 0
    removable_contact = []
    with open(DATABASE_NAME, 'r') as file:
        book = json.load(file)
        for contact in book:
            for data in contact.values():
                if removable_object == data:

                    for key, value in contact.items():
                        print(key, ': ', value)
                    removable_contact.append(contact)
                    number += 1
                    print(f'Contact number: {number}\n')
                    
        while True:
            answer = input('Enter the number of the contact you want to delete: ')
            if answer.isdigit(): 
                if int(answer) <= len(removable_contact):
                    for key, value in removable_contact[int(answer)-1].items():
                        print(key, ': ', value)
                    
                    while True:
                        confirmation = input('Are you sure you want to delete this contact?(yes/no)\n')
                        if confirmation.lower() == 'yes':
                            with open(DATABASE_NAME, 'r') as file:
                                contacts = json.load(file)
                                contacts.remove(removable_contact[int(answer)-1])
                            with open(DATABASE_NAME, 'w') as file:
                                json.dump(contacts, file)
                            print('Contact removed')
                            break
                        elif confirmation.lower() == 'no':
                            break
                        else:
                            print('Please enter only the specified options')
                    break
                else:
                    print('Unfortunately it\'s not the richt number:/')
                            
            else:
                print('Unfortunately, there is no such answer:/')
        if removable_contact == []:
            print('Unfortunately, no contact was found:/')



def edit_contact(editable_object):
    number = 0
    editable_contact = []
    with open(DATABASE_NAME, 'r') as file:
        book = json.load(file)
        for contact in book:
            for data in contact.values():
                if editable_object == data:

                    for key, value in contact.items():
                        print(key, ':', value)
                    editable_contact.append(contact)
                    number += 1
                    print(f'Contact number: {number}\n')
        
        if len(editable_contact) >= 1:
            while True:
                answer = input('Enter the number of the contact you want to edit: ')
                if answer.isdigit(): 
                    if int(answer) <= len(editable_contact):
                        for key, value in editable_contact[int(answer)-1].items():
                            print(key, ': ', value)
                        
                        while True:
                            confirmation = input('Are you sure you want to edit this contact?(yes/no)\n')
                            if confirmation.lower() == 'yes':
                                with open(DATABASE_NAME, 'r') as file:
                                    contacts = json.load(file)
                                    contact_index = contacts.index(editable_contact[int(answer)-1])
                                    while True:
                                        print('')
                                        print('first name\n'
                                            'last name\n'
                                            'full name\n'
                                            'number\n'
                                            'city\n'
                                            'state\n')
                                        answer= input('What do you want to change?\n')
                                        
                                        if answer.lower() == 'first name':
                                            contact = contacts[contact_index]
                                            contact['first name'] = input('What first name do you want to put down?\n')
                                            break
                                        
                                        elif answer.lower() == 'last name':
                                            contact = contacts[contact_index]
                                            contact['last name'] = input('What last name do you want to put down?\n')
                                            break
                                        
                                        elif answer.lower() == 'full name':
                                            contact = contacts[contact_index]
                                            contact['full name'] = input('What full name do you want to put down?\n')
                                            break
                                        
                                        elif answer.lower() == 'number':
                                            while True:
                                                answer = input('What number do you want to put down?\n')
                                                if answer.isdigit():
                                                    contact = contacts[contact_index]
                                                    contact['number'] = answer
                                                    break
                                                else:
                                                    print('Please enter only number')
                                            break
                                                
                                        
                                        elif answer.lower() == 'city':
                                            contact = contacts[contact_index]
                                            contact['city'] = input('What city do you want to put down?\n')
                                            break
                                        
                                        elif answer.lower() == 'state':
                                            contact = contacts[contact_index]
                                            contact['state'] = input('What state do you want to put down?\n')
                                            break
                                        else:
                                            print('Please enter only the options below')
                                with open(DATABASE_NAME, 'w') as file:
                                    json.dump(contacts, file)
                                print('Contact edit')
                                break
                            elif confirmation.lower() == 'no':
                                break
                            else:
                                print('Please enter only the specified options')
                        break
                    else:
                        print('Unfortunately it\'s not the richt number:/')
                                
                else:
                    print('Unfortunately, there is no such answer:/')
            if editable_contact == []:
                print('Unfortunately, no contact was found:/')
        else:
            print('Unfortunately, no contact was found')


def contacts():
    with open(DATABASE_NAME, 'r') as file:
        book = json.load(file)
        for contact in book:
            print('\n')
            for key, value in contact.items():
                print(key,': ', value)
    




while True:
    answer = input('\nEnter "contacts" to show all numbers\n'
          'Enter "add" to add a contact\n'
          'Enter "search" to search a contact\n'
          'Enter "remove" to remove a contact\n'
          'Enter "edit" to edit a contact\n' 
          'Enter "stop" to stop\n')    
    if answer.lower() == 'stop':
        break
    elif answer.lower() == 'contacts':
        contacts()
    elif answer.lower() == 'add':
        addition()
    elif answer.lower() == 'search':
        search(input('What you\'re looking for?\n'))
    elif answer.lower() == 'remove':
        remove_contact(input('Which contact do you want to delete?\n'))
    elif answer.lower() == 'edit':
        edit_contact(input('Which contact do you want to edit?\n'))
    else:
        print('Unfortunately, there is no such answer:/')