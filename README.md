"# Calculator-api" 

## Usage

Post at least two numbers and an operand,
it can be posted in seperate posts, or in one post.
If there is an incorrect number of arguments, and request GET is made,it will clear the input, and will state which argument was invalid.
Accepted operands:  
'+ - / *'

## Examples

-->POST / set 6  
<--OK  
-->POST / set 2  
<--OK  
-->POST / set +  
<--OK  
-->GET / get  
<--8.0  

-->POST / set 6 + 12  
<--OK  
-->GET / get  
<--18.0  

-->POST / set 6 + 12 88  
<--OK  
-->GET / get  
<-- Incorrect amount of NUMBER arguments, reenter your values from the start.  

-->POST / set 6 12  
<--OK  
-->GET / get  
<-- Incorrect amount of OPERAND arguments, reenter your values from the start.  
