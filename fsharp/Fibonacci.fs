namespace ProjectEulerLib

module Fibonacci =
  
  // A tail recursive version of Fibonacci
  let FibRec n = 
    let rec FibTail (x:bigint) (y:bigint) = function
      | 0 -> y
      | n -> FibTail y (bigint.Add(x,y)) (n-1)
      
    FibTail 0I 1I n

    // Testing code follows due, for now it's easier to copy that stuff into fsi