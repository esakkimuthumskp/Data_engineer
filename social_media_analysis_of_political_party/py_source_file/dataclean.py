from googletrans import Translator
import re
from langdetect import detect
import emoji
from textblob import TextBlob


def Clean(Str):

  t=re.sub("@[A-Za-z0-9]+","",Str)#Remove@sign
  t=re.sub('#+','',t)
  t=re.sub(r"(?:\@|http?\://|https?\://|www)\S+","",t)#Removehttplinks
  t="".join(t.split())
  t=emoji.demojize(t)
  t=re.sub(r'(:[!_\-\w]+:)','',t)
  t=re.sub(r'[\?\.\!\_\|\-]+(?=[\?\.\!\_\|\-])',"",t)
  t=re.sub(r"(.)\1+",r"\1\1",t)
  try:
    if  detect(t)!='en':
      translator=Translator()
      t=translator.translate(t).text
  except:
      translator=TextBlob(Str)
      try:
        t=translator.translate(to='ta')
        t=str(t.translate(to='en'))
    except:
      t=""
  return t
