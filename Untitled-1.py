print("Hello, welcome to RS Minimart")
menulist = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]
print("Menu", menulist)
price = [8.99, 5.49, 7.99, 4.99, 12.99]
i = 0
while i < len(menulist):
    print(menulist[i],":",price[i])
    i = i+1
def takeorder():
    print("thank you for your order", "your bill will be", orderprice)   
order = input("what will be your order:")
if order == menulist[0]:
    orderprice=price[0]
    takeorder()
if order == menulist[1]:
    orderprice=price[1]
    takeorder() 
if order == menulist[2]:
    orderprice=price[2]
    takeorder() 
if order == menulist[3]:
    orderprice=price[3]
    takeorder() 
if order == menulist[4]:
    orderprice=price[4]
    takeorder() 
else: 
    print("you stupid look at the menu")
