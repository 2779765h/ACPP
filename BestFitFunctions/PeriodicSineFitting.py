# Finding a function to fit over one (x,y) point in the dataset

# Data
I_25 = Data[25, 25, :] # Intensity over all the angles at (x=25, y=25)
AngleValues = np.linspace(0, 2*np.pi, 360) # Generate array of angle values

def sin_fit(x, c, A0, A1, A2, A3):
    '''
    Defining a fourier series, periodic function for fitting
    x is the angle/ x-axis data
    c is the offset term
    A0, A1, A2, A3 are the associated amplitudes for each sin term, respectivily 
    '''
    return c + A0*np.sin(x/2) + A1*np.sin(2*x/2) + A2*np.sin(3*x/2) + A3*np.sin(4*x/2)

# y = 30 + 65*np.sin(x/2) + 45*np.sin(2*x/2) + 60*np.sin(3*x/2) + 10*np.sin(4*x/2) - good initial guess

# Initial Guesses
#c = np.mean(I_25) # offset
#A = np.max(I_25)-np.min(I_25)/2 # amplitude

#p0 = [c, np.max(I_25), 45, 65, 50]
p0 = [c, 1, 0, 0, 0]

p, V = optimize.curve_fit(sin_fit, AngleValues, I_25, p0)
yfit = sin_fit(AngleValues, *p)

# Plot
plt.title('Intensity vs. Angle at x=25, y=25')
plt.plot(AngleValues, I_25, label="Data")
plt.plot(AngleValues, yfit, label="Best Fit")
plt.xlabel('Angle (rad)')
plt.ylabel('Scattering Intensity (Arbitrary Units)')
plt.suptitle('Figure 12', x = 0.5, y = 0)
plt.legend()
plt.show()
