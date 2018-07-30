# Compare and analyze the ranges of features (b,c,d,e) using BoxPlots. Plot all boxplots on same graph using R.

mydata <- read.csv("SrBachchan_tweets.csv", header = TRUE)

png(file="boxplot.png")
boxplot(mydata$hashtag_count, mydata$mention_count, mydata$likes_count, mydata$retweet_count)
dev.off()
