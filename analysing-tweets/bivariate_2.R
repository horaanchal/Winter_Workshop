#Draw scatter plots between features (hashtag_count,likes_count), (mention_count,likes_count), (hashtag_count,retweet_count) and (mention_count,retweet_count) using R.
library("plyr")

mydata <- read.csv("SrBachchan_tweets.csv", header = TRUE)

#scatterplot
png(file="scatterplot_1.png")
plot(mydata$hashtag_count, mydata$likes_count)
dev.off() 

png(file="scatterplot_2.png")
plot(mydata$mention_count, mydata$likes_count)
dev.off() 

png(file="scatterplot_3.png")
plot(mydata$hashtag_count, mydata$retweet_count)
dev.off() 

png(file="scatterplot_4.png")
plot(mydata$mention_count, mydata$retweet_count)
dev.off() 
