## Think about adding new functionalities!

The solution that I added here for now is not an optimal one in terms of extensibility. Think about how `rmdir` would be implemented? We'll have to iterate over all the dictionary keys and then delete/upate all of them containing the directory we are deleting.
I did optimize for more `ls` and `addContentToFile` reads but then, this design is not that extensible and also, potentially takes up a lot of redundant space in terms of the dictionary keys.

> Write an article on this discussing various designs and also, some other functionalities and how we can write a tester for this!
