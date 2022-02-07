#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(type(1))
print(type([]))
print(type(()))
print(type({}))


# ## class
# User defined objects are created using the <code>class</code> keyword. The class is a blueprint that defines the nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. For example, above we created the object <code>lst</code> which was an instance of a list object. 
# 
# Let see how we can use <code>class</code>:

# In[6]:


class Dog():
    
    def __init__(self, breed):
        
        self.breed = breed


# In[7]:


dog1 = Dog()


# In[8]:


dog1 = Dog(breed='Lab')


# In[9]:


type(dog1)


# In[10]:


dog1.breed


# An **attribute** is a characteristic of an object.
# A **method** is an operation we can perform with the object.
# 
# For example, we can create a class called Dog. An attribute of a dog may be its breed or its name, while a method of a dog may be defined by a .bark() method which returns a sound.

#     __init__() 
# is called automatically right after the object has been created:
# 
#     def __init__(self, breed):
# Each attribute in a class definition begins with a reference to the instance object. It is by convention named self. The breed is the argument. The value is passed during the class instantiation.
# 
#      self.breed = breed

# In[11]:


class Dog():
    
    def __init__(self, breed):
        
        self.attribute_breed = breed


# In[12]:


dog2 = Dog(breed='Huskie')


# In[13]:


dog2.attribute_breed


# In[22]:


class Dog():
    
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots


# In[23]:


dog3 = Dog(breed='lab', name='sammy', spots=False)


# In[24]:


dog3.breed


# In[25]:


dog3.name


# In[26]:


dog3.spots


# Note how we don't have any parentheses after breed; this is because it is an attribute and doesn't take any arguments.
# 
# In Python there are also *class object attributes*. These Class Object Attributes are the same for any instance of the class. For example, we could create the attribute *species* for the Dog class. Dogs, regardless of their breed, name, or other attributes, will always be mammals. We apply this logic in the following manner:

# In[27]:


class Dog():
    
    # class object attribute
    # same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots


# In[29]:


dog4 = Dog(breed='laB', name='Sam', spots=False)


# In[30]:


dog4.species


# ## Methods
# 
# Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. Methods are a key concept of the OOP paradigm. They are essential to dividing responsibilities in programming, especially in large applications.
# 
# You can basically think of methods as functions acting on an Object that take the Object itself into account through its *self* argument.

# In[52]:


class Dog():
    
    # class object attribute
    # same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self,breed,name):
        
        self.breed = breed
        self.name = name
        
    # Operations/Actions ---> Methods
    
    def bark(self,number):
        print('HAV! My name is {} and the number is {}'.format(self.name,number))


# In[53]:


dog5 = Dog('lab','Madam')


# In[54]:


dog5.species


# In[55]:


dog5.bark


# In[56]:


dog5.bark(3)


# In[66]:


class Circle():
    
    pi = 3.14 # class object attribute
    
    def __init__(self,radius=1): # default value = 1
        
        self.radius = radius
        self.area = radius*radius*self.pi
        
    def get_circumference(self): # method
        return self.radius * self.pi * 2         


# In[63]:


cir = Circle()


# In[59]:


cir.pi


# In[60]:


cir.radius


# In[61]:


cir.get_circumference()


# In[67]:


cir2 = Circle(30)


# In[68]:


cir2.get_circumference()


# In[69]:


cir2.area


# ## Inheritance
# 
# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).

# In[71]:


class Animal():
    
    def __init__(self):
        print('Animal created')
        
    def who_am_i(self):
        print('I am an animal')
        
    def eat(self):
        print('I am eating')


# In[83]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
    def who_am_i(self):
        print('I am a dog')
        
    def bark(self):
        print('HAV')


# In[72]:


cat = Animal()


# In[74]:


cat.eat()


# In[75]:


cat.who_am_i()


# In[84]:


dogx = Dog()


# In[85]:


dogx.eat()

# there is not any method eat. We inherited it from Animal class.


# In[86]:


dogx.who_am_i()

# we overwrote the method in Dog class.


# In[87]:


dogx.bark()


# ## Polymorphism
# 
# While functions can take in different arguments, methods belong to the objects they act on. In Python, *polymorphism* refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in.

# In[92]:


class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says hav'


# In[93]:


class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says miav'


# In[94]:


madam = Dog('madam')
felix = Cat('felix')


# In[97]:


print(madam.speak())


# In[98]:


print(felix.speak())


# In[101]:


for pet in [madam,felix]:
    
    print(type(pet))
    print(pet.speak())


# In[102]:


def pet_speak(pet):
    print(pet.speak())


# In[103]:


pet_speak(madam)


# In[104]:


pet_speak(felix)


# In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.
# 
# A more common practice is to use abstract classes and inheritance. An abstract class is one that never expects to be instantiated. For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:

# In[105]:


class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


# In[106]:


a = Animal('fred')


# In[107]:


a.speak()


# In[108]:


class Dog(Animal):
    
    def speak(self):
        return self.name + ' says hav'


# In[109]:


class Cat(Animal):
    
    def speak(self):
        return self.name + ' says miav'


# In[110]:


fino = Dog('fino')
tekir = Cat('tekir')


# In[111]:


print(fino.speak())


# ## Special Methods
# Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax.

# In[112]:


liste = [1,2,3]


# In[113]:


len(liste)


# In[114]:


class Sample():
    pass


# In[115]:


örnek = Sample()


# In[116]:


print(örnek)


# In[124]:


len(örnek)


# In[132]:


class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book object has been deleted')


# In[133]:


b = Book('python','Jose',222)


# In[134]:


print(b)


# In[135]:


str(b)


# In[136]:


len(b)


# In[137]:


del b


# In[138]:


b


# In[ ]:




