# import tkinter as tk
# from tkinter import font

# def press(num):
#     global expression
#     expression += str(num)
#     equation.set(expression)


# def equal_press():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression = total
#     except:
#         equation.set(" error ")
#         expression = ""

# def clear():
#     global expression
#     expression = ""
#     equation.set("")

# if __name__ == "__main__": 
#     root = tk.Tk()
#     root.title("Stylish Calculator")

#     expression = ""

#     equation = tk.StringVar()

#     window_width = 400
#     window_height = 500
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     position_top = int(screen_height/2 - window_height/2)
#     position_right = int(screen_width/2 - window_width/2)
#     root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
#     root.configure(bg="black", padx=20, pady=20)

#     entry_font = font.Font(size=20, weight='bold')
#     expression_field = tk.Entry(root, textvariable=equation, font=entry_font, bg="black", fg="white", bd=10, justify='right', relief='flat')
#     expression_field.grid(columnspan=4, ipadx=8, ipady=25, pady=20)

#     button_font = font.Font(size=18)

#     button_options = {
#         'bg': 'white', 'fg': 'black', 'font': button_font, 'bd': 1, 'relief': 'flat',
#         'width': 5, 'height': 2, 'highlightthickness': 0, 'activebackground': '#e0e0e0',
#         'borderwidth': 0
#     }

#     def create_button(text, row, col, cmd=None):
#         btn_frame = tk.Frame(root, bg='black', padx=10, pady=10)  
#         btn_frame.grid(row=row, column=col)
#         button = tk.Button(btn_frame, text=text, command=cmd, **button_options)
#         button.config(width=1, height=1) 
#         button.grid(sticky="nsew", ipadx=20, ipady=20)  

#     create_button('1', 2, 0, lambda: press(1))
#     create_button('2', 2, 1, lambda: press(2))
#     create_button('3', 2, 2, lambda: press(3))
#     create_button(' + ', 2, 3, lambda: press("+"))

#     create_button('4', 3, 0, lambda: press(4))
#     create_button('5', 3, 1, lambda: press(5))
#     create_button('6', 3, 2, lambda: press(6))
#     create_button(' - ', 3, 3, lambda: press("-"))

#     create_button('7', 4, 0, lambda: press(7))
#     create_button('8', 4, 1, lambda: press(8))
#     create_button('9', 4, 2, lambda: press(9))
#     create_button(' * ', 4, 3, lambda: press("*"))

#     create_button(' C ', 5, 0, clear)
#     create_button('0', 5, 1, lambda: press(0))
#     create_button(' = ', 5, 2, equal_press)
#     create_button(' / ', 5, 3, lambda: press("/"))

#     root.mainloop()

#write a program to implement the multilevel inheritence

# class Student:
#     def __init__(self, name, student_uid, phone_no):
#         self.name = name
#         self.student_uid = student_uid
#         self.phone_no = phone_no

#     def print_record(self):
#         print("Student Record:")
#         print(f"Name: {self.name}")
#         print(f"Student ID: {self.student_id}")
#         print(f"phone_no: {self.phone_no}")

# if __name__ == "__main__":
  
#     student1 = Student(name="david", student_uid="24mcc20034", phone_no="5198119156")

#     student1.print_record()

# write a program to implement the paramerterised funtion


#design make a admii

def subset_sum(S, subset, target_sum, index):
    # Check if the current subset's sum equals the target sum
    if sum(subset) == target_sum:
        print("Subset found:", subset)
        return

    # Stop if we've gone through all elements or if the subset's sum exceeds target
    if index >= len(S) or sum(subset) > target_sum:
        return

    # Recursive calls:
    # 1. Include the current element in the subset
    subset_sum(S, subset + [S[index]], target_sum, index + 1)
    # 2. Exclude the current element and move to the next
    subset_sum(S, subset, target_sum, index + 1)

def find_subsets(S, target_sum):
    S.sort()  # Sort to handle the set in order
    subset_sum(S, [], target_sum, 0)  # Start with an empty subset

# Define the input set and target sum
S = [1, 2, 5, 6, 8]
target_sum = 9

# Display the input set and target sum
print("Input Set: ", S)
print("Desired Target Sum: ", target_sum)
print("Possible subsets with sum equal to target:")

# Find and print subsets
find_subsets(S, target_sum)
