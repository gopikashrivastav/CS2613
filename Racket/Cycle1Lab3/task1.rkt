#lang racket

(define (larger_rectangle l1 w1 l2 w2)
(define a1 (* l1 w1))
(define a2 (* l2 w2))
(if (> a1 a2)
    -1
    1))
(larger_rectangle 1 1 2 2)
(larger_rectangle 3 5 2 4)
(larger_rectangle 2 21 6 7)


(define (fibonacci n)
(define a 0)
(define b 1)
(cond
  [(<= n 1)  n ]
  [else ( + (fibonacci (- n 1)) (fibonacci (- n 2)))]))



(fibonacci 13)
  



  

  