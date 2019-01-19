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
    Seq.unfold (fun (x, y) -> Some(x,(y, x+y))) (1I, 1I)
    

module TestFibonacci =
  let fibRec_Test = 
    // BTW prints only one of the first "1"s because we use a set for input parameters
    let fibs = Seq.map Fibonacci.fibRec (set [1..10])
    Seq.iter (fun x -> printfn "%A" x) fibs

  let fibSeq_Test = 
    Seq.iter (fun x -> printfn "%A" x) (Seq.take 10 Fibonacci.fibSeq)

  let iterateOverFibSeq =
    let rec forEver i =
      let digits = (Seq.item i fibSeq).ToString().Length
      if digits = 10 then
        printfn "%i" i
      else
        forEver (i+1)
    
    forEver 0