#lang racket
 ;requirements for lexer, parser, etc.
(require parser-tools/lex)
(require  parser-tools/yacc
         (prefix-in : parser-tools/lex-sre)
         (prefix-in re: parser-tools/lex-sre)
         (only-in pict cc-superimpose disk filled-rectangle text)
         pict/tree-layout
         syntax/readerr)
(require dyoo-while-loop)
(require loop)

;start implementation of lexer
(define-lex-abbrevs
  (string-content (union (char-complement (char-set "\"\n"))))
  (string-literal (union (concatenation #\" (repetition 0 +inf.0 string-content) #\")
                         "\"\\n\"" "\"\\\\\""))
  (var        (re:+ alphabetic))
  (string     (:: #\" (:* (complement "*/")) #\"))
  (digit      (:or (:+ (char-range #\0 #\9)) (:: (:+ (char-range #\0 #\9)) #\. (:+ (char-range #\0 #\9))) (::  #\0 #\. (:+ (char-range #\0 #\9))) ))
)



(define simple-math-lexer
           (lexer
            [string-literal (token-STRING lexeme)]
            [(:+ digit)  (token-NUM (string->number lexeme))]
            ("+" (token-PLUS))
            ("-" (token-MINUS))
            ("*" (token-MULT))
            ("/" (token-DIV))
            ("(" (token-LPARAN))
            (")" (token-RPARAN))
            ("[" (token-LBARAK))
            ("]" (token-RBARAK))
            ("," (token-comma))
            (";" (token-SEMICOLON))
            ("=" (token-EQUAL))
            ("==" (token-EQUALEQUAL))
            ("!=" (token-NOTEQUAL))
            ("<" (token-LESS))
            (">" (token-GREATER))
            ("while" (token-WHILE))
            ("do" (token-DO))
            ("end" (token-END))
            ("if" (token-IF))
            ("then" (token-THEN))
            ("else" (token-ELSE))
            ("return" (token-RETURN))
            ("true" (token-TRUE))
            ("false" (token-FALSE))
            ("null" (token-NULL))
            [var    (token-ID (string->symbol lexeme))]
            [whitespace (simple-math-lexer input-port)]
            [(eof) (token-EOF)]))


   

(define-tokens a (NUM ID STRING))
(define-empty-tokens b (EOF WHILE DO END IF THEN ELSE RETURN TRUE FALSE SEMICOLON comma NOTEQUAL EQUAL EQUALEQUAL GREATER LESS MINUS PLUS MULT DIV LPARAN RPARAN LBARAK RBARAK NULL))



;start implementation of parser
(define-struct run-cmd (unitcom command) #:transparent)
(define-struct if-com (exp then_com else_com) #:transparent)
(define-struct while-com (exp com) #:transparent)
(define-struct assign (var exp) #:transparent)
(define-struct return (exp) #:transparent)
(define-struct arith-exp (op bexp1 bexp2) #:transparent)
(define-struct num-exp (n) #:transparent)
(define-struct var-exp (var) #:transparent)
(define-struct bool-exp (bool) #:transparent)
(define-struct null-exp () #:transparent)
(define-struct str-exp (str) #:transparent)
(define-struct unequal-exp (op aexp1 aexp2) #:transparent)
(define-struct equal_equal-exp (aexp1 aexp2) #:transparent)
(define-struct not_equal-exp (aexp1 aexp2) #:transparent)
(define-struct list-exp (lst) #:transparent)
(define-struct list_acc-exp (var listmem) #:transparent)
(define-struct parentheses-exp (exp) #:transparent)
(define-struct neg-exp (exp) #:transparent)


;start represntation of environment
(define empty-env
  (lambda () '()))

(define extend-env
  (lambda (var val env)
    (cons (cons var val) env)))

(define apply-env
  (lambda (initial-env search-var)
    (letrec ((loop (lambda (env)
                     (cond ((null? env)
                            (report-no-binding-found search-var initial-env))
                           ((and (pair? env) (pair? (car env)))
                            (let ((saved-var (caar env))
                                  (saved-val (cdar env))
                                  (saved-env (cdr env)))
                              (if (eqv? search-var saved-var)
                                  saved-val
                                  (loop saved-env))))
                           (else
                            (report-invalid-env initial-env))))))
      (loop initial-env))))

;functions for  generating error messages
(define report-no-binding-found
  (lambda (search-var env)
    (displayln (list 'apply-env "No binding for ~a in ~s" search-var env))))

(define report-invalid-env
  (lambda (env)
    (displayln (list 'apply-env "Bad environment ~s" env))))


;env
(define init-env
(lambda ()
(empty-env)))

(define env (init-env))

;while statement
(define (while condition body)
  (when (condition)
    (body)
    (while condition body)))

;merge two lists 
(define addToList
  (lambda (a b) 
    (cond ((null? a) (list b)) ; outcome must be a list
          ((cons (car a) (addToList (cdr a) b))))))

(define neglist
  (lambda (lst)
    (cond
      ((null? lst) '())
      ((boolean? (car lst)) (cons (not (car lst)) (neglist (cdr lst))))
      ((number? (car lst)) (cons (- 0 (car lst)) (neglist (cdr lst))))
      ((list? (car lst)) (cons (neglist (car lst)) (neglist (cdr lst))))
      (else (error 'TypeError "Bad operand type for unary -: '~a'" (typeof (car lst))))
      )))

;parser for mathematical expressions
(define simple-math-parser
           (parser
            (start command)
            (end EOF)
            (error void)
            (tokens a b)
            (grammar
             (command ((unitcom) $1)
                      ((command SEMICOLON unitcom) (make-run-cmd $1 $3)))
             (unitcom ((WHILE exp DO command END) (make-while-com $2 $4))
                      ((IF exp THEN command ELSE command END) (make-if-com $2 $4 $6))
                      ((ID EQUAL exp) (make-assign $1 $3))
                      ((RETURN exp) (return $2)))
             (exp ((aexp) $1)
                  ((aexp GREATER aexp) (make-unequal-exp > $1 $3))
                  ((aexp LESS aexp) (make-unequal-exp < $1 $3))
                  ((aexp EQUALEQUAL aexp) (make-equal_equal-exp $1 $3))
                  ((aexp NOTEQUAL aexp) (make-not_equal-exp $1 $3)))
             (aexp ((bexp) $1)
                   ((bexp MINUS aexp) (make-arith-exp - $1 $3))
                   ((bexp PLUS aexp) (make-arith-exp + $1 $3)))
             (bexp ((cexp) $1)
                   ((cexp MULT bexp) (make-arith-exp * $1 $3))
                   ((cexp DIV bexp) (make-arith-exp / $1 $3)))
             (cexp ((MINUS cexp) (make-neg-exp  $2))   
                   ((LPARAN exp RPARAN) (make-parentheses-exp $2))
                   ((NUM) (num-exp $1))
                   ((NULL) (null-exp))
                   ((ID) (var-exp $1))
                   ((TRUE) (bool-exp #t))
                   ((FALSE) (bool-exp #f))
                   ((STRING) (str-exp (substring $1 1 (- (string-length $1) 1))))
                   ((list) $1)
                   ((ID listmem) (make-list_acc-exp $1 $2)))
             (list ((LBARAK listValues RBARAK) (make-list-exp $2))
                   ((LBARAK RBARAK) (list '())))
             (listValues ((exp) (list $1))
                         ((exp comma listValues) (cons $1 $3)))
             (listmem ((LBARAK exp RBARAK) (list $2))
                      ((LBARAK exp RBARAK listmem) (cons $2 $4)))
             
             )))

;define other expressions
(define (typeof expr)
  (cond
    ((string? expr) 'string)
    ((boolean? expr) 'boolean)
    ((equal? 'null expr) 'null)
    ((number? expr) 'number)
    (else 'list)))
(define return_value 0)
(define end #f)
(define (is-zero flag)
  (and (number? flag) (equal? (exact->inexact flag) 0.0))
  )

;;;;;;; fateme's part starts here

(define (eval parsed-exp )
  
  (match parsed-exp
    ((run-cmd unitcom comm)
     (eval unitcom )
     (if (not end)
         (eval comm )
         return_value))

    ((while-com exp com)
     (define condition (calculate exp ))
     (if (is-zero condition) (set! condition #f) '())
     (loop go ([con condition])
           (cond
            [con [begin
                         (eval com )
                         (let ([flag (calculate exp )])
                           (go (and (not (is-zero flag)) flag)))]]
            [else '()])))
    
    ((if-com exp thencom elsecom)
     (let ([flag (calculate exp )])
       (if (and (not (is-zero flag)) flag) (eval thencom ) (eval elsecom ))
       ))
    
    ((assign var exp)
     (set! env (extend-env var (calculate exp) env))
     )

    ((return exp)
     (set! return_value (calculate exp ))
     (set! end #t)
     return_value
     )  
    ))

(define (error-not-supported op op1 op2)
  (error 'TypeError "'~a' not feasible between '~a' and '~a'"
                 (if (equal? op <) '< '>)
                 (typeof op1)
                 (typeof op2))
  )

(define (list-number-unequal op lst num)
  (cond
            [(not (number? (car lst )))
             (error-not-supported op (car lst) num)] 
            [(equal? (length lst) 1) (op (car lst ) num)]
            [else (if (op (car lst ) num)
             (calculate (make-unequal-exp op (list (cdr lst)) num))
             #f)]) ;list > number
  )

(define (list-string-unequal op lst str e2)
  [begin
    (define str_op string<?)
    (cond [(equal? op >) (set! str_op string>?)]
          [else (set! str_op string<?)])
    (cond
      [(not (string? (car lst )))
       (error-not-supported op (car lst) str)]
      [(equal? (length lst) 1) (str_op (car lst ) str)]
      [else (if (str_op (car lst ) str)
                (calculate (make-unequal-exp op (list (cdr lst)) e2))
                #f)])] ;list > string
  )


(define (list-has-error tmp i)
  (cond
    [(not(list? tmp)) (error 'TypeError "A '~a' object does not behave like an iterable one" (typeof tmp))]
    [(> i (sub1 (length tmp))) (error 'IndexError "array index out of range")]
    [else #f]
  ))


(define (calculate exp)
  (match exp

    ((list_acc-exp var listmem)
    (define lst (apply-env env var))
    (define idx '())
    (define tmp '())
    (set! tmp lst)
    (define o '())
    (if (list? lst)
    (begin
     (for ([i listmem])
       (let ([x (calculate i)])
          (cond [(not (number? x)) (error 'TypeError "~a cannot be a list index" (typeof x))]
                [(not (exact-integer? x)) (error 'TypeError "a float is not list index material")]
                [(< x 0) (error 'IndexError "index below zero")]
                [else (set! idx (addToList idx x))])
         
       ))
     (let  ([n (length idx)])
     (do ((i 0 (+ i 1))) ((= i n))
       (if (< i (sub1 n)) (begin
                            (cond [(not (list-has-error tmp (list-ref idx i)))  (set! tmp (list-ref tmp (list-ref idx i)))]
                          ))
                         (begin
                           (cond [(not (list-has-error tmp (list-ref idx i)))
                                  (set! o (addToList o (list-ref tmp (list-ref idx i))))]
                          )))
     ))) 
    (error 'TypeError "A '~a' object does not behave like an iterable one" (typeof lst)))
    (car o)
    )

    ((list-exp lst)
     (define l '())
     (for ([i lst])
       (set! l (addToList l (calculate i))) 
       )
     l
     )

    ((parentheses-exp exp)
     (calculate exp)
     )

   ((neg-exp exp)
     (let ([o (calculate exp)])
        (cond
                   [(boolean? o) (not o)]
                   [(number? o)  (- 0 o)]
                   [(list? o)  (neglist o) ]
                   [else
                    (error 'TypeError "Type mismatch in unary -: '~a'" (typeof o))
                    ]
                   ))
     )

    
    ((unequal-exp op e1 e2)
     (let ([op1 (calculate e1)] [op2 (calculate e2)])
       (cond
         [(or (boolean? op1) (equal? 'null op1) (boolean? op2) (equal? 'null op2))
          (error-not-supported op op1 op2)
          ]
         
         [(and (list? op1) (not (null? op1)) (or (boolean? (car op1)) (equal? 'null (car op1))))
          (error-not-supported op (car op1) (car op2))
          ]

         [(and (list? op2) (not (null? op2)) (or (boolean? (car op2)) (equal? 'null (car op2))))
          (error-not-supported op (car op1) (car op2))
          ]

         [(and (list? op1) (list? op2))
          (error-not-supported op op1 op2)
          ]

         [(or (null? op1) (null? op2)) #f]

         [(and (list? op1) (number? op2))
          (list-number-unequal op op1 op2)
          ]
         
         [(and (number? op1) (list? op2))
          (list-number-unequal op op2 op1)
          ]

         [(and (list? op1) (string? op2))
          (list-string-unequal op op1 op2 e2)
          ]

         [(and (string? op1) (list? op2))
          (list-string-unequal op op2 op1 e2)
          ]

         [(and (string? op1) (string? op2))
          (if (equal? op >) (string>? op1 op2) (string<? op1 op2))] ;string > string
         
         [(or (string? op1) (list? op1) (string? op2) (list? op2))
          (error-not-supported op op1 op2)
          ]

         [else (op (calculate e1 ) (calculate e2 ))] ; why?
         )))

    ;;;;;;;;;; fateme's part ends here
    
    ((equal_equal-exp e1 e2)
     (let ([op1 (calculate e1 )] [op2 (calculate e2 )])
       (cond
         [(and (equal? 'null op1) (equal? 'null op2)) #t]
         
         [(and (list? op1) (list? op2))
          (cond
            [(and (null? op1) (null? op2)) #t]
            [(not (equal? (length op1) (length op2))) #f] 
            [(and (number? (car op1)) (number? (car op2)) (equal? (exact->inexact (car op1 )) (exact->inexact (car op2))))
             (calculate (make-equal_equal-exp (list (cdr op1)) (list (cdr op2))) )] 
            [(equal? (car op1 ) (car op2))
             (calculate (make-equal_equal-exp (list (cdr op1)) (list (cdr op2))) )]
            [else #f])]

         [(and (string? op1) (string? op2)) (equal? op1 op2)]
         [(and (boolean? op1) (boolean? op2)) (equal? op1 op2)]
          
       
         [else (if (and (number? op1) (number? op2))
                   (equal? (exact->inexact op1) (exact->inexact op2))
                   (equal? op1 op2))]
        )))

    ((not_equal-exp e1 e2) (not (calculate (make-equal_equal-exp e1 e2) )))
    
    ((arith-exp op e1 e2)
     (let ([op1 (calculate e1 )] [op2 (calculate e2 )])
       (cond
         
         [(and (number? op1) (number? op2))
          (op op1 op2)]

         [(and (boolean? op1) (boolean? op2))
          (cond
            [(equal? op +) (if op1 #t op2)]
            [(equal? op *) (if op1 op2 #f)]
            [else (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond
                                                                                          [(equal? op -) '-]
                                                                                          [(equal? op /) '/]) (typeof op1) (typeof op2))])]
         
          [(and (string? op1) (string? op2))
          (if (equal? op +)
              (string-append op1 op2)
              (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond
                                                                                      [(equal? op -) '-]
                                                                                      [(equal? op *) '*]
                                                                                      [(equal? op /) '/]) (typeof op1) (typeof op2)))]
          [(and (list? op1) (list? op2))
          (if (equal? op +)
              (append op1 op2)
              (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond
                                                                                      [(equal? op -) '-]
                                                                                      [(equal? op *) '*]
                                                                                      [(equal? op /) '/]) (typeof op1) (typeof op2)))]

          [(and (number? op1) (list? op2))
          (num-list-arith op op1 op2 #f)]
         
         [(and (list? op1) (number? op2))
          (num-list-arith op op2 op1 #t)]
         
         
         [(and (boolean? op1) (list? op2))
          (bool-list-arith op op1 op2)]
         
         [(and (list? op1) (boolean? op2))
          (bool-list-arith op op2 op1)]
         
         [(and (string? op1) (list? op2))
          (str-list-arith op op1 op2)]
         
         [(and (list? op1) (string? op2))
          (str-list-arith op op2 op1)]

         [else (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond
                                                                                       [(equal? op +) '+]
                                                                                       [(equal? op -) '-]
                                                                                       [(equal? op *) '*]
                                                                                       [(equal? op /) '/]) (typeof op1) (typeof op2))]
         )))
    
    ((num-exp n) n)
    
    ((bool-exp bool) bool)

    ((str-exp str) str)
    
     ((var-exp var)
      (apply-env env var))

    ((null-exp) 'null)
    
    ((list exp) exp) 
    ))

(define num-list-arith (lambda (op op1 op2 invert)
                  (define output '())
                  (if (and (equal? op *) (equal? (exact->inexact op1) 0.0))                                                  
                      (set! output 0)
                      [begin
                        (for [(item op2)]
                          (if (not (number? item))
                              (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond
                                                                                                      [(equal? op +) '+]      ; error dare mide, ma ke error nadarim pas age in bashe lo mire
                                                                                                      [(equal? op -) '-]
                                                                                                      [(equal? op *) '*]
                                                                                                      [(equal? op /) '/])(typeof op1) (typeof item))
                              (set! output (addToList output (if (equal? invert #t) (op item op1) (op op1 item))))))])    ; add to list (op op1 item)ro mizare tahe list
                  output   
                  ))

(define bool-list-arith (lambda (op op1 op2)
                          (define output '())
                  (for [(item op2)]
                    (if (not (or (equal? op +) (equal? op *)))                                       ; fargesh ba list o int ine ke faghat 2 ta operator e valid dare na 4 ta
                        (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond                     
                                                                                                       [(equal? op -) '-]            
                                                                                                       [(equal? op /) '/]) (typeof op1) (typeof op2))
                        (if (not (boolean? item))
                            (error 'TypeError "Incompatible types passed to operation ~a: '~a' and '~a'" (cond
                                                                                                           [(equal? op +) '+]
                                                                                                           [(equal? op *) '*]) (typeof op1) (typeof item))
                            (cond
                              [(equal? op +) (if op1 (set! output (addToList output #t)) (set! output (addToList output item)))]   ;or
                              [else (if op1 (set! output (addToList output item)) (set! output (addToList output #f)))]))))        ; and
                  output))

(define str-list-arith (lambda (op op1 op2)                                                                                         ;str faghat append mishe
                         (define output '())
                  (if (equal? op +)
                      (for [(item op2)]
                        (if (not (string? item))
                            (error 'TypeError "Incompatible types passed to operation +: '~a' et '~a'" (typeof op1) (typeof item))
                            (set! output (addToList output (string-append op1 item)))))
                      (error 'TypeError "Incompatible types passed to operation ~a: '~a' et '~a'" (cond
                                                                                              [(equal? op -) '-]
                                                                                              [(equal? op *) '*]
                                                                                              [(equal? op /) '/]) (typeof op1) (typeof op2)))
                  output))



(define evaluate
  (lambda (filename)
  (begin
  (define path filename)
  (define port (open-input-file path))
  (define str (port->string port))
  (define lex-this (lambda (lexer input) (lambda () (lexer input))))
   (define my-lexer (lex-this simple-math-lexer (open-input-string str)))
    (simple-math-parser my-lexer)
    (eval (simple-math-parser (lex-this simple-math-lexer (open-input-string str)))))))

(evaluate "a.txt")




