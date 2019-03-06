try:
    x = float(input("factorial ra vared kon: "))
    y = float(input("amel aval ra vared kon: "))
    if y < 0:
        print("faghat a\'dad mosbat bzn baraye amel aval")
except:
    print("mosbat bzn")

if y == 0:
    y = 5
else:
    pass

try:
    tavan = 1
    l = []
    z = y
    while True:
        t = x / z
        #print(t)
        tavan += 1
        #print(tavan)
        z = y**tavan
        t = int(t)
        l.append(t)
        if t == 0:
            print(l)
            break

except Exception as err:
    print("error", err)

j = 0
for i in l:
    j += i

print("answer: ",j)
