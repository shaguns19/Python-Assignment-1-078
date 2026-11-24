marks = [float(input(f"Enter marks for subject {i}: ")) for i in range(1, 6)]
total = sum(marks)
average = total / 5
print("Total marks =", total)
print("Average marks =", average)
