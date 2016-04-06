  require("dplyr")
  require("scales")
  require("ggplot2")
  require("foreach")
  args <- commandArgs(TRUE)
  filename <- "RandomWalkSimulation.csv"
  df <- read.csv(filename)
  colnames(df) <- c("vertices","edges","algorithm","path_length","included_failiure")
  df <- tbl_df(df)
  df <- arrange(df,included_failiure,vertices)
  df <- df[2:nrow(df),]
  #png(paste(df$vertices, df$algorithm, " Performance", ".png"))
  
  graph <- ggplot(df, aes(x=edges,y=path_length)) + geom_line(color="grey") + geom_point(size = 0.2, aes(color = included_failiure)) + geom_smooth(se=TRUE)
  graph <- graph + ggtitle(paste(df$vertices, " ",df$algorithm, " Performance"))+ xlab("Number of Edges") + ylab("Average Path Length")
  graph <- graph + theme_minimal() + scale_size_area() + scale_colour_hue(l=40)
  graph
  #dev.off()