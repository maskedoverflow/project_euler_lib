namespace ProjectEulerLib
open System

module Factorizing =

  // This inefficiently looks for the biggest prime in any given number by tearing said number down
  let biggestFactorOf number =
    let rec sluggish factor = function
      | x when x < factor -> factor
      | x when x % factor <> 0I -> sluggish (factor + 1I) x
      | x -> sluggish factor (x / factor)
    sluggish 2I number
