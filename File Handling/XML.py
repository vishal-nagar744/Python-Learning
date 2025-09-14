# A) Create & Write XM

import xml.etree.ElementTree as ET

students = [
    {"name": "Honey", "roll": 1, "marks": 95.5},
    {"name": "Vishal", "roll": 2, "marks": 88.0},
]

root = ET.Element("students")

for s in students:
    stu = ET.SubElement(root, "student", attrib={"roll": str(s["roll"])})
    name = ET.SubElement(stu, "name")
    name.text = s["name"]
    marks = ET.SubElement(stu, "marks")
    marks.text = str(s["marks"])

tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)
print("XML written: students.xml")



# B) Read/Parse XML

import xml.etree.ElementTree as ET

tree = ET.parse("students.xml")
root = tree.getroot()             # <students>

for stu in root.findall("student"):
    roll = int(stu.get("roll"))   # attribute
    name = stu.find("name").text  # child text
    marks = float(stu.find("marks").text)
    print(roll, name, marks)


# C) Update XML (change node text / add new)

import xml.etree.ElementTree as ET

tree = ET.parse("students.xml")
root = tree.getroot()

# Update marks where roll=2
target = root.find("student[@roll='2']")
if target is not None:
    target.find("marks").text = "90.0"

# Add a new student
new_stu = ET.SubElement(root, "student", attrib={"roll": "3"})
ET.SubElement(new_stu, "name").text = "Aditi"
ET.SubElement(new_stu, "marks").text = "76.5"

tree.write("students.xml", encoding="utf-8", xml_declaration=True)
print("XML updated.")
