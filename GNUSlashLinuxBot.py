import praw
import os
cache = open('commentcache.txt', 'a+')

reddit = praw.Reddit(client_id="5gOnG5pa-bxThQ",
                     client_secret="Wnyznb7mGUwYMjlUDsmuR8vNnNM", password=os.environ['PASSWORD'],
                     user_agent="such_creative", username='GNUSlashLinuxBot')


def is_pro_gnu_linux(words):
    linuxoccurs = words.count("linux")
    gnulinuxoccurs = words.count("gnu/linux")
    print(linuxoccurs, gnulinuxoccurs)
    prognulinux = True if gnulinuxoccurs > linuxoccurs \
        else None if gnulinuxoccurs == linuxoccurs \
        else False
    return prognulinux

print('bot is ready.')

for i in reddit.subreddit("Makefile_dot_in_user").stream.comments(pause_after=6):
    print(i.body)
    parent = i.parent()
    if parent.fullname not in cache.readlines():
        body = i.body.lower()
        if i.author == "Makefile_dot_in": print(body)
        words = body.split(" ")
        parentWords = parent.body.split(" ") if hasattr(parent, "body") else parent.selftext.split(" ")\
        if hasattr(parent, "selftext") else parent.title.split(" ")
        print(body.count('linux'))
        if "linux" in body:
            isParentProGNULinux = is_pro_gnu_linux(parentWords)
            isCommentProGNULinux = is_pro_gnu_linux(words)
            print(isParentProGNULinux, isCommentProGNULinux)
            if isCommentProGNULinux is not None and isParentProGNULinux is not None and not isParentProGNULinux == isCommentProGNULinux:
                cache.write("\n"+i.fullname)
                try:
                    i.reply("""
[It's all very simple.](https://i.redd.it/5a1k8tf6ogjz.png).

___

^I'm ^a ^bot, ^beep ^boop ^| ^Image ^by ^[u\/Cukta](/u/Cukta)""")
                except:
                    continue

