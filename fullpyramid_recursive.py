def printspaces(space):
    if space > 0:
        print(" ", end="")
        printspaces(space-1)

def printstars(star):
    if star > 0:
        print("*", end="")
        printstars(star-1)

def printpyramid(n, currentrow = 1):
    if currentrow > n:
        return

    space = n - currentrow
    star = 2 * currentrow - 1

    printspaces(space)
    printstars(star)
    print()

    printpyramid(n, currentrow + 1)

n = 5

printpyramid(n)
