def main():
    notes = []
    
 # start add_note function
def add_note(notes):
    note = input('Enter Note: ')
    notes.append(note)
    print('Note added!\n')
# stop add_note function

# start view_notes function
def view_notes(notes):
    if not notes:
        print('No notes yet.\n')
    else:
        print('Your Notes:')
        for i, note in enumerate(notes, 1):
            print(f'{i}. {note}')
# stop view_notes function

    while True:
        print('--- Personal Journal ---')
        print('1. Add a note')
        print('2. View notes')
        print('3. Exit')

        choice = input('Select an option: \n')

        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Please try again.\n')
# stop main function

main()
