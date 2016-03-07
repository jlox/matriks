import math

def make_translate( x, y, z ):
    matrix = new_matrix(4, 4)
    ident(matrix)
    matrix[0][3] = x
    matrix[1][3] = y
    matrix[2][3] = z
    return matrix

def make_scale( x, y, z ):
    matrix = new_matrix(4, 4)
    ident(matrix)
    matrix[0][0]=x
    matrix[1][1]=y
    matrix[2][2]=z
    return matrix
    
def make_rotX( theta ):   
    matrix = new_matrix(4, 4)
    rads = math.radians(theta)
    matrix[0][0]=1
    matrix[1][1]=math.cos(rads)
    matrix[1][2]= -1 * math.sin(rads)
    matrix[2][1] = math.sin(rads)
    matrix[2][2] = math.cos(rads)
    return matrix

def make_rotY( theta ):
    matrix = new_matrix(4, 4)
    rads = math.radians(theta)
    matrix[0][2] = math.sin(rads)
    matrix[1][1] = 1
    matrix[2][0] = -1 * math.sin(rads)
    matrix[2][2] = math.cos(rads)
    return matrix

def make_rotZ( theta ):
    matrix = new_matrix(4, 4)
    rads = math.radians(theta)
    matrix[0][0] = math.cos(rads)
    matrix[0][1] = -1 * math.sin(rads)
    matrix[1][0] = math.sin(rads)
    matrix[1][1] = math.cos(rads)
    matrix[2][2] = 1
    return matrix

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    r = len(matrix)
    c = len(matrix[0])
    for ro in range(rows):
        s = str(matrix[r][0])
        for co in range(1, c):
            s += ", " + str(matrix[ro][co])
        print(s)

def ident( matrix ):
    r = len(matrix)
    c = len(matrix[0])
    for ro in range(r):
        for co in range(c):
            if(r==c):
                matrix[ro][co] = 1
            else:
                matrix[ro][co] = 0

def scalar_mult( matrix, x ):
    r = len(matrix)
    c = len(matrix[0])
    for ro in range(r):
        for co in range(c):
            matrix[ro][co] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    r = len(m1)
    c = len(m2[0])
    newie = new_matrix(r, c)
    l = len(m2)
    for ro in range(r):
        for co in range(c):
            res=0
            for i in range(l):
                res+=m1[ro][i] * m2[i][co]
            newie[ro][co] = res
    return newie
