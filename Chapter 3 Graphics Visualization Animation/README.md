# Chapter 3: Graphics and visualization

##### Exercise 3.1
This program was a simple example of how to plot experimental data gathered in `sunspots.txt` and how to manipulate it.
##### Exercise 3.2
This program plots three functions: the deltoid curve, the galilean_spiral, 
and Fey's function. To accomplish this more easily, a polar plot coordinate
convert was also built.
##### Exercise 3.3
This program plots `stm.txt` which contains a grid of values from scanning tunneling
microscope measurements of the surface of silicon. It shows the structure of the surface
of silicon using a heatmap method.
##### Exercise 3.4
This program renders a sodium chloride crystal arranged on a cubic using two different colors to represent the two different atoms in 3-D.
This program also builds an fcc crystal lattice. 
##### Exercise 3.5
This program animates a 3-D model of the inner-most planets of the solar system 
with a scale factor to account for size and orbit to aid ease of visualization. This project does not use gravity equations; the spheres have no mass, and their orbits are as circular as the resolution allows. this project intends to showcase some OOD, 3-D modeling and animation as a light-weight representation of the planets with accurate ratios of planetary orbit to Sun's radius and Jupiter radius to planet's radius. The author does not intend this exercise to be orbital modeling but the practice of 3-D animation.
##### Exercise 3.6
This program calculates and displays the behavior of the logistic map of deterministic chaos as represented by the Feigenbaum. 
##### Exercise 3.7
This program calculates the Mandelbrot set in an NxN matrix grid and uses the heatmap plot function from pyplot to turn it into an image of the fractal.
##### Exercise 3.8
This program creates an object called `LeastSquareFit`; this object is a linear best fit line for experimental data in x and y with the following methods: 
- `chi_square`: gives the data's sum of the squares of the distances to the best fit line.
- `best_fit_line`: returns two arrays, one for the x values, and one for the best fit y values.
- `__finding_m_and_c`: an internal method, it is in charge of finding m and c values for the best fit line.

This program also uses data from the Millikan experiment, `millikan.txt` to test the program and to calculate Planck's constant as a final test of accuracy.

###### Link to all exercise questions in this chapter can be found [here](http://www-personal.umich.edu/~mejn/cp/exercises.html)