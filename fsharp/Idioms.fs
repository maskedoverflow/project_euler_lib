namespace Idioms
// Short passages of code that quite often

module Benchmarking =
  /// Measures the executions time of a function f (more precisely, a lambda expression f) and returns f's value
  /// That is, call this like durationOf (fun whatever -> whatever)
  let durationOf f =
    let timer = System.Diagnostics.Stopwatch()
    let result = f()
    Printf.printfn "Function took %i ms" timer.ElapsedMilliseconds
    result