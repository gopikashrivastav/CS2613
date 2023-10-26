#lang racket

(define my-list '(1 2 3 4 5))
(define result (apply + my-list))

(displayln result) ; This will display the sum of the elements in the list


(define original-list '(1 2 3 avg 4 5 6))

(define new-list
  (if (member 'avg original-list)
      (take original-list (add1 (length (take-right original-list 'avg))))
      original-list))

(displayln new-list)
