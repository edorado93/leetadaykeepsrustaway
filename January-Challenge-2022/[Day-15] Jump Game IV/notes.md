# Amazing question!
Lot of points to think about in this case truly:

* Dynamic Programming won't work. The state space becomes too big and then it doesn't remain feasible anymore.
* Next up, the solution I came up with was based on a mixture of Topological Sorting and Dynamic Programming. 
  * Start from the last node in the queue. If you're there, then we have 0 steps to get to our destination. Let's call this index `x`
  * Next, we look at all the places that are reachible from this index. All these places (same value as `x`, the index `x - 1`, and index `x + 1` have to take one _additional_ step than what it takes to reach the destination from `x`)
  * And continue. We push all these values into the queue and continue.
  * Interestingly, we don't store indices in the `visited` dictionary. Instead, we store the values there. Once a value has been popped from the queue, all related indices will be pushed to the queue. So, we can instead mark the values as visited rather than the indices.
