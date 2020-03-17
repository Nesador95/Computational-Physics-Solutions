# Done
import vpython as vp
import numpy as np
###############################################################################
# Set up
###############################################################################
class celestial_body:
    def __init__(self,color_of_body,radius_of_body, position):
        self.body = vp.sphere(color=color_of_body, \
                                radius=radius_of_body,\
                                pos=position, canvas=scene, make_trail=True,retain=10)
        self.position = position
    
    def orbit(self, theta, delta_time):
            new_position = vp.vector(np.cos(theta), np.sin(theta),0)
            self.body.pos = self.body.pos + new_position* delta_time
caption = """This animation was intended to show how one may make 3-D models of physical events. 
The model uses 2 different scales: the sun radius is taken as the unit vector of 10 lenght
the orbits of the planets are then derived by dividing the radius of the real sun and the planet's orbit
to get the ratio of the two. The second scale is for the sizes of the planets. Here Jupiter's radius was taken as
as the unit vector of lenght of 5, that is 50 percent smaller than then sun instead of the closer value of 10 percent
to allow all other planets to be visible. This simulation takes all orbits to be spherical by dividing the unit circle into
100 parts and updating the orbits with those values as well as a time delta to allow the planets to update their orbits at different rates,
This keeps them from running into eachother; this in turn means that the period of the orbits is not accurately represented here 
and since gravitational equations are not used either, the longer the program runs the more likely it is for the orbits to migate out of position."""
scene = vp.canvas(title="        Model of the First 5 Planets of the Solar System",\
                    width=1366,height=768, x=10,y=10,caption= caption)
scene.select()
###############################################################################
# Rendering Stage
###############################################################################
sun_radius= 10
jupiter_radius = 5

Sun = celestial_body(vp.color.yellow, sun_radius, vp.vector(0,0,0))
Mercury = celestial_body(vp.color.orange,jupiter_radius*0.035273879,\
                         vp.vector(0,-sun_radius+(-sun_radius*0.083249461),0))
Venus = celestial_body(vp.color.purple,jupiter_radius*0.087490784,\
                       vp.vector(0,-sun_radius+(-sun_radius*0.155571531),0))
Earth = celestial_body(vp.color.blue,jupiter_radius*0.09210241,\
                       vp.vector(0,-sun_radius+(-sun_radius*0.210783609),0))
Mars = celestial_body(vp.color.red,jupiter_radius*0.048949735,\
                       vp.vector(0,-sun_radius+(-sun_radius*0.32767793),0))
Jupiter = celestial_body(vp.color.magenta,jupiter_radius,\
                       vp.vector(0,-sun_radius+(-sun_radius*1.119338605),0))
Saturn = celestial_body(vp.color.white,jupiter_radius*0.828589189,\
                       vp.vector(0,-sun_radius+(-sun_radius*2.060963336),0))
###############################################################################
# Animation Stage
###############################################################################

time = 0
while time < 10:
    delta_time = 0.11
    for theta in np.arange(0,2*np.pi,0.01):
        vp.rate(60)
        Mercury.orbit(theta,delta_time)
        Venus.orbit(theta, delta_time+0.01)
        Earth.orbit(theta,delta_time+0.02)
        Mars.orbit(theta,delta_time+0.03)
        Jupiter.orbit(theta,delta_time+0.12)
        Saturn.orbit(theta,delta_time+0.21)
    time += delta_time