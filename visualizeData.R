require("dplyr")
require("scales")
require("ggplot2")
require("foreach")
args <- commandArgs(TRUE)
filename <- "RandomWalkSimulation.csv"
df <- read.csv(filename)
colnames(df) <- c("vertices","edges","algorithm","path_length")
df <- tbl_df(df)
df <- arrange(df,edges,vertices)

png("plot.png")
graph <- ggplot(df, aes(x=edges,y=path_length)) + geom_point(size = 0.02) + geom_smooth()
graph <- graph + ggtitle(paste(df$algorithm, " Performance")) + xlab("Number of Edges") + ylab("Average Path Length")
graph
dev.off()