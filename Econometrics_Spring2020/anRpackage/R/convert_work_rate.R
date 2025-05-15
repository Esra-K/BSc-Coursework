convert_work_rate <-
function(wr){
  wr <- c(strsplit(as.character(wr), "/"))[[1]]
  score <- 0
  for(i in 1:length(wr)){
    inc <- if (wr[i] == "Low") 0 else (if (wr[i] == "Medium") 1 else 2)
    score <- score + inc
  }
  score
}
