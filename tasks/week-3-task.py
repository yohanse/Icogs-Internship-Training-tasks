from hyperon import MeTTa
metta = MeTTa()

metta_code_task_1 = '''
;1. extract the last element -- e.g., (:: 1 (:: 2 (:: 3 (:: 4 ())))) the last element would be 4

; The base case: If the input list is empty, 
; the pattern is null (no last element).
(= (last-element ()) 
   (The pattern is null)
)

; Recursive case: Extract the first element ($first) and the rest of the pattern ($rest).
(= (last-element (:: $first $rest))
   ; We check if the rest of the list is empty.
   (unify ($rest)
      (())          ; If $rest is an empty list, then $first is the last element.
      ($first)      ; Return $first when $rest is empty.
      (last-element $rest) ; Otherwise, continue recursively with $rest.
   )
)

!(last-element ()) 
; Output - [(The pattern is null)]

!(last-element (:: 1 (:: 2 (:: 3 (:: 4 ()))))) 
; Output - [(4)]
'''

metta_code_task_2 = '''
; 2. append one more element to the list at the begining -- e. g., adding 0 to the list (:: 1 (:: 2 (:: 3 (:: 4 ())))) --> (:: 0(:: 1 (:: 2 (:: 3 (:: 4 ())))))

; This function appends $element to the left of $pattern.
; It first checks whether $element is a structured list or a single element.
(= (append-left $pattern $element) (
    unify ($element)
      ((:: $first $rest))
      (append-left-pattern $pattern $element)
      (append-left-pattern $pattern (:: $element ()))
    )
)

(= (append-left-pattern $pattern ()) 
    $pattern
)

(= (append-left-pattern $pattern (:: $first $rest)) (
    :: $first (append-left-pattern $pattern $rest)
    )
)


!(append-left (:: 0 ()) 1)
; Output --> [(:: 1 (:: 0 ()))]

!(append-left (:: 0 ()) (:: 2 (:: 1 ())))
; Output --> [(:: 2 (:: 1 (:: 0 ())))]

!(append-left (append-left (:: 1 (:: 2 (:: 3 (:: 4 ())))) (:: 5 (:: 6 ()))) 7)
; Output --> [(:: 7 (:: 5 (:: 6 (:: 1 (:: 2 (:: 3 (:: 4 ())))))))]

'''


metta_code_task_3 = '''
; 3. append one more element to the list at the end -- e. g., adding 5 to the list (:: 1 (:: 2 (:: 3 (:: 4 ())))) --> (:: 1 (:: 2 (:: 3 (:: 4 (:: 5 ())))))

; This function appends $element to the right of $pattern.
; It first checks whether $element is a structured list or a single element.
(= (append-right $pattern $element) (
    unify ($element)
      ((:: $first $rest))
      (append-right-pattern $pattern $element)
      (append-right-pattern $pattern (:: $element ()))
    )
)

(= (append-right-pattern () $element) 
    $element
)

(= (append-right-pattern (:: $first $rest) $element) (
    :: $first (append-right-pattern $rest $element)
    )
)


!(append-right (:: 0 ()) 1)
; Output --> [(:: 0 (:: 1 ()))]

!(append-right (:: 0 ()) (:: 2 (:: 1 ())))
; Output --> [(:: 0 (:: 2 (:: 1 ())))]

!(append-right (append-right (:: 1 (:: 2 (:: 3 (:: 4 ())))) (:: 5 (:: 6 ()))) 7)
; Output --> [(:: 1 (:: 2 (:: 3 (:: 4 (:: 5 (:: 6 (:: 7 ())))))))]
'''


metta_code_task_5 = '''
; 5. a function to extract all the elements of the above list type into an expresion -- (:: 1 (:: 2 (:: 3 (:: 4 ())))) --> (1 2 3 4)

(= (extract-elements ()) (
    The pattern is empty
    )
)

(= (extract-elements (:: $first $rest)) (
    unify ($rest)
      (())
      (cons-atom $first ())
      (
      let* (($head $first)
          ($tail (extract-elements $rest))
      )
     (cons-atom $head $tail)
      )
    )
)


!(extract-elements (:: 1 (:: 2 (:: 3 (:: 4 ())))))
; Output --> [(1 2 3 4)]

!(extract-elements ())
; Output --> [(The pattern is empty)]

'''


metta_code_task_6= '''
;6.  finding length of an expression of the form (A B C) -- 3

;To caculate the length
(= (length $atom) (
    unify ($atom)
        (())       
        0      
        (+ 1 (length (cdr-atom $atom))) 
    )
)

!(length (1 2 4 4 1))
;Output --> [5]

!(length ())
;Output --> [0]
'''

metta_code_task_7 = '''
; 6 finding an expression containing sum of two numeric expressions (including length checking conditions -- a plus)

;To caculate the length
(= (length $atom) (
    unify ($atom)
        (())       
        0   
        (+ 1 (length (cdr-atom $atom))) 
    )
)

; Function to sum two expressions (lists of numbers)
(= (sum-expression $atom1 $atom2) (
    case((length $atom1) (length $atom2)) (
        (($a $a) (sum-expression-helper $atom1 $atom2))
        (($a $b) not-equal)
        )
    )
)

; Helper function to sum two lists element-wise
(= (sum-expression-helper $atom1 $atom2) (
    unify ($atom1)
        (())       
        ()   
        (
        let* (
            ($head1 (car-atom $atom1))
            ($head2 (car-atom $atom2))
            ($total (+ $head1 $head2))
            ($tail (sum-expression-helper(cdr-atom $atom1) (cdr-atom $atom2)))
        )
        (cons-atom $total $tail)
        ) 
    )
)

!(sum-expression (1 2 3 4) (5 6 7 8))
;Output --> [(33 4 4)]

!(sum-expression (1 2) (3 4 5))
;Output --> [(33 4 4)]

'''


metta_code_task_8 = '''
; 8. select by index function , e.g., in (1 3 4) (funct (1 3 4) 0) -- 1


;To caculate the length
(= (length $atom) (
    unify ($atom)
        (())       
        0   
        (+ 1 (length (cdr-atom $atom))) 
    )
)

(= (select-by-index $atom $index) (
    if ( or (>= $index (length $atom)) ( < $index 0)) (not-exists) (select-by-index-helper $atom $index)
    )
)

(=(select-by-index-helper $atom $index) (
    if(< $index 1)(car-atom $atom)(select-by-index-helper (cdr-atom $atom) (- $index 1))
    )
)

!(select-by-index (1 2 3 4) 2)
;Output --> [3]

!(select-by-index (1 2 3 4) 4)
;Output -->  [(not-exists)]
'''

metta_code_task_9 = '''
; 9. slicing an expression by index
; Assumption the end index is inclusive

;To caculate the length
(= (length $atom) (
    unify ($atom)
        (())       
        0   
        (+ 1 (length (cdr-atom $atom))) 
    )
)

; To check if the starting and ending index is valid
(= (slice-by-index $atom $start $end) (
    if ( or ( or ( or  (>= $start (length $atom)) (< $start 0)) (>= $end (length $atom))) ( < $end $start)) (not-exists) (slice-by-index-helper $atom $start $end 0)
    )
)

( = (slice-by-index-helper $atom $start $end $index) (
    if ( < $index $start) (slice-by-index-helper (cdr-atom $atom) $start $end (+ $index 1)) (
        if ( <= $index $end) (
            let* (
                ($head (car-atom $atom))
                ($tail (slice-by-index-helper (cdr-atom $atom) $start $end (+ $index 1)))
            )
            (cons-atom $head $tail)
            )
        ()
        )
    )
)

!(slice-by-index (1 2 3 4 5 6 7 8 9) 5 8)
; Output --> [(6 7 8 9)]

!(slice-by-index (1 2 3 4 5 6 7 8 9) 5 9)
; Output --> [(not-exists)]

'''

metta_code_task_10 = '''
; 10. Reconstruct an expression using car-atom, cdr-atom and cons-atom 
; make use of the println! function to show reconstruction variable outputs

(= (reconstruct $atom) (
    unify ($atom)
        (())
        ()
        (
        let* (
            ($head (car-atom $atom))
            ($tail (reconstruct (cdr-atom $atom)))
            ($reconstructed (cons-atom $head $tail))
        )
        (trace! $reconstructed $reconstructed)
        
      )
    )
)

!(reconstruct (1 2 3 4 5))
;Output --> 
;(5)
;(4 5)
;(3 4 5)
;(2 3 4 5)
;(1 2 3 4 5)
;[[(1 2 3 4 5)]]
'''

metta_code_task_bonus = '''
; bonus -- insering a node to this list -- insert node D to (:: A (:: B (:: C ()))) -- >(:: A (:: B (:: D (:: C ()))))

(= (length ()) 0)

(= (length (:: $x $xs))
   (+ 1 (length $xs)))

(= (insert-node $pattern $index $node) (
    if ( or (> $index (length $pattern)) ( < $index 0)) (can-not-be-inserted) (insert-node-helper $pattern $index $node)
    )
)

; Helper function to insert a node at a given index

; If the index is at the last, return new pattern.
(= (insert-node-helper () $index $node) (:: $node ()))

(=(insert-node-helper (:: $first $rest) $index $node) (
    if(< $index 1) 
    (:: $node (:: $first $rest))
        
    (
        let* (
                ($head $first)
                ($tail (insert-node-helper $rest (- $index 1) $node))
            )
            (:: $head $tail)
        )
    )
)

!(insert-node (:: A (:: B (:: C ()))) 3 D)
;Output --> [(:: A (:: B (:: D (:: C ()))))]

'''
result = metta.run(metta_code_task_bonus)
print(result)