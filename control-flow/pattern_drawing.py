size = int(input("Enter the size of the pattern:"))
width = size

while size > 0:
    col = 0
    while col < width:
        print("*", end="")
        col += 1
    size -= 1
    print("")
