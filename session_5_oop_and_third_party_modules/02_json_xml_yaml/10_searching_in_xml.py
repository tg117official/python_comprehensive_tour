import xml.etree.ElementTree as ET

# Parse an existing XML file
tree = ET.parse('data/my_sample_xml.xml')  # Ensure this file exists and is properly formatted
root = tree.getroot()

# Using 'find()' to find the first 'Book' element
first_book = root.find('Book')
if first_book is not None:
    print("First Book Title:", first_book.get('title'))

# Using 'findall()' to find all 'Book' elements with a specific author
books_by_author = root.findall(".//Book[@author='Mark Lutz']")
print("Books by Mark Lutz:")
for book in books_by_author:
    print(book.get('title'))

# Using 'iter()' to iterate over all 'Chapter' elements in the document
print("All Chapters in the Document:")
for chapter in root.iter('Chapter'):
    print(chapter.text)

# Combining 'findall()' and XPath to find all chapters in books by 'Joshua Bloch'
print("Chapters in books by Joshua Bloch:")
books = root.findall(".//Book[@author='Joshua Bloch']")
for book in books:
    chapters = book.findall('Chapter')
    for chapter in chapters:
        print(chapter.text)

# ET.parse('sample.xml') and getroot():
#       These lines load the XML from a file and retrieve the root element of
#       the XML tree.
#
# find('Book'):
#       This function searches for the first child with the specified tag directly
#       under the specified element (in this case, the root).
#       It returns a single element, or None if no matching element is found.
#
# findall(".//Book[@author='Mark Lutz']"):
#       This function uses an XPath expression to find all elements that match the
#       criteria.
#       Here, it finds all <Book> elements anywhere in the document that have an
#       author attribute equal to 'Mark Lutz'.
#
# iter('Chapter'):
#       This method creates a generator that iterates over all elements with the
#       specified tag (Chapter) in the entire XML tree.
#       It is useful for processing all occurrences of a particular type of element.
#
# findall('Chapter') within the loop:
#       Inside the loop, this method finds all <Chapter> elements that are children
#       of each <Book> element found by the previous query.
