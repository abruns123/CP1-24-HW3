"""
electricSphere uses information generated by the user to 
calculate the electric field at a point in space produced 
by a sphere with constant charge density placed at another
point in space.
"""
import numpy as np
def get_volume():
    """returns a function defining the volume of the sphere"""
    return lambda r:4/3*np.pi*r**3

def get_area():
    """returns a function defining the surface area of a sphere"""
    return lambda r: r**2*np.pi*4

def get_sep():
    """
    returns a function defining the separation vector
    between the center of the sphere and the point where
    electric field is measured
    """
    return lambda p,o: p-o

def get_qe():
    """
    Returns a function defining the charge enclosed by the sphere
    """
    return lambda cd,r: get_volume()(r)*cd


def get_vmag(v1):
    """getVMag returns the magnitude of a 3D vector"""
    return np.sqrt(v1[0]**2+v1[1]**2+v1[2]**2)

def get_uvec(v1,m):
    """getUVec returns the unit vector of vector v. m is the magnitude of that vector"""
    if m==0:
        return [0,0,0]
    return v1/m

def inside(r,v1):
    """inside determines whether or not the vector v has 
    greater magnitude r and returns either the magnitude of v or r
    """
    if r>=get_vmag(v1):
        return get_vmag(v1)
    return r

def get_field_mag(cd,r,m):
    """getFieldMag returns the magnitude of the electric field"""
    EPS=8.85*10**-12
    return get_qe()(cd,r)/(EPS*get_area()(m))

def zero_condition(v1):
    """zeroCondition returns a list with a number of elements 
    defined by whether or not the elements of v are zero.
    This way, the number of zero elements in the 
    separation vector may be known.
    """
    return [1 for i in v1 if i==0]

def elec_field(o,cd,r,p):
    """elecField returns a vector which defines the 
    electric field of a sphere which has its center 
    located at point o, a charge density cd, and a 
    radius r at point p.
    """

    m=get_vmag(get_sep()(p,o)) #m is the magnitude of the separation vector between p and o
    r=inside(r,get_sep()(p,o))
    #if point p is inside the sphere, the radius is
    # reduced to the magnitude of the separation vector

    if len(zero_condition(get_sep()(p,o)))==3:
    #if the separation vector is zero, a 3-dimensional zero vector is returned.

        return np.array([0,0,0])

    return get_field_mag(cd,r,m)*get_uvec(get_sep()(p,o),m)

def get_field(o,cd,r,p):
    """
    getField just puts the electric field into a string datatype
    such that it may be easily read by the user.
    """
    e=elec_field(o,cd,r,p)
    return (
        "The electric Field is defined by the vector\
 ["+str(e[0])+"x,", str(e[1])+"y,",str(e[2])+"z] V/m"
    )

if __name__=="__main__":
    """
    This main loop allows the user to make a
    sample calculation of an electric field
    of a sphere located at origin with charge density
    qd and radius rad at a point p in the x,y,z space.
    """
    origin=np.array([0,0,0])
    QD=1
    RAD=5
    po=np.array([.8,.9,.3])
    print(get_field(origin, QD, RAD, po))
