#Quadrant 
def find_quadrant(x,y):
    if x>0 and y >0:
        return "Quadrant 1 (Q1)"
    elif x<0 and y>0:
        return "Quadrant 2 (Q2)" 
    elif x<0 and y<0:
        return "Quadrant 3 (Q3)"
    elif x>0 and y<0:
        return "Quadrant 4 (Q4)"
    elif x==0 and y!=0:
        return "on the Y-axis"
    elif y==0 and x!=0:
        return "on the X-axis"
    else:
        return "At the origin"
    
x=int(input("enter X coordinate: "))
y=int(input("enter Y coordinate: "))

print(f" The point ({x}, {y}) lies in : {find_quadrant(x,y)}")