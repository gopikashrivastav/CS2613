#lang racket
;Sample code that creates a file "Output2.txt" in the
;same directory and then writes "hello world" out to it. YAY!!! works!
 (define out (open-output-file "Output2.txt"))
 (write "hello world" out)
 (close-output-port out)

(define in (open-input-file "Input.txt"))
;read-string reads n bytes in
(read-string 10 in)
(close-input-port in)