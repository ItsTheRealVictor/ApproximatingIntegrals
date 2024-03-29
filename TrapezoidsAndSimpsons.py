import math
import sympy as sp

x = sp.symbols('x')

# defining the function and the limits of integration
function = ((-x**2) + 49) # if this program works correctly, you will be able to change this function and its bounds to whatever you want. 
upperBound = 5
lowerBound = 1
n = 10 + 1 #this is the number of trapezoids. We take the area of each one, add them up, and divide by .5(delta_x). The more trapezoids you use, the more accurate your approximation becomes

delta_x = (upperBound - lowerBound) / ((int(n) - 1))

# beginning at 1, this sequence adds the value of delta_x to the previous value
def sequence(n):
    if n <= 1:
        return n
    else:
        return(delta_x + sequence(n - 1))
nterms = n
deltaTerms = []

# this adds numbers from the sequence to the deltaTerms list. Later, we will plug those values into the function.
if nterms <= 1:
    print("no")
else:
    for i in range(nterms + 1):
        deltaTerms.append(sequence(i))
deltaTerms.pop(0)


# this determines the coefficient values of the trapezoidal and simpson's approximations. We will multiply these values by the function values, later to be summed and multplied by .5(delta_x). This achieves our final approximations.

#The trapezoidal approximation multiplies the first by 1, and all subsequent values by 2
trapCoefficients = [2] * (int(n))
trapCoefficients.insert(0, 1)
trapCoefficients.pop(-1)

#The Simpson's approximation multiplies the first by 1, and all subsequent values by alternating 4's and 2's. 
simpsonsCoefficients = []
for i, j in enumerate(trapCoefficients):
  if i == 0:
    simpsonsCoefficients.append(1)
  elif i % 2 == 0:
    simpsonsCoefficients.append(2)
  else:
    simpsonsCoefficients.append(4)


#This plugs the delta_x sequence values into our actual function.
actualFunctionVals = []
for i in (deltaTerms):
  actualFunctionVal = function.subs(x, i)
  actualFunctionVals.append(actualFunctionVal)

#this joins the delta values with the function values into a separate dictionary
termDict = (dict(zip(deltaTerms, actualFunctionVals)))
trapValuesToBeSummed = [a * b for a, b in zip(trapCoefficients, actualFunctionVals)]
simpValuesToBeSummed = [a * b for a, b in zip(simpsonsCoefficients, actualFunctionVals)]

#this is the formula for the approximations. We will compare these values to the exact value of the integral
trapApproximation = .5 * delta_x * sum(trapValuesToBeSummed)
simpApproximation = (1/3) * delta_x * sum(simpValuesToBeSummed)
actual = sp.integrate(function, (x, lowerBound, upperBound)) #using the integrate function from SymPy

#we will now calculate the percent difference between the approximation and the actual value.

def percentDiff(x1, x2):
  average = ((x1 + x2) / 2)
  percDif = ((abs(x1 - x2)) / average) * 100
  return(percDif)

# a review of everything we have for the user to verify
print("This is an approximation of the definite integral of " + str(function ) + " from " + str(lowerBound) + " to " + str(upperBound) + ".")
print("")
print("We will use the area of " + str(n - 1) + " trapezoids to achieve this approximation.")
print("")
print("Trapezoidal approximate: " + str(round(float(trapApproximation), 4)))
print("Simpson's approximate: " + str(round(float(simpApproximation), 4)))
print("Exact value: " + str(round(float(actual), 4)))
print("Trapezoidal percent difference: " + str(round(float(percentDiff(trapApproximation, actual)), 2)) + " percent.")
print("Simpson's percent difference: " + str(round(float(percentDiff(simpApproximation, actual)), 2)) + " percent.")

"""
Future features of this program
1) Add graphs of the function with MatPlotLib. The user can visualize what the function looks like and how many trapezoids are being used to calculate the approximation
2) Add the data to an excel spreadsheet using openPyXL.
3) Add GUI functionality. The user will be able to enter a function of x, the lower/upper bounds, and the number of trapezoids. It will calculate and display the same data you see in the output of this program. 
"""
