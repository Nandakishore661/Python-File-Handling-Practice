# Python File Handling Practice Tasks 
# Task 1 – Create and Write 

file = open("notes.txt", "w")

file.write("Python is a programming language.\n")
file.write("Python is easy to learn.\n")
file.write("Python is used in AI and web development.\n")

file.close()

print("Data written successfully")

# Create a file named notes.txt and write three lines about Python using write(). 

file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()


# Task 2 – Read the Whole File 
# Open notes.txt in read mode and display the entire contents using read(). 

file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()

# Task 3 – Read One Line 
# Create a file named students.txt containing at least five student names. Use readline() to display only the  first line. 

file = open("students.txt", "w")

file.write("Nanda\n")
file.write("Rahul\n")
file.write("Kiran\n")
file.write("Arjun\n")
file.write("Ravi\n")

file.close()

file = open("students.txt", "r")

data = file.readline()

print(data)

file.close()

# Task 4 – Read Line by Line 
# Using readline(), display the first three lines of students.txt, one line at a time. 

file = open("students.txt", "r")

print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")

file.close()

# Task 5 – Read All Lines 
# Use readlines() to read all lines from students.txt and print the returned list. 

file = open("students.txt", "r")

data = file.readlines()

print(data)

file.close()

# Task 6 – Count Lines 
# Use readlines() to find and display the total number of lines in a file named story.txt. 

file = open("story.txt", "r")

data = file.readlines()

count = len(data)

print("Total number of lines:", count)

file.close()


# Task 7 – Write Multiple Lines 
# Use write() to store a student's name, age, course, and city on separate lines in student_details.txt. 

file = open("student_details.txt", "w")

file.write("Name: Nanda\n")
file.write("Age: 22\n")
file.write("Course: Python\n")
file.write("City: Hyderabad\n")

file.close()

print("Student details saved successfully")


# Task 8 – Append a New Record 
# Open student_details.txt in append mode and add a new student's details without deleting the existing  content. 

file = open("student_details.txt", "a")

file.write("Name: Rahul\n")
file.write("Age: 23\n")
file.write("Course: Java\n")
file.write("City: Bangalore\n")

file.close()

print("New student record added")



# Task 9 – Append Multiple Lines 
# Use writelines() to append three new lines to a file named daily_log.txt. Ensure each line ends with a  newline character. 

file = open("daily_log.txt", "a")

data = [
    "Completed Python practice\n",
    "Learned file handling\n",
    "Practiced SQL queries\n"
]

file.writelines(data)

file.close()

print("Daily log updated")


# Task 10 – Write a List of Lines 
# Create subjects.txt and use writelines() to write a list of five subject names, each on a separate line. 

file = open("subjects.txt", "w")

subjects = [
    "Python\n",
    "Java\n",
    "SQL\n",
    "HTML\n",
    "CSS\n"
]

file.writelines(subjects)

file.close()

print("Subjects saved successfully")


# Task 11 – Understand Write Mode 
# Create a file with some text, reopen it using w mode, write different text, and then read the file to observe  what happened to the old content. 

# First create a file
file = open("test.txt", "w")
file.write("This is old content")
file.close()

# Reopen using write mode
file = open("test.txt", "w")
file.write("This is new content")
file.close()

# Read the file
file = open("test.txt", "r")
print(file.read())
file.close()

# Task 12 – Understand Append Mode 
# Create a file with two lines, append two more lines using a mode, and verify that all four lines remain. 

file = open("append.txt", "w")

file.write("Line 1\n")
file.write("Line 2\n")

file.close()

file = open("append.txt", "a")

file.write("Line 3\n")
file.write("Line 4\n")

file.close()

file = open("append.txt", "r")

print(file.read())

file.close()

# Task 13 – Exclusive Creation 
# Use x mode to create a new file named unique.txt and write a message into it. Run the program again and  observe what happens if the file already exists.

try:
    file = open("unique.txt", "x")

    file.write("This is a unique file.")
    file.close()

    print("File created successfully")

except FileExistsError:
    print("File already exists")

# Task 14 – Handle a Missing File 
# Try to open a file named missing.txt in r mode. Handle the situation gracefully if the file does not exist. 

try:
    file = open("missing.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("File does not exist")

# Task 15 – Copy File Contents 
# Read all contents from source.txt using read() and write them into a new file named copy.txt. 

# Read source file
file = open("source.txt", "r")

data = file.read()

file.close()

# Write into another file
file = open("copy.txt", "w")

file.write(data)

file.close()

print("File copied successfully")

# Task 16 – Copy Lines Using readlines() 
# Read the lines from source.txt using readlines() and write them into backup.txt using writelines(). 

file = open("source.txt", "r")

data = file.readlines()

file.close()

file = open("backup.txt", "w")

file.writelines(data)

file.close()

print("Backup created successfully")


# Task 17 – Search for a Word 
# Read a file named article.txt and check whether a word entered by the user appears in its contents. 

file = open("article.txt", "r")

data = file.read()

file.close()

word = input("Enter a word to search: ")

if word.lower() in data.lower():
    print("Word found in the file")
else:
    print("Word not found in the file")
    
    
    
# Task 18 – Count Words 
# Use read() to read paragraph.txt and display the number of words in the file. 

file = open("paragraph.txt", "r")

data = file.read()

words = data.split()

count = len(words)

print("Total words:", count)

file.close()


# Task 19 – Simple Notes Manager 
# Create a menu-driven program that lets the user write new notes, append a note, or display all notes. Use  w, a, and r modes. 

while True:

    print("\n----- NOTES MANAGER -----")
    print("1. Write New Notes")
    print("2. Append a Note")
    print("3. Display All Notes")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        file = open("notes.txt", "w")

        note = input("Enter your note: ")

        file.write(note + "\n")

        file.close()

        print("New note saved successfully")

    elif choice == 2:

        file = open("notes.txt", "a")

        note = input("Enter your new note: ")

        file.write(note + "\n")

        file.close()

        print("Note added successfully")

    elif choice == 3:

        try:
            file = open("notes.txt", "r")

            data = file.read()

            print("\nYour Notes:")
            print(data)

            file.close()

        except FileNotFoundError:
            print("No notes found")

    elif choice == 4:

        print("Thank you for using Notes Manager")
        break

    else:

        print("Invalid choice")
        
        
# Task 20 – Student Records File 
# Create a program that stores multiple student names and marks in marks.txt using write() or writelines().  Then read the file and display every record. Add one more record using append mode. 


# Store student records
file = open("marks.txt", "w")

file.write("Nanda - 85\n")
file.write("Rahul - 90\n")
file.write("Kiran - 78\n")

file.close()

# Display student records
file = open("marks.txt", "r")

print("Student Records:")
print(file.read())

file.close()

# Append a new record
file = open("marks.txt", "a")

name = input("Enter student name: ")
marks = input("Enter student marks: ")

file.write(name + " - " + marks + "\n")

file.close()

print("New record added successfully")

# Display updated records
file = open("marks.txt", "r")

print("\nUpdated Student Records:")
print(file.read())

file.close()

