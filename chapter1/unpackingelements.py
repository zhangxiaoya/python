print ("use star expressions to solve too many values to unpack problem")


def avg(values):
    if(len(values) < 1):
        return None
    else:
        return sum(values) / len(values)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

grades = [1,2,3,4,5];

print(drop_first_last(grades))

record = ['Dave','dace@develop.com','773-555-112','888-222-111']
name,email,*phone_numbers = record
print(name)
print(email)
print(phone_numbers)

records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4)
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

