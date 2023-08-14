import tweepy
import pandas as pd 
import json 
from datetime import datetime 
import s3fs


access_key= "hCdOI3YHhkLygjq1UnESXStqc"
access_secret= "CFwqhLKKyx6acHpkGMz7aHrB4Ots6xazycgSmuwT2NFmntoa4V"
consumer_key= "1118823170864287744-d6zD2sg6xenk1SLkwVinyaW6Wir2Iy"
consumer_secret= "V1poTcTeFqou0Q2FMcgMPdfe8rZzB2raeMuFXKzTubmaC"


#Twitter authentication
auth=tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)


#Create an API Object
api=tweepy.API(auth)


tweets=api.user_timeline(screen_name='@elonmusk',
                        count=10,
                        include_rts = False,
                        tweet_mode = 'extended'

)

print(tweets)