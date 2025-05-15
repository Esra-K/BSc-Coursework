library(dplyr)
library(ggplot2)
library(GGally)

fifa <- read.csv("Data/players_20.csv")
selected_columns <- c("short_name", "value_eur", "age", "height_cm", "weight_kg",  "nationality", "club", 
                      "wage_eur", "release_clause_eur", "overall", "potential", "player_positions", "preferred_foot", "international_reputation",
                      "weak_foot", "work_rate", "joined", "contract_valid_until")

score_components <- c("attacking_crossing", "attacking_finishing", "attacking_heading_accuracy", "attacking_short_passing", "attacking_volleys",
                      "skill_dribbling", "skill_curve", "skill_fk_accuracy", "skill_long_passing", "skill_ball_control",
                      "movement_acceleration", "movement_sprint_speed", "movement_agility", "movement_reactions", "movement_balance",
                      "power_shot_power", "power_jumping", "power_stamina", "power_strength", "power_long_shots",
                      "mentality_aggression", "mentality_interceptions", "mentality_positioning", "mentality_vision", "mentality_penalties", "mentality_composure",
                      "defending_marking", "defending_standing_tackle", "defending_sliding_tackle",
                      "goalkeeping_diving", "goalkeeping_handling", "goalkeeping_kicking", "goalkeeping_positioning", "goalkeeping_reflexes")
fifa_selected <- fifa[, c(selected_columns, score_components)]

fifa_selected$value_eur <- log(fifa_selected$value_eur)
fifa_selected$wage_eur <- log(fifa_selected$wage_eur)
fifa_selected$release_clause_eur <- log(fifa_selected$release_clause_eur)
fifa_selected$agesquare <- fifa_selected$age * fifa_selected$age
print(fifa_selected$agesquare)

goalkeeper <- c("GK")
attacker <- c("LW", "RF", "CF", "LF", "RF", "ST", "LS", "RS", "RW")
midfielder <- lapply(c("rdm", "cdm", "ldm", "rcm", "cm", "lcm", "lam", "cam", "ram", "rm", "lm"), toupper)
defender <- c("RCB", "LCB", "RB", "LB", "CB", "RWB", "LWB")
for (i in 1:nrow(fifa_selected)) {
  position_arr <- c(strsplit(as.character(fifa_selected$player_positions[i]), ", "))[[1]]
  # print(class(midfielder))
  # print(position_arr)
  p <- c(sum(position_arr %in% goalkeeper), sum(position_arr %in% attacker)
        , sum(position_arr %in% midfielder), sum(position_arr %in% defender))
  ind_of_max = which.max(p)
  for(j in 1:length(p)){
    if(j == ind_of_max){
      p[j] <- 1
    }else{
      p[j] <- 0
    }
  }
  fifa_selected$goalkeeper[i] <- p[1]
  fifa_selected$attacker[i] <- p[2]
  fifa_selected$midfielder[i] <- p[3]
  fifa_selected$defender[i] <- p[4]
  # print(sum(position_arr %in% goalkeeper))
  # print(sum(position_arr %in% attacker))
  # print(sum(position_arr %in% midfielder))
  # print(sum(position_arr %in% defender))
}

positions <- c("goalkeeper", "defender", "midfielder", "attacker")
technical_criteria <- c("attacking", "skill", "power", "movement", "mentality", "defending", "goalkeeping")
# fifa_selected <- mutate(fifa_selected, attacking = rowMeans(select(fifa_selected, starts_with("attacking")), na.rm = TRUE))
# fifa_selected <- mutate(fifa_selected, skill = rowMeans(select(fifa_selected, starts_with("skill")), na.rm = TRUE))
# fifa_selected <- mutate(fifa_selected, power = rowMeans(select(fifa_selected, starts_with("power")), na.rm = TRUE))
# fifa_selected <- mutate(fifa_selected, movement = rowMeans(select(fifa_selected, starts_with("movement")), na.rm = TRUE))
# fifa_selected <- mutate(fifa_selected, mentality = rowMeans(select(fifa_selected, starts_with("mentality")), na.rm = TRUE))
# fifa_selected <- mutate(fifa_selected, defending = rowMeans(select(fifa_selected, starts_with("defending")), na.rm = TRUE))
# fifa_selected <- mutate(fifa_selected, goalkeeping = rowMeans(select(fifa_selected, starts_with("goalkeeping")), na.rm = TRUE))

fifa_selected[, technical_criteria] <- c(0,0,0,0,0,0,0)
categories <- list(c(19:23), c(24:28), c(29:33), c(34:38), c(39:44), c(45:47), c(48:52))
cors <- list()
# fifa_selected <- subset( fifa_selected, select = -c(club, nationality ))
fifa_selected <- fifa_selected[complete.cases(fifa_selected), ]
fifa_selected <- fifa_selected[!is.nan(fifa_selected$value_eur), ]

for(i in 1:length(categories)){
    # print(lapply(fifa_selected[, categories[[i]]], class))
    cors[[i]] <- cor(fifa_selected[, categories[[i]]], fifa_selected$value_eur)
}


for (i in 1:nrow(fifa_selected)){
  print(i)
  fifa_selected[i, ]$attacking <- sum(fifa_selected[i, categories[[1]]] * cors[[1]])
  fifa_selected[i, ]$skill <- sum(fifa_selected[i, categories[[2]]] * cors[[2]])
  fifa_selected[i, ]$movement <- sum(fifa_selected[i, categories[[3]]] * cors[[3]])
  fifa_selected[i, ]$power <- sum(fifa_selected[i, categories[[4]]] * cors[[4]])
  fifa_selected[i, ]$mentality <- sum(fifa_selected[i, categories[[5]]] * cors[[5]])
  fifa_selected[i, ]$defending <- sum(fifa_selected[i, categories[[6]]] * cors[[6]])
  fifa_selected[i, ]$goalkeeping <- -1 * sum(fifa_selected[i, categories[[7]]] * cors[[7]])
}

fifa_selected <- fifa_selected[, c(selected_columns, technical_criteria, positions, "agesquare")]
fifa_selected <- subset( fifa_selected, select = -c(player_positions) )


date_to_num <- function(d_arr){
  as.numeric(as.Date(d_arr))
}

# fifa_selected$dob <- date_to_num(fifa_selected$dob)
fifa_selected$joined <- date_to_num(fifa_selected$joined)

convert_work_rate <- function(wr){
  wr <- c(strsplit(as.character(wr), "/"))[[1]]
  score <- 0
  for(i in 1:length(wr)){
    inc <- if (wr[i] == "Low") 0 else (if (wr[i] == "Medium") 1 else 2)
    score <- score + inc
  }
  score
}

fifa_selected$work_rate <- mapply(convert_work_rate, fifa_selected$work_rate)

fifa_selected <- fifa_selected %>% 
  mutate(preferred_foot = if_else(preferred_foot == "Right", 0, 1))

top_clubs <- c("FC Barcelona", "Juventus", "Paris Saint-Germain", "Atlético Madrid", "Real Madrid",
              "Manchester City", "Liverpool", "Napoli", "Tottenham Hotspur", "Manchester United",
              "Chelsea", "FC Bayern München", "Inter", "Borussia Dortmund", "Arsenal",
              "Lazio", "Milan")


top_countries <- c("Brazil", "Argentina", "Uruguay", "Colombia", "Chile",
                   "France", "Belgium", "England", "Netherlands", "Germany", "Spain", "Croatia", "Serbia",
                   "Mexico", "United States", 
                   "Cameroon", "Ivory Coast", "Nigeria")

fifa_selected <- fifa_selected %>% 
  mutate(big_team = if_else(club %in% top_clubs, 1, 0))

fifa_selected <- fifa_selected %>% 
  mutate(big_country = if_else(nationality %in% top_countries, 1, 0))
fifa_selected <- subset( fifa_selected, select = -c(club, nationality ))
fifa_selected <- fifa_selected[complete.cases(fifa_selected), ]
fifa_selected <- fifa_selected[!is.infinite(fifa_selected$value_eur), ]

pdf("Results/correlations2.pdf", height = 7, width = 7)
g <- ggcorr(fifa_selected)
print(g)
dev.off()

