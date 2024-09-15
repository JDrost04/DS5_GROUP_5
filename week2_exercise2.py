import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter) -> int:
    """_summary_

    Args:
        c (_type_): _description_
        max_iter (_type_): _description_

    Returns:
        int: _description_
    """
    a = 0
    for n in range(max_iter):
        if abs(a) > 2:
            return n
        a = a**2 + c
    return max_iter


def mandelbrot_set(xmin, xmax, ymin, ymax, width, max_iter) -> np.ndarray:
    """_summary_

    Args:
        xmin (_type_): _description_
        xmax (_type_): _description_
        ymin (_type_): _description_
        ymax (_type_): _description_
        width (_type_): _description_
        max_iter (_type_): _description_

    Returns:
        np.ndarray: _description_
    """    
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, width)
    mset = np.zeros((width, width))
    
    for i in range(width):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iter)
    
    return mset
   

def draw_mandel(width: int):
    """_summary_

    Args:
        width (int): _description_
    """    
    xmin, xmax, ymin, ymax = -1.5, 0.5, -1, 1
    max_iter = 100

    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, max_iter)

    plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='inferno')
    plt.colorbar()
    plt.title(f'Mandelbrot Visualization (Resolution: {width}x{width})')
    plt.xlabel('Real(c)')
    plt.ylabel('Imaginary(c)')
    plt.show()

draw_mandel(200)