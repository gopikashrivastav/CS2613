#lang racket
"hello"
1
2.3

#t

#f
'(1,2,3, "hello", #t)

(define a 1)
a

(- 2 a)

(define (bake flavor)
  (printf "preheating oven...\n")
  (string-append flavor " pie"))






;(display(+(char->integer #\6)))

(display(remainder 13583 10))

;(display(quotient 135 10))

(define(mystery x)
  (cond [(< x 20) x]
  [else (+ (remainder x 10) (mystery(quotient x 10)))]))
(display(mystery 2334683))
  



