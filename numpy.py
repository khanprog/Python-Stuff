-----------------------------------------------
Numpy functions and its details
-----------------------------------------------

np.sum() -- for summing values
np.dot() -- scalar multiplication
np.sqrt() -- takes  square root
np.linalg() -- find mangnitude or distance
np.linalg.norm() -- for finding the angle 
datetime.now() -- gets the current time

-----------------------------------------------
* -- means element by element multiplication
. -- means matrix multiplication

Matrix = np.array([[1,2], [3,4]]) -- create a Matrix
Matrix = np.matrix([[1,2], [3,4]]) -- alternative of matrix not preferred
Matrix.T -- Takes a transpose of the matrix
Matrix[0,0] -- gets the first item of matrix

------------------------------------------------

z = np.zeros() -- creates a zeros matrix 
o = np.ones() -- creates a ones matrix
r = np.random.random(()) -- create a random matrix
G = np.random.randn() -- creates a guassian distribution random matrix
G.mean() -- finds the mean of the matrix
G.var() -- finds the variance of the matrix

---------------------------------------------------

np.linalg.inv() -- finds inverse of a matrix
np.linalg.det() -- finds determinant of the matrix
np.diag() -- finds the diagnol of the matrix
np.outer() -- finds the outer product of the matrix
np.inner() -- finds the innder product of the matrix as dot product do 
np.trace() -- finds the sum of the diagnols of the matrix
np.cov(matrix.T) -- find the covariance of the matrix, take transpose before finding covariance
np.linalg.eig() -- finds the eigen values
np.linalg.eigh() -- finds the eigen values for symmatric of hermitian matrix

-----------------------------------------------------

np.linalg.solve(matrix1,matrix2) -- find solution for a problem of matrix to find values

-----------------------------------------------------

-----------------------------------------------------
Pandas and its details
-----------------------------------------------------

map(datatype, value) -- it casts the value to that type 
X = pandas.read_csv("filenamce",header=None) -- it reads the cvs file ignoring the column names it returns the Dataframse datatype
X.info() -- shows the details of the data read
X.head() -- shows the specific data pass an argument an int 

M = X.as_matrix() -- it returns the matrix of the data in numpy array
X[0] -- it returns a whole column 
M[0] -- it returns a whole row
X.iloc[0] -- it returns a row 
X.ix[0] -- it returns a row 
X[[0,2]] -- multiple colums 
X[[0] < 5] -- select rows with a condition

X.columns = ["name", "name"] -- give names to the columns by passing a list or we just check with it
X.nameofcolumn -- it should not have spaces and should have to be a string 
X['Ones'] = 1 -- it adds a new column to the data 

X['dt'] = X.apply(lambda row: datetime.strptime(row['month'],'%Y-%m'),axis=1) -- it generates a new column with date and time 

m = X.merge(table1, table2, on="ids etc") -- it joins tow tables

-------------------------------------------------------

-------------------------------------------------------
Matplotlib funcs and details
-------------------------------------------------------

X = np.linspace(start,end,no_points) --- generates data points 

y = np.sin(x) -- generates sin wave

plt.plot(x,y) -- plot data
plt.xlable("X") -- give label to x-axis
plt.ylabel("y") -- give label to y-axis
plt.title("Chart") -- give title to the figure
plt.show() -- finally show the figure


plt.scatter(x,y) -- create a scatter Chart

plt.hist(x, bins=10) -- creates a histogram



im = M[0, 1:]
im = np.reshape(28,28)
plt.imshow(im) -- show the image in as heatmap
plt.imshow(im, cmap="gray") -- black background
plt.imshow(255-im, cmap="gray") -- white background

--------------------------------------------------------

--------------------------------------------------------
Scipy funcs and details
--------------------------------------------------------

norm.pdf()
norm.logpdf()
norm.cdf()
norm.logcdf()




--------------------------------------------------------

intitle:index.of? mkv Avengers 
intitle:index.of? mkv 
Movie Name -inurl:(htm|html|php|pls|txt) intitle:index.of “last modified” (mp4|wma|aac|avi)