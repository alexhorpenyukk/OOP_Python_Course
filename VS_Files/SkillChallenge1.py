class TextField:
    def __init__(self, length):
        self.length = length

    def __get__(self, instance, owner):
        return instance.__dict__.get('att')
    
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError('value should be string type')
        
        if len(value) > self.length:
            raise ValueError('value should contain less than 200 charackters')
        
        instance.__dict__['att'] = value
    
    def __delete__(self, instance):
        pass
    
class PersonTable:
    first_name = TextField(200)
    second_name = TextField(200)

p1 = PersonTable()
p2 = PersonTable()

p1.first_name = 'Andrew'
p1.second_name = 'Hryshiv'
p2.first_name = 'Bob'

print(p1.first_name)
print(p1.second_name)
print(p2.first_name)