#lang racket
(define (palindrome st)
  (define len (string-length st))
  
  ;Base Case
 (cond
    [(= len 0) (display "#t")]
    [(= len 1) (display "#t")])
  
  ;(if (= len 0)
     ; (display ("#t"))
     ; -1)
  ;(if (= len 0)
      ;(display ("#t"))
    ;  -1)
  
  ;Gen Case
  (if (char=? (string-ref st 0) (string-ref st (- len 1)))
  (palindrome (substring st 1 (- len 1)))
  (display "#f")))

(palindrome "")
  