#lang slideshow

(define (square n)
  (filled-rectangle n n))

(define (original-rainbow p)
  (map (lambda (color)
         (colorize p color))
       (list "red" "orange" "yellow" "green" "blue" "purple")))


(define (my-rainbow p)
  (define (color-mapper shape colorlist)
    (cond
      [(empty? colorlist) empty]
      [else (cons (colorize shape (first colorlist))
                  (color-mapper shape (rest colorlist)))]))
  (color-mapper p (list "red" "orange" "yellow" "green" "blue" "purple")))

(provide square my-rainbow)

(my-rainbow (square 5))
