#1.

x = "whata up Tim!"
print(x)

#2.

num1 = int(input("sheiyvanet cifri:"))
num2 = int(input("sheiyvanet cifri:"))
num3 = int(input("sheiyvanet cifri:"))
res = (num1 + num2 + num3) / 3
print(res)

#3.

for i in range(20,126,5):
    print(i)

#4.

ls = input("enter 10 numbers with commas:")
symbol = ","
res = ls.split(symbol)
print(res)

#5.

inp = input("sheiyvane ricxvi:")
inp = list(inp)
print(ls[0])

#6.

ls = [i**1 for i in range(0,101,2)]
print(sum(ls))

#7.

ls = [10,20,30,40,50]
ls.append(60)
ls.append(70)
ls.remove(10)
for i in ls:
    print(i)

print(len(ls))


#8.

ls = [i**3 for i in range(0,101,5)]
print(sum(ls) / len(ls))

#9.

x = int(input("sheiyvane pirveli ricxvi:"))
y = int(input("sheiyvane meore ricxvi:"))
z = int(input("sheiyvane mesame ricxvi:"))
if x < y and x < z:
    print(f"the smallest number is {x}")
elif y < x and y < z:
    print(f"the smallest number is {y}")
else:
    print(f"the smallest number is {z}")

#10.

x = input("sheiyvanet ricxvi da getyvi bolo cifrs:")
x = list(x)
x.reverse()
print(x[0] + " aris bolo cifri")