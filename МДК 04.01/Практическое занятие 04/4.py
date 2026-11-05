n = int(input("количество школьников: "))
k = int(input("количество мандаринов: "))

integer = k // n
remains = k % n

print(f"каждый школьник получит {integer} мандаринов, в корзине останется {remains}")