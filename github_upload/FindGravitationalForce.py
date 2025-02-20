# Logan Richan
# ph295

print("What is the mass of object 1?")
m1 = float(input())
print("What is the mass of object 2?")
m2 = float(input())
print("What is the distance between the two objects?")
r = float(input())

G = 6.673e-11
F = G*m1*m2/(r**2)

print("The force is: ", F, "Newtons")
