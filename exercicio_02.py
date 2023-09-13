h1=int(input("quantas horas vc passou lá? "))
m1=int(input("quantos minutos vc passou lá? "))
print(f"você ficou por {h1}:{m1}")

h2=int(input("de que horas você chegou lá? "))
m2=int(input("de que minutos você chegou lá? "))
print(f"você chegou as {h2}:{m2}")

htemp=0

if h1>12:
    h1=(h1-12)

if h2>12:
    h2=(h2-12)

totalm=m1+m2

if totalm>=60:
    totalm=totalm-60
    htemp = 1

totalh= h1+h2+htemp

if totalh>12:
    totalh=totalh-12

print(f"você saiu as {totalh}:{totalm}")
