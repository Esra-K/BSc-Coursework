# Hello from the other side
# Hi dear, I hope to manage to conduct the best project of the class
# ^_^

# fifa <- read.csv("Data/players_20.csv")
# 
# print(nrow(fifa))
# print(ncol(fifa))
# 
# print(colnames(fifa))
# selected_columns <- c("short_name", "value_eur", "age", "nationality", "club",
#                       "wage_eur", "release_clause_eur", "overall", "potential", "player_positions", "preferred_foot", "international_reputation",
#                       "weak_foot", "skill_moves", "work_rate", "joined", "contract_valid_until")
# 
# score_components <- c("attacking_crossing", "attacking_finishing", "attacking_heading_accuracy", "attacking_short_passing", "attacking_volleys",
#                       "skill_dribbling", "skill_curve", "skill_fk_accuracy", "skill_long_passing", "skill_ball_control",
#                       "movement_acceleration", "movement_sprint_speed", "movement_agility", "movement_reactions", "movement_balance",
#                       "power_shot_power", "power_jumping", "power_stamina", "power_strength", "power_long_shots",
#                       "mentality_aggression", "mentality_interceptions", "mentality_positioning", "mentality_vision", "mentality_penalties", "mentality_composure",
#                       "defending_marking", "defending_standing_tackle", "defending_sliding_tackle",
#                       "goalkeeping_diving", "goalkeeping_handling", "goalkeeping_kicking", "goalkeeping_positioning", "goalkeeping_reflexes")
# 
# fifa_selected <- fifa[, c(selected_columns, score_components)]
# print(summary(fifa_selected))
# 
# fifa_selected$value_eur <- log(fifa_selected$value_eur)
# fifa_selected$wage_eur <- log(fifa_selected$wage_eur)
# fifa_selected$release_clause_eur <- log(fifa_selected$release_clause_eur)
# fifa_selected$age2 <- fifa_selected$age ^ 2
# unique_vals <- lapply(fifa_selected, unique)
# 
# # fileConn<-file("Results/summary.txt")
# # writeLines(summary(fifa_selected), fileConn)
# # close(fileConn)
# 
# assign_position <- function(f){
#   c1 <- as.character(f)
#   c1 <- strsplit(c1, ", ")[[1]]
#   print(c1)
#   goalkeeper <- c("GK")
#   attacker <- c("LW", "RF", "CF", "LF", "RF", "ST", "LS", "RS")
#   midfielder <- lapply(c("rdm", "cdm", "ldm", "rcm", "cm", "lcm", "lam", "cam", "ram", "rm", "lm"), toupper)
#   defender <- c("RCB", "LCB", "RB", "LB", "CB", "RWB", "LWB")
#   position_dummies <- c(0, 0, 0, 0)
#   for (i in 1:length(c1)) {
#     if (c1[i] %in% goalkeeper){
#       position_dummies[1] <- 1
#     }
#     if (c1[i] %in% defender){
#       position_dummies[2] <- 1
#     }
#     if (c1[i] %in% midfielder){
#       position_dummies[3] <- 1
#     }
#     if (c1[i] %in% attacker){
#       position_dummies[4] <- 1
#     }
#   }
#   position_dummies
# }
# fifa_selected$goalkeeper <- 0
# fifa_selected$defender <- 0
# fifa_selected$midfielder <- 0
# fifa_selected$attacker <- 0
# #
# update_position <- function(row){
#   dummies <- assign_position(row$player_positions)
#   row$goalkeeper <- dummies[1]
#   row$defender <- dummies[2]
#   row$midfielder <- dummies[3]
#   row$attacker <- dummies[4]
#   row
# }
# # purrrlyr::by_row(fifa_selected, update_position)
# # fifa_selected <- by(fifa_selected, 1:nrow(fifa_selected), update_position)
# for (i in 1:30) {
#   dummies <- assign_position(fifa_selected[i,]$player_positions)
#   print(dummies[1])
#   fifa_selected[i,]$goalkeeper <- dummies[1]
#   fifa_selected[i,]$defender <- dummies[2]
#   fifa_selected[i,]$midfielder <- dummies[3]
#   fifa_selected[i,]$attacker <- dummies[4]
#   print(fifa_selected[i, c("goalkeeper", "defender", "midfielder", "attacker")])
# }
# 
# # sample <- fifa_selected[1:10, ]
# #
# # sample[, c("goalkeeper", "defender", "midfielder", "forward")] <- mapply(assign_position, sample$player_positions)
# 
# # ordered_by_wage = fifa_selected[order(fifa_selected$value_eur, decreasing = TRUE),]
# # unique(ordered_by_wage$nationality)
# 
# library(dplyr)
# 
# fifa <- read.csv("Data/players_20.csv")
# fifa2 <- fifa[, c("value_eur", "wage_eur")]
# fifa2$value_eur <- log(fifa2$value_eur)
# fifa2$wage_eur <- log(fifa2$wage_eur)
# fifa2 <- fifa2[complete.cases(fifa2), ]
# fifa2 <- fifa2[!is.infinite(rowSums(fifa2)),]
# lmMod2 <- lm(value_eur ~ wage_eur, data=fifa2)  # build the model
# summary(lmMod2)
# #
# #
# fifa3 <- fifa[, c("value_eur", "team_jersey_number")]
# fifa3$value_eur <- log(fifa3$value_eur)
# # fifa2$wage_eur <- log(fifa2$wage_eur)
# fifa3 <- fifa3[complete.cases(fifa2), ]
# fifa3 <- fifa3[!is.infinite(rowSums(fifa3)),]
# lmMod2 <- lm(value_eur ~ team_jersey_number, data=fifa3)  # build the model
# summary(lmMod2)
# 
# lmMod2 <- lm(value_eur ~
#             + potential
#             + weak_foot + work_rate
#             + midfielder + attacker
#             + big_team + international_reputation
#             + dob + joined + contract_valid_until, data=fifa_selected)  # build the model
# 
# 
# 
# lmMod2 <- lm(value_eur ~ potential + big_team + international_reputation, data=fifa_selected)
# summary(lmMod2)
# cor(fifa_selected$international_reputation, resid(lmMod2))
# 
# residuals_and_omitted <- cbind.data.frame(fifa_selected$international_reputation, resid(lmMod2))
# new_regression <- lm(`resid(lmMod2)` ~ `fifa_selected$international_reputation`, data = residuals_and_omitted)
# summary(new_regression)
# library(VIF)
# fifa2 <- fifa_selected[, c("attacking", "power", "movement", "goalkeeping")]
# max(eigen(cor(select_if(fifa2, is.numeric)))$values)/min(eigen(cor(select_if(fifa2, is.numeric)))$values)
# 
fifa_selected2 <- fifa_selected

fifa_selected2$reputation2 <- fifa_selected2$international_reputation ^ 2
fifa_selected2$reputation3 <- fifa_selected2$international_reputation ^ 3
fifa_selected2$weak_foot2 <- fifa_selected2$weak_foot ^ 2
fifa_selected2$weak_foot3 <- fifa_selected2$weak_foot ^ 3
fifa_selected2$work_rate2 <- fifa_selected2$work_rate ^ 2
fifa_selected2$work_rate3 <- fifa_selected2$work_rate ^ 3
fifa_selected2$agesquare <- fifa_selected2$age ^ 2
fifa_selected2$agecube <- fifa_selected2$age ^3
fifa_selected2$potential2 <- fifa_selected2$potential ^ 2
fifa_selected2$potential3 <- fifa_selected2$potential ^ 3
fifa_selected2$overall2 <- fifa_selected2$overall ^ 2
fifa_selected2$overall3 <- fifa_selected2$overall ^ 3
fifa_selected2$height_cm2 <- fifa_selected2$height_cm ^ 2
fifa_selected2$contract_valid_until2 <- fifa_selected2$contract_valid_until ^2
fifa_selected2$joined <- log(fifa_selected2$joined)
fifa_selected2$joined <- log(fifa_selected2$joined)
fifa_selected2$weak_foot <- log(fifa_selected2$weak_foot)
fifa_selected2$power <- log(fifa_selected2$power)
fifa_selected2$movement <- log(fifa_selected2$movement)
fifa_selected2$joined <- log(fifa_selected2$joined)
fifa_selected2$joined <- log(fifa_selected2$joined)

myvals <- c( "age", "big_team", "big_country", "release_clause_eur"
             , "midfielder", "attacker" , "goalkeeper"
             , "international_reputation"
             , "weak_foot", "work_rate"
             , "power", "movement", "skill"
             , "contract_valid_until", "height_cm")#, "joined")
# myvals <- colnames(fifa_selected)[2:27]
fifa_selected2$short_name <- NULL
# fifa_selected2 <- fifa_selected2[fifa_selected2$attacker == 1, c(myvals, "value_eur")]
# fifa_selected2 <- fifa_selected2[300:16000,]
fifa_selected2 <- scale(fifa_selected2)
fifa_selected2 <- data.frame(fifa_selected2)

# print(class(fifa_selected2))
# fifa_selected2 <- fifa_selected2[fifa_selected2$value_eur > 5 & fifa_selected2$value_eur < 8, ]
i <- 0
r <- 0
current <- c()
column <- "power"

old_coeffs <- c(1, 1)
old_ts <- c(1, 1)
while (length(myvals) > 0){
  print("-------------------------------------------------------------------------------------")
  print("-------------------------------------------------------------------------------------")
  # column <- myvals[1]
  print(paste("Round", as.character(i + 1), ": ", column))
  current <- c(current, column)
  # print(current)
  # f <- fifa_selected[, current]
  lmMod2 <- lm(as.formula(paste("value_eur~", paste(current, collapse = "+"))), data = fifa_selected2)
  # print(summary(lmMod2))
  myvals <- myvals[!myvals==column]
  coeffs <- summary(lmMod2)$coefficients[,'Estimate']
  ts <- summary(lmMod2)$coefficients[,'t value']
  tdiffs <- (old_ts - ts[names(ts) != column]) / (old_ts / 100)

  coeff_diffs <- (old_coeffs - coeffs[names(coeffs) != column]) / (old_coeffs/100)
  print("coefficient value diff %:")
  print(coeff_diffs)
  print("coefficient significance diff: %")
  print(tdiffs)
  print(paste("norm of diff", sum(coeff_diffs[(2:length(coeff_diffs))]^2)))
  old_coeffs <- coeffs
  old_ts <- ts
  if (i > 0){
    mat <- cor(fifa_selected2[, current])
    # print(fifa_selected[, current])
    e <- eigen(mat)$values
    print(paste("collinearity index: ", as.character(max(e) / min(e))))
  }

  # print(coeffs)
  print(paste("delta r:", as.character(summary(lmMod2)$adj.r.squared - r)))
  r <- summary(lmMod2)$adj.r.squared
  # ols_vif_toll(lmMod2)
  i <- i + 1
  max <- 0
  # print(paste("len(myvals):", as.character(length(myvals))))
  for(element in myvals){
    print(element)
    residuals_and_omitted <- cbind.data.frame(fifa_selected2[, element], resid(lmMod2))
    # print(head(residuals_and_omitted))
    new_regression <- lm(`resid(lmMod2)` ~ `fifa_selected2[, element]`, data = residuals_and_omitted)
    
    e <- summary(new_regression)$coefficients[,'Estimate']
    t <- summary(new_regression)$coefficients[,'t value']
    
    if(abs(t[names(t) == "`fifa_selected2[, element]`"] +  log(abs(e[names(e) == "`fifa_selected2[, element]`"]))) > max){
      max <- abs(t[names(t) == "`fifa_selected2[, element]`"])
      column <- element
    } 
    
  }
  print(paste("finding best omitted column:", as.character(column)))
  # column <- myvals[1]
  # print(myvals[1])
  # max <- 0
  # for(element in myvals){
  #   if(abs(cor(resid(lmMod2), fifa_selected2[,element]) > max)){
  #     max <- abs(cor(resid(lmMod2), fifa_selected2[,element]))
  #     column <- element
  #   }
  # }
}

remove_outliers <- function(x, na.rm = TRUE, ...) {
  qnt <- quantile(x, probs=c(.25, .75), na.rm = na.rm, ...)
  H <- 1.5 * IQR(x, na.rm = na.rm)
  y <- x
  y[x < (qnt[1] - H)] <- NA
  y[x > (qnt[2] + H)] <- NA
  y
}

fifa_selected2$resi <- lmMod2$residuals
varfunc.ols <- lm(as.formula(paste("value_eur~", paste(current, collapse = "+"))), data = fifa_selected2)
fifa_selected2$varfunc <- varfunc.ols$fitted.values
gls <- lm(as.formula(paste("value_eur~", paste(current, collapse = "+"))), weights = 1/sqrt(varfunc), data = fifa_selected2)
plot(gls)





