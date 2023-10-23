import math
def euclidean_dist(x1, y1, x2, y2):
    xdiff = ((x2-x1)**2)
    ydiff = ((y2-y1)**2)
    retval = math.sqrt(xdiff+ydiff)
    return retval

a = euclidean_dist(1,1,2,2)
print(a)