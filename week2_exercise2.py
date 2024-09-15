""" The Mandelbrot set is a set of complex numbers defined by the sequence 
a(n) = a(n-1)**2 + c
a(0) = 0
 with thge complex number 
c = x + y*i

The number c is part of the Mandelbrot set when a(n) does not diverge to infinity. 
In python, c = complex(x,y) is often used. This Mandelbrot set is a fractal and 
can be visualized as in figure 1. We will be generating such an image. 
The black area of the image correspond to the number c for which a(n) did not diverge to infinity. 

Normally, we would see if the sequence a_n would diverge for n→∞, but we do not have enough time 
to check it for infinite numbers. For this reason, we assume that the sequence diverges to infinity
if |a_n |>2 and we call this n the diverging index. If we cannot find a diverging index less than 100, 
then we assume that the sequence diverges to infinity and the diverging index will be defined as 0. 

Your assignment is to draw a 200x200 image of the Mandelbrot set. The x range is [-1.5, 0.5] and 
the y range is [-1, 1]. Make a function draw_mandel(width) where width is the width and height of
the image (so it is always a square!). Use the diverging index as a colour representation of the pixel color. 

To start, divide this exercises in pieces. Make a list of functions (not a Python list) that needs 
to be made. Clearly define what the purpose of a function is and what its inputs and outputs are. 
If your tasks are clear, you can start coding. Communicating and collaboration for this assignment 
might be harder than the programming itself. 

Things to take into account:
1.	Work in Github from the start (mandatory)
2.	Create docstrings and type hints for your functions (mandatory)
3.	A numpy array can often be used as a representation of an image. With matplotlib, you can visualise 
    that image. Let someone do some research on working with images in Python.
4.	Note that the assignment is to draw a 200x200 image, but your function should be generic for any 
    squared image. Test your image also for 300x300, 500x500 and 800x800. 
    
In the end, you should have a draw_mandel(200) function call in your code.
"""