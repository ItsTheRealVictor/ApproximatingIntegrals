# ApproximatingIntegrals

This is a small project used to approximate the value of definite integrals. It uses the SymPy package to calculate the exact value of the integral and compare it with the approximations. 

It uses the trapezoidal and Simpson's methods, where a number of boxes are draw underneath the curve of a function. The area of the boxes is calculated and collectively summed, representing an approximate value for the area underneath the curve. The more boxes are added, the more accurate the approximation becomes when compared with the exact value.

This was originally an extra credit project presented to my calculus 2 class after everyone bombed a test. The suggestion was to use microsoft excel to make the calculations, I thought it would make a good candidate for a python program. It's easy to change the number of trapezoids in the script, with excel the values need to manually added. 
