#lang racket

(define (read-strings-from-file file-path)
  (with-input-from-file file-path
    (λ ()
      (let loop ((line (read-line (current-input-port)))
                 (strings '()))
        (cond
          ((eof-object? line) (reverse strings)) ; Reverse to maintain original order
          (else
           (loop (read-line (current-input-port))
                 (cons line strings))))))))

(define input-file "DataInput.txt") ; Replace with your file path

(define strings-list
  (if (file-exists? input-file)
      (read-strings-from-file input-file)
      '("File not found.")))

(displayln strings-list) ; Print the list of strings

  (if (ormap (λ (x) (equal? x "SUM")) strings-list)
      (for-each xxxx strings-list)
    ;(displayln "Found")
    ;(displayln "Not found"))

;Function that traverses each element
;(define (process-string str))


  
  ;(displayln str))

;(for-each process-string strings-list); for-each element in strings-list, call process-string


