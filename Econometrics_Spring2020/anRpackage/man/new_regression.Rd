\name{new_regression}
\alias{new_regression}
\docType{data}
\title{
%%   ~~ data name/kind ... ~~
}
\description{
%%  ~~ A concise (1-5 lines) description of the dataset. ~~
}
\usage{data("new_regression")}
\format{
  The format is:
List of 12
 $ coefficients : Named num [1:2] -0.227111 0.000013
  ..- attr(*, "names")= chr [1:2] "(Intercept)" "`fifa_selected[, element]`"
 $ residuals    : Named num [1:16980] -0.592 -1.3463 0.2755 0.6041 0.0664 ...
  ..- attr(*, "names")= chr [1:16980] "1" "2" "3" "4" ...
 $ effects      : Named num [1:16980] 4.93e-14 -1.32 2.80e-01 5.94e-01 8.01e-02 ...
  ..- attr(*, "names")= chr [1:16980] "(Intercept)" "`fifa_selected[, element]`" "" "" ...
 $ rank         : int 2
 $ fitted.values: Named num [1:16980] -0.062816 0.003972 -0.000475 -0.015 0.008614 ...
  ..- attr(*, "names")= chr [1:16980] "1" "2" "3" "4" ...
 $ assign       : int [1:2] 0 1
 $ qr           :List of 5
  ..$ qr   : num [1:16980, 1:2] -1.30e+02 7.67e-03 7.67e-03 7.67e-03 7.67e-03 ...
  .. ..- attr(*, "dimnames")=List of 2
  .. .. ..$ : chr [1:16980] "1" "2" "3" "4" ...
  .. .. ..$ : chr [1:2] "(Intercept)" "`fifa_selected[, element]`"
  .. ..- attr(*, "assign")= int [1:2] 0 1
  ..$ qraux: num [1:2] 1.01 1
  ..$ pivot: int [1:2] 1 2
  ..$ tol  : num 1e-07
  ..$ rank : int 2
  ..- attr(*, "class")= chr "qr"
 $ df.residual  : int 16978
 $ xlevels      : Named list()
 $ call         : language lm(formula = `resid(lmMod)` ~ `fifa_selected[, element]`, data = residuals_and_omitted)
 $ terms        :Classes 'terms', 'formula'  language `resid(lmMod)` ~ `fifa_selected[, element]`
  .. ..- attr(*, "variables")= language list(`resid(lmMod)`, `fifa_selected[, element]`)
  .. ..- attr(*, "factors")= int [1:2, 1] 0 1
  .. .. ..- attr(*, "dimnames")=List of 2
  .. .. .. ..$ : chr [1:2] "`resid(lmMod)`" "`fifa_selected[, element]`"
  .. .. .. ..$ : chr "`fifa_selected[, element]`"
  .. ..- attr(*, "term.labels")= chr "`fifa_selected[, element]`"
  .. ..- attr(*, "order")= int 1
  .. ..- attr(*, "intercept")= int 1
  .. ..- attr(*, "response")= int 1
  .. ..- attr(*, ".Environment")=<environment: R_GlobalEnv> 
  .. ..- attr(*, "predvars")= language list(`resid(lmMod)`, `fifa_selected[, element]`)
  .. ..- attr(*, "dataClasses")= Named chr [1:2] "numeric" "numeric"
  .. .. ..- attr(*, "names")= chr [1:2] "resid(lmMod)" "fifa_selected[, element]"
 $ model        :'data.frame':	16980 obs. of  2 variables:
  ..$ resid(lmMod)            : num [1:16980] -0.655 -1.342 0.275 0.589 0.075 ...
  ..$ fifa_selected[, element]: num [1:16980] 12600 17722 17381 16267 18078 ...
  ..- attr(*, "terms")=Classes 'terms', 'formula'  language `resid(lmMod)` ~ `fifa_selected[, element]`
  .. .. ..- attr(*, "variables")= language list(`resid(lmMod)`, `fifa_selected[, element]`)
  .. .. ..- attr(*, "factors")= int [1:2, 1] 0 1
  .. .. .. ..- attr(*, "dimnames")=List of 2
  .. .. .. .. ..$ : chr [1:2] "`resid(lmMod)`" "`fifa_selected[, element]`"
  .. .. .. .. ..$ : chr "`fifa_selected[, element]`"
  .. .. ..- attr(*, "term.labels")= chr "`fifa_selected[, element]`"
  .. .. ..- attr(*, "order")= int 1
  .. .. ..- attr(*, "intercept")= int 1
  .. .. ..- attr(*, "response")= int 1
  .. .. ..- attr(*, ".Environment")=<environment: R_GlobalEnv> 
  .. .. ..- attr(*, "predvars")= language list(`resid(lmMod)`, `fifa_selected[, element]`)
  .. .. ..- attr(*, "dataClasses")= Named chr [1:2] "numeric" "numeric"
  .. .. .. ..- attr(*, "names")= chr [1:2] "resid(lmMod)" "fifa_selected[, element]"
 - attr(*, "class")= chr "lm"
}
\details{
%%  ~~ If necessary, more details than the __description__ above ~~
}
\source{
%%  ~~ reference to a publication or URL from which the data were obtained ~~
}
\references{
%%  ~~ possibly secondary sources and usages ~~
}
\examples{
data(new_regression)
## maybe str(new_regression) ; plot(new_regression) ...
}
\keyword{datasets}
