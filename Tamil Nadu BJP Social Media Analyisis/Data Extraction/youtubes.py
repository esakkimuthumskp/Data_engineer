from googleapiclient.discovery import build
import pandas as pd
from dateutil import parser
import scrapetube
import google_auth_oauthlib
from time import sleep
from social_media.dataclean import Clean
from youtube_comment_downloader import *
from itertools import islice


class YouTube:
    def__init__(self):
        api_key='AIzaSyAyeBV93eJxh4_W3cyFqJz8XaylNgz0xc4'
        channel_id='UCgQEM4eg3aWn1qgo1vy1Qig'
        #youtube=build('youtube','v3',developerKey=api_key)
        api_service_name="youtube"
        api_version="v3"
        self.youtube=build(api_service_name,api_version,developerKey=api_key)


    def get_video_details(self,video_ids):
        all_video_info=[]
        i=len(video_ids)
        j=len(video_ids)
        while True:
            if  0<i-49:
                i-=49
                request=self.youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_ids[i:j])
                response=request.execute()
                j-=49
             else:
                request=self.youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_ids[0:i])
                response=request.execute()
                i=0
                for video in response['items']:
                    stats_to_keep={'snippet':['channelTitle','title','description','tags','publishedAt'],
                                                    'statistics':['viewCount','likeCount','commentCount'],
                                                      'contentDetails':['duration','definition','caption']}
                    video_info={}
                    video_info['video_id']=video['id']

                    for k in stats_to_keep.keys():
                        for v in stats_to_keep[k]:
                            try:
                                video_info[v]=video[k][v]
                            except:
                                video_info[v]=None
                        all_video_info.append(video_info)
            if i==0:
                break

        #df['leader']=[leader]*len(df)
        #df['party']=[party]*len(df)
        return pd.DataFrame(all_video_info)
    def extract_comment(self,video_ids):
    all_video_info=[]
    downloader=YoutubeCommentDownloader()
    for x in video_ids:
        comments=downloader.get_comments_from_url(f'https://www.youtube.com/watch?v={x}')
        for comment in islice(comments,3000):
            comment['videoId']=x
            all_video_info.append(comment)
    return all_video_info
#pd.DataFrame(all_video_info)

#defextract_comment(self,video_ids):
#all_video_info=[]
#try:
#forxinvideo_ids:
#request=self.youtube.commentThreads().list(
#part="snippet,replies",
#videoId=x
#)
#try:
#response=request.execute()
#exceptExceptionasa:
#print(a)
#continue
#forxinresponse['items']:
#all_video_info.append({"videoId":x['snippet']['topLevelComment']['snippet']['videoId'],
#"comment":x['snippet']['topLevelComment']['snippet']['textDisplay'],
#"likeCount":x['snippet']['topLevelComment']['snippet']['likeCount'],
#"publishedAt":x['snippet']['topLevelComment']['snippet']['publishedAt'],
#"Replycount":x['snippet']['totalReplyCount']
#})
#exceptExceptionase:
#print(e)

##df['leader']=[leader]*len(df)
##df['party']=[party]*len(df)
#returnpd.DataFrame(all_video_info)

    def video_id(self,videos_json):
        Links=[x['videoId']forxinvideos_json]
        return Links



if__name__=='__main__':
obj=YouTube()
print(obj.extract_comment("N07PkNpllvw"))

