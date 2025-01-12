from typing import Optional

def spi( name: str | int, ):
    return(name)

a = spi(90)

print(type(a))

def api(name: Optional[str | None] = None):
    return(name)

b = api(["ritesh","Bhavesh",'Lucky'])
c = api([])
print(c)
d =api()
print(d)
print(b)




