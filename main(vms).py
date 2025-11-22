import Valkyrie_manager as vm 
import Otto as ot 
import file_handler as fh
def main():
    while True:
        print('------------------------------------------')
        print('Welcome to the Schikshal database')
        username = input('Enter your username(e to exit): ')
        if username.lower() == 'e':
            break
        password = input('Enter your password: ')
        if username == 'Amber' and password == 'Amber213':
            vm.valk()
        elif username == 'Otto' and password == 'Otto213':
            ot.otto()
        else:
            print('Invalid credentials')

if __name__ == '__main__':
    main()