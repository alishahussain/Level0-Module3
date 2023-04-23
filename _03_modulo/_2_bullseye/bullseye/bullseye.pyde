def setup():
    size(500,500)
    pass

def draw():
    s=400
    for i in range(5):
        s-=80
        if i%2==1:
            fill(255,0,0)
        else:
            fill(100,255,0)
        ellipse(250,250,s,s)
