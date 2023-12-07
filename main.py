import random
import tkinter as tk
from tkinter import messagebox

#set up the window
window = tk.Tk()
window.title("Matching Game")
window.geometry("400x400")



#empty lists and variables for row and column functions
number = 0
column_list = []
row_list = []

#matches to be shuffled
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
#shuffles matches list
random.shuffle(matches)

#empty lists and variables for button functions
count = 0
answer_list = []
answer_dict = {}

#function for clicking buttons
def onClick(l, num):
  global count, answer_list, answer_dict

  if l["text"] == " " and count < 2:
    l["text"] = matches[num]
    #add number to answer list
    answer_list.append(matches[num])
    #keep track of button clicks
    answer_dict[l] = matches[num]
    #increment counter
    count += 1

  #what happens when answers match
  if len(answer_list) == 2:
    if answer_list[0] == answer_list[1]:
      #cards stay up and can not be clicked
      for key in answer_dict:
        key["state"] = "disabled"
        count = 0
      answer_list = []
      answer_dict = {}

    #when cards do not match
    else:
      #messagebox appears when answers do not match
      messagebox.showinfo("Incorrect", "Incorrect")
      #cards "flip" back over
      for key in answer_dict:
        key["text"] = " "
      answer_dict = {}
      count = 0
      answer_list = []
      
#generates random number for the row
def generate_row():
  global number
  
  list = [0, 1, 2]
  for i in range(3):
    number = number + random.choice(list)
    list.remove(number)
    row_list.append(number)
    number = 0
    
#generates random number for the column
def generate_column():
  global number
  
  list = [0, 1, 2, 3]
  for i in range(4):
    number = number + random.choice(list)
    list.remove(number)
    column_list.append(number)
    number = 0


#calls the function of generate column
generate_column()
c1 = column_list[0]
c2 = column_list[1]
c3 = column_list[2]
c4 = column_list[3]

#calls the function of generate row
generate_row()
r1 = row_list[0]
r2 = row_list[1]
r3 = row_list[2]


#the buttons that are on the grid
l1 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l1, 0))
l1.grid(row = r1, column = c1)
l2 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL,command=lambda: onClick(l2, 1))
l2.grid(row = r2, column = c2)
l3 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l3, 2))
l3.grid(row = r3, column = c3)
l4 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l4, 3))
l4.grid(row = r1, column = c4)
l5 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l5, 4))
l5.grid(row = r2, column = c1)
l6 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l6, 5))
l6.grid(row = r3, column = c2)
l7 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l7, 6))
l7.grid(row = r1, column = c3)
l8 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l8, 7))
l8.grid(row = r2, column = c4)
l9 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l9, 8))
l9.grid(row = r3, column = c1)
l10 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l10, 9))
l10.grid(row = r1, column = c2)
l11 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l11, 10))
l11.grid(row = r2, column = c3)
l12 = tk.Button(window, text = " ", padx = 30, pady = 40, state=tk.NORMAL, command=lambda: onClick(l12, 11))
l12.grid(row = r3, column = c4)