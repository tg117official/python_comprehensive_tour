import re

text = """Alice was born on 1990-05-20 in New York.
Bob's email is bob@example.com.
The project deadline is approaching: 2024-07-31.
John's phone numbers are 321-555-4321, 123.555.1234
, 123*555*1234
, 800-555-1234
, 900-555-1234.
cat
mat
pat
bat
Mr. John
Mr James
Mr Sunder
Mr. Satya
Ms Dibya
Mrs. Ashwini
Mr. A

emails = 
thisIsSample@gmail.com
IamStudent@university.edu
my-117-business@my-work.net

https://www.google.com
http://technologicalgeeks.in
https://youtube.com
https://www.nasa.gov

"""
pattern = re.compile(r'')
matches = pattern.finditer(text)

for match in matches :
    print(match)