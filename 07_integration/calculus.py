"""
Numerical calculus module for use in PHY494
-------------------------------------------
"""


def calculus():

	def simpson_np(f, a, b, N):
		'''Uses simpson's rule of integration to approximate the integral.'''
    if N % 2 == 0:
        raise ValueError("N must be odd")
        
    h = np.abs(a-b)/(N - 1)
    function = f(np.linspace(a,b,N))
    weights = 4*np.ones(N)
    weights[[0,-1]] = 1
    weights[2:-2:2] = 2
    return np.sum(weights*function)*h/3

    def integrate_simple_np(f, a, b, N):
    '''Integrate function `f` from `a` to `b` with `N` points. Taken from jupyter.'''
    h = (b - a)/(N-1)
    xi = np.linspace(a, b, N)    # all interval points
    fi = f(xi)                   # all function evaluations
    fi[[0, -1]] /= 2    # include endpoints with weight 1/2
    return h * fi.sum()

    def D_forward(y, t, h):
    """Forward difference. Taken from jupyter."""
    return (y(t + h) - y(t))/h

	def D_cd(y, t, h):
    """Central difference. Taken from jupyter."""
    return (y(t + h/2) - y(t - h/2))/h

	def D_ed(y, t, h):
    """Extended difference. Taken from jupyter."""
    return (8*(y(t + h/4) - y(t - h/4)) - (y(t + h/2) - y(t - h/2)))/(3*h)