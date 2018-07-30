#Find correlation value between all pairs of features (a,b,c,d,e,f,g) in the above dataset constructed using R.

mydata <- read.csv("SrBachchan_tweets.csv", header = TRUE)

#for(i in 1:4)
#{
#	for(j in 1:4)
#	{
#		core <- cor(mydata[,i], mydata[,j])
#		print(paste(i, "and", j, "::"))
#		print(core)
#	}
#	
#}
