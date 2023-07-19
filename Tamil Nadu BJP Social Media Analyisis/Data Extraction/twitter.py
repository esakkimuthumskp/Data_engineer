import snscrape.modules.twitterassntwitter
import pandas as pd
#!pipinstallgoogletrans==3.1.0a0
import time
from social_media.dataclean import Clean


class Twitter_Scrape:
   def__init__(self):
      self.translator='m'
   def Scrape(self,Data_obj,limit):
      tweets=[]
        for i,tweet in Data_obj:
          if i>limit:
            break
          try:
            mentioneduser=[tweet.mentionedUsers[x].usernameforxinrange(len(tweet.mentionedUsers))]
          except:
            mentioneduser=''
            tweets.append([tweet.date,tweet.id,tweet.content,tweet.lang,mentioneduser,tweet.hashtags,tweet.retweetCount,tweet.likeCount,tweet.replyCount,tweet.user.username,tweet.user.followersCount,tweet.user.verified])
      return pd.DataFrame(tweets,columns=['Datetime','TweetId','content','lang','mentionedUser','hashtags','retweet','like','replyCount','Username','followersCount','verified',])

  def ProfileTweets(self,Username,limit):
    return self.Scrape(enumerate(sntwitter.TwitterSearchScraper("from:"+Username).get_items()),limit)

  def Search(self,Text,limit):
    return self.Scrape(enumerate(sntwitter.TwitterSearchScraper(Text).get_items()),limit)

  def HashtagTweets(self,Hashtag,limit):
    return self.Scrape(enumerate(sntwitter.TwitterHashtagScraper(Hashtag).get_items()),limit)

  def Trends(self,limit):
    df=pd.DataFrame()
    for m,i in enumerate(sntwitter.TwitterTrendsScraper().get_items()):
      if i.domainContext=='Politics·Trending':
        df2=self.Scrape(enumerate(sntwitter.TwitterHashtagScraper(i.name).get_items()),limit)
        df2['treadingHashTag']=[i.name]*len(df2)
      if i.metaDescription.endswith('KTweets'):
        df2['tweetCount']=[int(''.join([xforxini.metaDescriptionifx.isdigit()]))*1000]*len(df2)
      else:
        df2['tweetCount']=[int(''.join([xforxini.metaDescriptionifx.isdigit()]))]*len(df2)
      df=pd.concat([df,df2])
    return df
