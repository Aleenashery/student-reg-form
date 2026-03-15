from tkinter import *

# Create main window
root = Tk()
root.title("Student Registration Form")
root.geometry("400x450")

# Title label
title = Label(root, text="Student Registration Form", font=("Arial", 16))
title.pack()

# Name
name_label = Label(root, text="Student Name")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# Email
email_label = Label(root, text="Email")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

# Phone
phone_label = Label(root, text="Phone Number")
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

# Gender
gender_label = Label(root, text="Gender")
gender_label.pack()

gender = StringVar()

male = Radiobutton(root, text="Male", variable=gender, value="Male")
male.pack()

female = Radiobutton(root, text="Female", variable=gender, value="Female")
female.pack()

# Course
course_label = Label(root, text="Course")
course_label.pack()

course_list = Listbox(root)
course_list.insert(1, "BSc Computer Science")
course_list.insert(2, "BSc Mathematics")
course_list.insert(3, "BCA")
course_list.insert(4, "BCom")
course_list.pack()

# Submit button
submit_button = Button(root, text="Submit")
submit_button.pack()

# Run the window
root.mainloop()
