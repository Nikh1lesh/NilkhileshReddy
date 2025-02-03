class Logger:
    def log(self, message):
        print(message)

    def log(self, message, type):
        if type == 'error':
            print(f'Error: {message}')
        elif type == 'warning':
            print(f'Warning: {message}')
        elif type == 'info':
            print(f'Info: {message}')
        else:
            print(f'Unknown type: {message}')
def main():
    l = Logger()
    l.log('This is an error', 'error')
    l.log('This is a warning', 'warning')
    l.log('This is an info', 'info')
    l.log('This is an unknown type')
main()