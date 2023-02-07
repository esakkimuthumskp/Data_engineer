importsnscrape.modules.twitterassntwitter
importpandasaspd
#!pipinstallgoogletrans==3.1.0a0
importtime
fromsocial_media.datacleanimportClean


classTwitter_Scrape:
def__init__(self):
self.translator='m'
defScrape(self,Data_obj,limit):
tweets=[]
fori,tweetinData_obj:
ifi>limit:
break
try:
mentioneduser=[tweet.mentionedUsers[x].usernameforxinrange(len(tweet.mentionedUsers))]
except:
mentioneduser=''
tweets.append([tweet.date,tweet.id,tweet.content,tweet.lang,mentioneduser,tweet.hashtags,tweet.retweetCount,tweet.likeCount,tweet.replyCount,tweet.user.username,tweet.user.followersCount,tweet.user.verified])
returnpd.DataFrame(tweets,columns=['Datetime','TweetId','content','lang','mentionedUser','hashtags','retweet','like','replyCount','Username','followersCount','verified',])

defProfileTweets(self,Username,limit):
returnself.Scrape(enumerate(sntwitter.TwitterSearchScraper("from:"+Username).get_items()),limit)

defSearch(self,Text,limit):
returnself.Scrape(enumerate(sntwitter.TwitterSearchScraper(Text).get_items()),limit)

defHashtagTweets(self,Hashtag,limit):
returnself.Scrape(enumerate(sntwitter.TwitterHashtagScraper(Hashtag).get_items()),limit)

defTrends(self,limit):
df=pd.DataFrame()
form,iinenumerate(sntwitter.TwitterTrendsScraper().get_items()):
ifi.domainContext=='Politics·Trending':
df2=self.Scrape(enumerate(sntwitter.TwitterHashtagScraper(i.name).get_items()),limit)
df2['treadingHashTag']=[i.name]*len(df2)
ifi.metaDescription.endswith('KTweets'):
df2['tweetCount']=[int(''.join([xforxini.metaDescriptionifx.isdigit()]))*1000]*len(df2)
else:
df2['tweetCount']=[int(''.join([xforxini.metaDescriptionifx.isdigit()]))]*len(df2)
df=pd.concat([df,df2])
returndf
