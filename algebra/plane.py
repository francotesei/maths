from sympy import solve,Plane as sPlane,symbols,Point,Line
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x,y,z = symbols('x,y,z');
class Plane:

    def __init__(self,general_equation_plane):
        self.input = general_equation_plane
        d = self.__valuePoint__(self.input,(0,0,0))
        x_normal = self.__valuePoint__(self.input,(1,0,0)) - d
        y_normal = self.__valuePoint__(self.input,(0,1,0)) - d
        z_normal = self.__valuePoint__(self.input,(0,0,1)) - d
        normal = (x_normal,y_normal,z_normal)
        z1 = solve(self.input.subs({x:1,y:1}),z)[0]
        self.point = (1,1,int(z1))
        self.plane = sPlane(self.point,normal_vector=normal)

    def equation(self):
        return self.plane.equation()

    def normal(self):
        n = self.plane.normal_vector
        return (int(n[0]),int(n[1]),int(n[2]))

    def is_normal(self,p):
        return self.plane.is_perpendicular(Line(Point(0,0,0),Point(p)))

    def is_include(self,point):
        return self.__valuePoint__(self.input,point) == 0

    def get_point(self):
        return self.point;

    def __valuePoint__(self,equation,p):
        array = np.asarray(p)
        return equation.subs([(x,array[0]),(y,array[1]),(z,array[2])])

    def show(self):
        point1  =  np.asarray(self.get_point())
        normal1 =  np.asarray(self.normal())
        # a plane is a*x+b*y+c*z+d=0
        # [a,b,c] is the normal. Thus, we have to calculate
        # d and we're set
        d1 = -np.sum(point1*normal1)# dot product
        # create x,y
        xx, yy = np.meshgrid(range(30), range(30))
        # calculate corresponding z
        z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
        # plot the surface
        plt3d = plt.figure().gca(projection='3d')
        plt3d.plot_surface(xx,yy,z1, color='blue')
        plt.show()
