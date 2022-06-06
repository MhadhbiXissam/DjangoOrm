# Field Options : 
## Field options¶ : 
- **null** : default False , enable value to be null . 
- **blank** : default False , used with string types to allow inserting empty sstring in place consider it null . 
- **choices** : tuple of tuple ( (k , v) , (k , v) ..... ) .and in constructor use Person(name="Fred Flintstone", columdb_name= k ) . 
- **default** : can be value or callable , called every time object created .
- **help_text** : usefull for documentations . 
- **primary_key** : if set to True mecanisim of id will be overided otherwise django use id integer mecanisme by default . 
- **unique** : every row shall have unique value . 

