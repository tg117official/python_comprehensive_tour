import xml.etree.ElementTree as ET

# Parsing an existing XML file
tree = ET.parse('data/my_sample_xml.xml')  # Make sure you have a file named 'sample.xml'
root = tree.getroot()

# Display the root element (and its tag)
print(f"Root element: {root.tag}")

# Creating a new XML document from scratch
new_root = ET.Element("Library")  # Root element named 'Library'
book = ET.SubElement(new_root, "Book")  # Sub-element named 'Book'

# Adding attributes to elements
book.set('title', 'The Art of Programming')
book.set('author', 'Jane Doe')

# Creating sub-elements within 'Book'
chapter = ET.SubElement(book, "Chapter")
chapter.text = 'Introduction to XML with Python'

# Dumping the newly created XML to the console
ET.dump(new_root)
