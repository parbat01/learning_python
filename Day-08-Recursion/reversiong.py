#In this program i'll reverse the string using recursion.
def reverse(name):
    if len(name)==1:
        return name
    else:
        return reverse(name[1:])+name[0]
print(reverse("parbat"))