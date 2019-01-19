#load "Fibonacci.fs"
open ProjectEulerLib.Fibonacci

module TestFibonacci =
  let fibRecTest =
    // BTW prints only one of the first "1"s because we use a set for input parameters
    let fibs = Seq.map fibRec (set [1..10])
    printfn "Now trying the tail recursive version of Fibonacci"
    Seq.iter (fun x -> printf "%A " x) fibs
    printfn " "

  let fibSeqTest =
    printfn "Now trying the seq version of Fibonacci"
    Seq.iter (fun x -> printf "%A " x) (Seq.take 10 fibSeq)
    printfn " "

  let iterateOverFibSeq =
    let rec forEver i =
      let digits = (Seq.item i fibSeq).ToString().Length

      if digits = 10 then
        printfn "No.%i is the first Fibonacci number with %i digits" i digits
      else
        forEver (i+1)

    forEver 0
