* First of all, we need to read @lee's explanation for this solution if not already done so. It's brilliant.
* However, there are flaws with that approach. What if we have a million or a billion stack elements (maxSize)? In that case, this solution will not work
  because we cannot allocate an in-memory structure of that size. So, we need to think of an alternative as well
* The alternative is to do this:
  * Instead of an additional array for the increment operations, we keep another stack.
  * Each operation, whether push or increment, has to be incorporated with an additional "time" information i.e. when was that operation performed.
  * This can be a simple incrementing time value. 
  * So the stack we build will have (data, t) tuples. Similarly, the increment stack will have (inc, t) information. Both these operations will be O(1)
  * When popping, we check if the topmost element of the stack applies to this element or not (t_inc >= t_data). If it does, we keep incorporating increments by
    going down the inc stack one by one, all the way to the end or until we find (t_inc < t_data). 
  * Pop will be expensive of the order of O(m) where `m` is the number of increment operations done till now. It does not depend on the number of elements we have in the stack.
