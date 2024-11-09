def likes(names):
    # your code here
    if names == []:
        return f"no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    if len(names) > 3:
        num = len(names) - 2
        return f"{names[0]}, {names[1]} and {num} others like this"
        