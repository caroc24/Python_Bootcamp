line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
column = position[0]
row = position[1]
x_column = 0
x_row = 0

if column == "A":
  x_column = 0
elif column == "B":
  x_column = 1
else:
  x_column = 2

if row == "1":
  x_row = 0
elif row == "2":
  x_row = 1
else:
  x_row = 2
  
map[x_row][x_column] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")