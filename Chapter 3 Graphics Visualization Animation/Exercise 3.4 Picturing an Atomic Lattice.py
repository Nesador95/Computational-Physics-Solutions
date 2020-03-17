# Done

import vpython as vp
# part a
def sodium_chloride_lattice(lenght_of_side):
    L = lenght_of_side
    R = 0.3
    count = 1
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if count%2 == 0:
                    vp.sphere(pos=vp.vector(i,j,k), radius=R, color=vp.color.cyan)
                else:
                    vp.sphere(pos=vp.vector(i,j,k), radius=R, color=vp.color.red)
                count+=1     

# sodium_chloride_lattice(5)

# part b

def fcc_lattice(lenght_of_side):
    L = lenght_of_side
    R = 0.3
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                vp.sphere(pos=vp.vector(i,j,k), radius=R, color=vp.color.purple)
                vp.sphere(pos=vp.vector(i+0.5,j+0.5,k), radius=R, color=vp.color.purple)
                vp.sphere(pos=vp.vector(i,j+0.5,k+0.5), radius=R, color=vp.color.purple)
                vp.sphere(pos=vp.vector(i+0.5,j,k+0.5), radius=R, color=vp.color.purple)
 fcc_lattice(5)