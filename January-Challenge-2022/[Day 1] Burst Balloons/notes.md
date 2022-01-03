# Notes

* Very similar to the Matrix Multiplication dp but one subtle difference that breaks the original thought.
  * Think why the two subproblems are ***not independant*** of each other unlike in matrix multiplication.
* Some ingenious backward thinking helps here to make them independant.
* Think about why, for a range like [left, right], the balloons left-1, and right+1 will be intact until the range is exhausted. That's very important.  
