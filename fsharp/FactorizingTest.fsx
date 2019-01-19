#load "Factorizing.fs"
open ProjectEulerLib.Factorizing

module FactorizingTest =
  let biggestFactorOfTest =
    printfn "Biggest prime fator of %O is %O" 600851475143I (biggestFactorOf 600851475143I)