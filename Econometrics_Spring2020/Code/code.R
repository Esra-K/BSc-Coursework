library(ggplot2)

fifa <- read.csv("Data/players_20.csv")

values <- as.data.frame(fifa["value_eur"])
values$log_value <- log10(values$value_eur)
df.m <- reshape2::melt(values[, 2, drop = FALSE], id.vars = NULL)
ggplot(df.m, aes(x = variable, y = value)) + geom_violin()

bottom_players <- values[9000:nrow(values),]

df.m <- reshape2::melt(bottom_players[, 1, drop = FALSE], id.vars = NULL)
ggplot(df.m, aes(x = variable, y = value)) + geom_violin()
ggsave('players9000To18000.jpg', width = 9, height = 16)

boxplot(values$value_eur)
boxplot(values$log_value)

values$scaled_val <- with(values, (value_eur - min(value_eur)) / (max(value_eur) - min(value_eur)))
boxplot(values$scaled_val)
boxplot(log(values$scaled_val))

df.m <- reshape2::melt(values[, 3, drop = FALSE], id.vars = NULL)
ggplot(df.m, aes(x = variable, y = log(value))) + geom_violin()

