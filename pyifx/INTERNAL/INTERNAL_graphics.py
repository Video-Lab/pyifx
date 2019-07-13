def _create_kernel(size=(3,3), radius=1.5, type_kernel=None):
	matrix = None

	if type_kernel == "gaussian":
	    m,n = [(ss-1.)/2. for ss in size]
	    y,x = np.ogrid[-m:m+1,-n:n+1]
	    matrix = np.exp( -(x*x + y*y) / (2.*radius*radius) )
	    matrix[ matrix < np.finfo(matrix.dtype).eps*matrix.max() ] = 0
	    sumh = matrix.sum()
	    if sumh != 0:
	        matrix /= sumh
	    matrix = np.asmatrix(matrix)

	else:
		raise Exception("Something went wrong. Please try again.")


def _is_matrix_symmetrical(kernel):
	pass

def _convolute(img, filter):
	pass

def _blur(img_paths, kernel):
	pass