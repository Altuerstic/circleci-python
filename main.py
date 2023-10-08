def to_upper(name):
    return name.upper()
def say_hello(name):
    print(f'Hello, {name}')
    
if __name__ == '_main_':
    name = 'TrainWithGaurav'
    say_hello(name)
    up = to_upper(name)
    print(up)