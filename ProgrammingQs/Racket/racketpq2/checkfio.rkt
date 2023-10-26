#lang racket

(define (read-strings-from-file file-path)
  (with-input-from-file file-path
    (λ ()
      (let loop ((line (read-line (current-input-port))))
        (cond
          ((eof-object? line) '())
          (else
           (displayln line)
           (loop (read-line (current-input-port)))))))))

(define input-file "Input.txt") ; Replace with your file path

(if (file-exists? input-file)
    (read-strings-from-file input-file)
    (display "File not found."))
