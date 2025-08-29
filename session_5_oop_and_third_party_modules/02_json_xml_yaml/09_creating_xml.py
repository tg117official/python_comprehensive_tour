import xml.etree.ElementTree as ET

# Create the root element 'Library'
library = ET.Element('Library')

# Add a new 'Book' element to 'Library'
book1 = ET.SubElement(library, 'Book')

# Set attributes for 'Book'
book1.set('title', 'Learning Python')
book1.set('author', 'Mark Lutz')

# Add chapters to 'Book'
chapter1 = ET.SubElement(book1, 'Chapter')
chapter1.text = 'Introduction to Python'
chapter2 = ET.SubElement(book1, 'Chapter')
chapter2.text = 'Advanced Python Techniques'

# Add another 'Book' element to 'Library'
book2 = ET.SubElement(library, 'Book')
book2.set('title', 'Effective Java')
book2.set('author', 'Joshua Bloch')

# Add chapters to the second 'Book'
chapter3 = ET.SubElement(book2, 'Chapter')
chapter3.text = 'Java Platform'
chapter4 = ET.SubElement(book2, 'Chapter')
chapter4.text = 'Generics in Java'

# Convert the XML structure back to a string and print it
tree = ET.ElementTree(library)
tree.write('data/output.xml')  # Optionally, save the tree to a file

# Alternatively, print the XML to the console
import xml.dom.minidom
xmlstr = xml.dom.minidom.parseString(ET.tostring(library)).toprettyxml(indent="   ")
print(xmlstr)

# ET.Element('Library'):
#       Creates the root element with the tag 'Library'.
#       This will be the top-level element in our XML structure.
#
# ET.SubElement(library, 'Book'):
#       Creates a new child element under the specified parent.
#       Here, 'Book' is created as a child of 'Library'.
#
# set('title', '...') and set('author', '...'):
#       These methods are used to add or modify attributes in an XML element.
#       They key-value pairs represent the attribute name and its value, respectively.
#
# ET.SubElement(book1, 'Chapter'):
#       Adds 'Chapter' elements under 'Book'.
#       Each chapter is a child element of 'Book'.
#
# chapter1.text = 'Introduction to Python':
#       Sets the text content of the 'Chapter' element, which can be the title or any
#       other relevant information.
#
# ET.ElementTree(library):
#       Wraps the entire 'Library' element (and its children) into an ElementTree
#       object, which can then be manipulated or saved.
#
# tree.write('output.xml'):
#       Saves the XML document to a file named 'output.xml'.
#       This step is optional if you want to keep the XML in memory or print it
#       directly.
#
# Printing the XML:
#       The script uses xml.dom.minidom to convert the XML into a string with
#       proper indentation and formatting, which is then printed to the console.
#       This is useful for debugging or displaying the constructed XML in a readable
#       format.
