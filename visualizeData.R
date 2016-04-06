  require("dplyr")
  require("scales")
  require("ggplot2")
  require("foreach")
  args <- commandArgs(TRUE)
  filename <- "this.csv"
  df <- read.csv(filename)
  colnames(df) <- c("vertices","edges","algorithm","path_length","included_failure")
  df <- tbl_df(df)
  df <- arrange(df,included_failure,vertices)
  df <- df[2:nrow(df),]
  failureDf <- filter(df, included_failure == "True")
  #png(paste(df$vertices, df$algorithm, " Performance", ".png"))
  
  graph <- ggplot(df, aes(x=edges,y=path_length)) + geom_line(color="grey") + geom_jitter(size = .2) + geom_smooth(se=TRUE)
  graph <- graph + ggtitle(paste(df$vertices, "-Vertex ",df$algorithm, " Performance"))+ xlab("Number of Edges") + ylab("Average Path Length")
  graph <- graph + theme_minimal() + scale_size_area() + scale_colour_hue(l=20) + geom_vline(data=failureDf,color="blue",size=.2,aes(xintercept=edges))
  graph
  #dev.off()
  