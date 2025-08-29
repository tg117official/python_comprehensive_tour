import xml.etree.ElementTree as ET

# Load the XML file from disk
tree = ET.parse('data/my_sample_xml.xml')
root = tree.getroot()

# Print out the root element's tag
print("Root element:", root.tag)

# Iterate over each 'Book' in the 'Library'
for book in root.findall('Book'):
    # Access and print the 'title' and 'author' attributes of each 'Book'
    title = book.get('title')
    author = book.get('author')
    print(f"Book title: {title}, Author: {author}")

    # Iterate over each 'Chapter' within the 'Book'
    for chapter in book.findall('Chapter'):
        # Print the text content of each 'Chapter'
        print("Chapter:", chapter.text)

# Find the first book with the title 'Learning Python' and print its details
python_book = root.find(".//Book[@title='Learning Python']")
if python_book is not None:
    print("\nDetails of 'Learning Python':")
    print("Author:", python_book.get('author'))
    for chapter in python_book.findall('Chapter'):
        print("Chapter:", chapter.text)

# import xml.etree.ElementTree as ET: This line imports the XML parsing module.
#
# ET.parse('sample.xml'):
#       Parses the XML file named sample.xml and returns a tree structure.
#
# getroot():
#       Retrieves the root element of the tree (in this case, <Library>).
#
# findall('Book'):
#       Finds all child elements with the tag <Book> directly under the root.
#       It returns a list of elements.
#
# get('title') and get('author'):
#       These methods retrieve the value of the specified attribute from the element.
#
# findall('Chapter'):
#       Finds all <Chapter> elements under each <Book>.
#       This is used to iterate over chapters within each book.
#
# find(".//Book[@title='Learning Python']"):
#       Demonstrates a more complex search using XPath to find the first <Book>
#       element that has a title attribute of "Learning Python".
#       This is useful for accessing specific elements quickly.
