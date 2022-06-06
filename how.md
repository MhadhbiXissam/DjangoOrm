# Field Options : 
- **null** : default False , enable value to be null . 
- **blank** : default False , used with string types to allow inserting empty sstring in place consider it null . 
- **choices** : tuple of tuple ( (k , v) , (k , v) ..... ) .and in constructor use Person(name="Fred Flintstone", columdb_name= k ) . 
- **default** : can be value or callable , called every time object created .
- **help_text** : usefull for documentations . 
- **primary_key** : if set to True mecanisim of id will be overided otherwise django use id integer mecanisme by default . 
- **unique** : every row shall have unique value .   


# Overide save methode for to do act on saving before or after  : 
`from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()`

