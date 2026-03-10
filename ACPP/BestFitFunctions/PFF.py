import numpy as np

def FitandPlot(x, y, degree, Rx, Ry, Px, Py, Ex, Ey, Figure):
    '''
    Define a function for making best fit and plots.
    Calculates the best fit, then the residuals, and then computes the goodness of fit.
    Transfers all the calculated data towards plotting 
    and showing the data with fit and a seperate residuals plot. 
    
    Data types:
    x: np.array
    y: np.array
    degree: int
    Rx: float
    Ry: float
    Figure: str     

    This function takes input parameters:
    x = x_data
    y = y_data
    degree - represents the degree of the polynomial
    Rx - x coordinate of the position for goodness of fit
    Ry - y coordinate of the position for goodness of fit
    Figure - Figure number
    '''

    # Perform fitting 
    p, V = np.polyfit(x, y, degree, cov=True) 
    x_fit = np.linspace(min(x), max(x), 300)
    y_fit = np.polyval(p, x_fit) # predicted best fit y values 
    bestfit_parameters = p
    bestfit_errors = np.sqrt(np.diag(V))

    # Calculate the Residuals
    y_datafit = np.polyval(p, x) # predicted y values from x data 
    ResidualData = y - y_datafit

    # Calculate the value of R^2
    y_mean = np.mean(y)
    SS_res = np.sum((ResidualData)**2) # sum of squares of residuals
    SS_tot = np.sum((y - y_mean)**2)
    R_squared = (1 - (SS_res / SS_tot)) 

    # Plots
    plt.figure(figsize=[10,6])

    # Best fit plot
    plt.subplot(2,2,1)
    plt.scatter(x, y, label='Data')
    plt.plot(x_fit, y_fit, "-", label="Best fit", color='green')
    plt.text(Rx, Ry, '$R^2$ = {0:.4f}'.format(R_squared))
    plt.xlabel('Current (A)')
    plt.ylabel('Magnetic Field (mT)')
    plt.title('Current vs. Magnetic Field')
 
    # Functions for looping over fit and fit error parameters
    Parameters = "Fit parameters:\n"
    for i, a in enumerate(bestfit_parameters):
        b = degree - i
        Parameters += 'a{b} = {j:.2f}\n'.format(b=b, j=a)
        
    Errors = "Fit uncertainties:\n"
    for i, da in enumerate(bestfit_errors):
        c = degree - i
        Errors += 'Δa{c} = {j:.2f}\n'.format(c=c, j=da)

    plt.text(Px, Py, Parameters)
    plt.text(Ex, Ey, Errors)
    plt.legend()

    # Residuals plot
    plt.subplot(2,2,2)
    plt.scatter(x, ResidualData, color = 'darkorange')
    plt.xlabel('Current (A)')
    plt.ylabel('Residual')
    plt.title('Residual Plot')

    plt.suptitle(Figure, x = 0.5, y = 0.4)
    plt.tight_layout()
    plt.show()  
