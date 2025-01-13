from datetime import date, datetime, time
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

def abi(name: Optional[dict | None ]= None):
    return (name)

f = abi({"Name": "Ritesh","age":25, "class": "btech 4th year"})

print(f["Name"] )   # same for tuple and set are use make sure 
                    # always first give datastructur and datastructur 
                    # type always in square bracket ex like list[int,str]
                    # tuple[str,int,float, None]. dict[str, float]
                    # instead of giving type like tuple we can give like
                    # tuple[str | int | bool]

g = datetime.now().time()
print(g.replace(microsecond=0))
 



