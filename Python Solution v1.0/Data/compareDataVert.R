require("dplyr")
require("scales")
require("ggplot2")
require("foreach")
temp = list.files(pattern="*.csv")
myfiles = lapply(temp, read.csv, header = FALSE)
assign('df',do.call(rbind , myfiles))
colnames(df) <- c("vertices","edges","algorithm","path_length","included_failure","space","time")
df <- unique(df)


#dfA <- read.csv(filename1)
#dfB <- read.csv(filename2)
colnames(df) <- c("vertices","edges","algorithm","path_length","included_failure","space","time")
df <- tbl_df(df)
df <- arrange(df,included_failure,vertices)
df <- df[2:nrow(df),]
failureDf <- filter(df, included_failure == "True")

#selects the two algorithms being compared
algdf <- arrange(df,algorithm)
algA <- algdf[1,3]
algB <- algdf[nrow(algdf),3]
#png(paste(df$vertices, " Vertex Comparison of Path Length.png"))
graph <- ggplot(df, aes(x=edges,y=path_length, color=vertices)) + geom_line(data=subset(df, algorithm == "bfs"), color="grey") + facet_grid(.~vertices, scales = "free")
graph <- graph + geom_line(data=subset(df, algorithm == "randomwalk"), color="grey") + geom_jitter(size = 2, shape = 18, aes(color=algorithm))
graph <- graph + geom_smooth(data=subset(df, algorithm == "lazyrandomwalk"),se=TRUE,color="green", size =2) + geom_smooth(data=subset(df, algorithm == "randomwalk"),se=TRUE,color="blue", size =2) + geom_smooth(data=subset(df, algorithm == "bfs"),se=TRUE, color="red", size =2)
graph <- graph + ggtitle(paste("Comparison of Path Length"))+ xlab("Number of Edges") + ylab("Path Length")
graph <- graph + scale_colour_hue(l=30) + geom_vline(data=failureDf,color="red",size=.2,aes(xintercept=edges))
graph
#dev.off()

#png(paste(df$vertices, " Vertex Comparison of Space Per Host.png"))
graph <- ggplot(df, aes(x=edges,y=space, color=vertices)) + geom_jitter(size = 2, shape = 18, aes(color=algorithm)) + facet_grid(.~vertices, scales = "free")
graph <- graph + geom_smooth(data=subset(df, algorithm == "lazyrandomwalk"),se=TRUE,color="green", size =2) + geom_smooth(data=subset(df, algorithm == "randomwalk"),se=TRUE,color="blue", size =2) + geom_smooth(data=subset(df, algorithm == "bfs"),se=TRUE, color="red", size =2)
graph <- graph + ggtitle(paste("Comparison of Space Per Host"))+ xlab("Number of Edges") + ylab("Space per host in bytes")
graph <- graph + scale_colour_hue(l=30) + geom_vline(data=failureDf,color="red",size=.2,aes(xintercept=edges))
graph
#dev.off()

#png(paste(df$vertices, " Vertex Comparison of Running Time.png"))
graph <- ggplot(df, aes(x=edges,y=time, color=algorithm)) + facet_wrap(~vertices, scales = "free", ncol=2) +geom_jitter(size = 2, shape = 18, aes(color=algorithm))
graph <- graph + geom_smooth(data=subset(df, algorithm == "lazyrandomwalk"),se=TRUE,color="green", size =2) + geom_smooth(data=subset(df, algorithm == "randomwalk"),se=TRUE,color="blue", size =2) + geom_smooth(data=subset(df, algorithm == "bfs"),se=TRUE, color="red", size =2)
graph <- graph + ggtitle(paste("Comparison of Running Time in Miliseconds"))+ xlab("Number of Edges") + ylab("Running Time (Miliseconds/Query)")
graph <- graph + scale_colour_hue(l=30) + geom_vline(data=failureDf,color="red",size=.2,aes(xintercept=edges))
graph
#dev.off()
