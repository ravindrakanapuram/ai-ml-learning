# strings in python are immutable sequences of characters bcz they cannot be changed after they are created
#but they support the operation like slicing indexing and concatenation othe built in methods like upper(), lower(), strip(), replace() etc.

#string creation

single_quote = 'Hello'
double_quote = "World"
multiple_lines = """ Hello this is multiple line string in python usage """

#Indexing 

text = "python"
first_char = text[0]
last_char = text[-1]

#slicing [start:stop:step] -> start is inclusive and stop is exclusive

greetings = "Hello, World!"
first_word = greetings[0:5]
every_second_char = greetings[::2] #skips every other character
reversed_string = greetings[::-1] #reverses the string

#string methods
dirty_string = "   Hello, Ravindra !   "
clean_string = dirty_string.strip() # remove the spaces 

csv_data = "Kanapuram , Ravindra , Reddy"
first_name, middle_name, last_name  = csv_data.split(",") #splits the string into a list of substrings based on the comma delimiter
#above one converts to the list of strings and we can unpack the list into individual variables
name_list = csv_data.split(",") #splits the string into a list of substrings based on the comma delimiter

joined_string = "&".join(name_list) #joins the list of strings into a single string with the specified delimiter

replaced_string = greetings.replace("World", "Python") #replaces the substring "World" with "Python"

shout = greetings.upper() #converts the string to uppercase
whisper = greetings.lower() #converts the string to lowercase

check_start = greetings.startswith("Hello") #checks if the string starts with "Hello"
check_end = greetings.endswith("!") #checks if the string ends with "!"

# membership testing 
sentence = "Python is a great programming language."
contains_python = "Python" in sentence #checks if "Python" is present in the sentence
contains_java = "Java" in sentence #checks if "Java" is present in the sentence

#f strings

name = "Ravindra"
age = 25
profile = f"My name is {name} and I am {age} years old." #f-string allows you to embed expressions inside string literals using curly braces {}

# string normalization
#unicode allows you to represent characters from different languages and scripts using a standardized encoding. However, some characters can be represented in multiple ways, which can lead to inconsistencies when comparing or processing strings. String normalization is the process of converting strings to a standard form to ensure consistent representation.
import unicodedata
string_composed = "Café"  # 'é' is a single character
string_decomposed = "Café"  # 'e' followed by a combining acute accent
normalized_composed = unicodedata.normalize("NFC", string_composed)
normalized_decomposed = unicodedata.normalize("NFD", string_decomposed) 
