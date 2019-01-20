namespace ProjectEulerLib

module Sets =
  let rec powerset s =
    seq {
      match s with
        | [] -> yield []
        | head::tail -> for x in powerset tail do yield! [x; head::x]
     }