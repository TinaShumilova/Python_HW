def kort(s: str) -> tuple:
    *a, b = s.split("/") 
    b, c = b.split(".")
    result = (a, b, c)
    return result

s = "D:/studying/GeekBrains/Python/Homeworks/work.txt"
print(kort(s))