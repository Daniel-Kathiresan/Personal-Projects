#Daniel Kathiresan


#Page number + offset calculator
#Page number = (address reference / page size)-starting page size
#Offset = (address reference % page size)
#Starting page size
d = float(input("Enter Address Decimal: "))
ps =int(input("Enter Page Size (KB): "))
sps =int(input("Page Start (EG;0): "))
ps = (1024 * ps)
pn = ((d/float(ps))-(sps+1))
os = ((d%float(ps)))
print("Page number = ",pn)

print("Page offset = ",os)
print("page number hex = ",hex(int(os)))
