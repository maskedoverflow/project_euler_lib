namespace ProjectEulerLib

module Fibonacci =

  // A tail recursive version of Fibonacci
  let fibRec n = 
    let rec fibTail (x:bigint) (y:bigint) = function
      | 0 -> y
      | 1 -> y
      | n -> fibTail y (bigint.Add(x,y)) (n-1)
      
    fibTail 0I 1I n

  let fibSeq = 
    // Seq.unfold f x expects f to return a "('T * 'State) option", i.e.
    // an tuple option where the first value is the result of f
    // and the second value is whatever to be passed next to f, hence the 'State
    Seq.unfold (fun (x, y) -> Some(x,(y, x+y))) (1I, 1I)