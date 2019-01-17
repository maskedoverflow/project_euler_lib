namespace ProjectEulerLib

module Fibonacci =

  // A tail recursive version of Fibonacci
  let fibRec n = 
    let rec fibTail (x:bigint) (y:bigint) = function
      | 0 -> y
      | n -> fibTail y (bigint.Add(x,y)) (n-1)
      
    fibTail 0I 1I n


module TestFibonacci =
  let fibRec_Test = 
    let fibs = Set.map Fibonacci.fibRec (set [1..10])
    Seq.iter (fun x -> printfn "%A" x) fibs
    