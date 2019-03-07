try:
    x = int(input("factorial ra vared kon: "))
    y = int(input("amel aval ra vared kon: "))
    if y > 0 or y == 0 and x > 0 or x == 0:
        print("wait a sec")
    else:
        print("Adad mosbat bzn")
        exit()
except ValueError:
    print("Adad bedon a\'shar VARED kn")
    exit()

if y == 0:
    y = 5

tavan = 1
li = []
z = y
while True:
    t = x / z
    tavan += 1
    z = y**tavan
    t = int(t)
    li.append(t)
    if t == 0:
        print(li)
        break

j = 0
for i in li:
    j += i

print("answer: ", j)
