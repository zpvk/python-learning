/*
 * @Author: Rohan K 
 * @Date: 2020-10-23 22:22:34 
 * @Last Modified by: mikey.zhaopeng
 * @Last Modified time: 2020-10-23 23:09:27
 */

% The ; denotes we are going back to a new row.
A = [1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 12]

% Initialize a vector 
v = [1;2;3]

% Get the dimension of the matrix A where m = rows and n = columns
[m,n] = size(A)

% You could also store it this way
dim_A = size(A)

% Get the dimension of the vector v 
dim_v = size(v)s

% Get the dimension of the vector v 
dim_v = size(v)

% Initialize matrix A and B 
A = [1, 2, 4; 5, 3, 2]
B = [1, 3, 4; 1, 1, 1]

% Initialize constant s 
s = 2

% See how element-wise addition works
add_AB = A + B 

% See how element-wise subtraction works
sub_AB = A - B

% See how scalar multiplication works
mult_As = A * s

% Divide A by s
div_As = A / s

% What happens if we have a Matrix + scalar?
add_As = A + s

% Initialize matrix A 
A = [1, 2, 3; 4, 5, 6;7, 8, 9] 

