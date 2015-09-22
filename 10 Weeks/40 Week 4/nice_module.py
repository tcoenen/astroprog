'''
Demonstration of the __name__ variable
'''

def addtwo(x):
    '''Add two to a number'''
    return x + 2

if __name__ == '__main__':
    print addtwo(10)
    print __name__
