# Field Options : 
- **null** : default False , enable value to be null . 
- **blank** : default False , used with string types to allow inserting empty sstring in place consider it null . 
- **choices** : tuple of tuple ( (k , v) , (k , v) ..... ) .and in constructor use Person(name="Fred Flintstone", columdb_name= k ) . 
- **default** : can be value or callable , called every time object created .
- **help_text** : usefull for documentations . 
- **primary_key** : if set to True mecanisim of id will be overided otherwise django use id integer mecanisme by default . 
- **unique** : every row shall have unique value .   


# Overide save methode for to do act on saving before or after or extra validations before save : 
```
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()
```

# Fields Types : 
- **AutoField** : not needed cause when primapr key is set to true , otherwise will be used as incremental ids . 
- **BigAutoField** : same like **AutoField** but in range of 1 .. 9223372036854775807 .
- **IntegerField** : Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
- **BigIntegerField** : A 64-bit integer, with in range -9223372036854775808 .. 9223372036854775807
- **BinaryField** : store raw binary data , it has option max_length . 
- **BooleanField** : (true / false ) , The default value of BooleanField is None when Field.default isn’t defined.
- **CharField** : list of chars has option max_length . 
- **TextField** : for large text content . 
- **DateField(auto_now=False, auto_now_add=False, ...)** : datetime field but it if you set default value it will be usefull for tracking time of creating (auto_now = True) and last modified  = auto_now_add = True ) , be carfull must always use Model.save() to have such utilty  . 
- **DateTimeField(auto_now=False, auto_now_add=False, ..options..)**  : same as DateFiled . 
- **DecimalField(max_digits=None, decimal_places=None, ...)** : for save excat decimal precession , max_digit  = max in number , dicaml places  = numbers of precession . 
- **DurationField** : equivalent in python **timedelta** , can use bigint to count mill seconds . 
- **EmailField** : a char field withy email validator . 
- **TimeField** : same as **DateField** . 










































