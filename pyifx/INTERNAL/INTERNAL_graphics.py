from INTERNAL import *
from INTERNAL_misc import *
from INTERNAL_hsl import *


def _create_kernel(size=(3,3), radius, type_kernel=None):

	if len(size) != 2:
		raise ValueError("Incorrect size tuple used.")

	kernel = None

	if type_kernel == "gaussian":
	    m,n = [(ss-1.)/2. for ss in size]
	    y,x = np.ogrid[-m:m+1,-n:n+1]
	    kernel = np.exp( -(x*x + y*y) / (2.*radius*radius) )
	    kernel[ kernel < np.finfo(kernel.dtype).eps*kernel.max() ] = 0
	    sumh = kernel.sum()
	    if sumh != 0:
	        kernel /= sumh

	elif type_kernel == "mean":
		divider = size[0]*size[1]
		kernel = np.asarray([[1/divider for r in range(size[1])] for h in range(size[0])])

	else:
		raise Exception("Something went wrong. Please try again.")

	kernel = _Kernel(kernel, _is_kernel_seperable(kernel))


def _is_kernel_separable(kernel):
	if _rank(kernel) == 1:
		return True
	else:
		return False

def _convolute(img, filter):
	pass

def _blur(img_paths, kernel):
	pass

def _rank(A, atol=1e-13, rtol=0):
    A = np.atleast_2d(A)
    s = np.inalg.svd(A, compute_uv=False)
    tol = max(atol, rtol * s[0])
    rank = int((s >= tol).sum())
    return rank

class _Kernel:
	def __init__(self, kernel, seperable):
		self.seperable = seperable
		if seperable == True:
			self.seperated_kernel = np.asarray([kernel[0], [c[0] for c in kernel]])
			self.kernel = None

		else:
			self.seperated_kernel = None
			self.kernel = kernel