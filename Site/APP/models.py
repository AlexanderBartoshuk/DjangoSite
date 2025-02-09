from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(blank=True) 
    def __str__(self):
        return self.name 

class Products(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(blank=True) 
    category = models.ForeignKey(Categories,
                                on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return self.name 


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length= 50 , verbose_name= "ФИО учителя")
    subject = models.CharField(max_length=50, verbose_name= "Предмет")
    email = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.name 
    

class Group(models.Model):
    group = models.CharField(max_length=20, verbose_name="Название группы" , unique=True)
    about_group = models.TextField(blank = True, verbose_name="Информация о группе")
    email = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.group 

class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name= "ФИО судента" , unique= True) 
    age = models.IntegerField(verbose_name="Возраст" , blank=True) 
    group = models.ForeignKey(Group, verbose_name= 'Группа' , on_delete=models.DO_NOTHING)
    number = models.CharField(max_length= 11, verbose_name= 'Номер телефона' , blank= True)
    def __str__(self):
        return self.name 
    

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


















# Chardfield поле текста и обязательный аргумент 
# max_lenght - максимальная длина этой строчки 
#TextField - больше текстовое поле 
#IntegerField - поле целых чисел 
#ForeignKey - One to May 
#on_delete - показывает что будет происходить при удалении 
#OneToOneField - One to one 
#Many to many field 

#Аргументы 
#verbose_name - отображаемое имя 
#blank - True\False проверка оригинальности 



