import android
import os
import math

layout="""
<? xml version="1.0" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:orientation="vertical" android:layout_width="fill_parent"
android:layout_height="fill_parent" android:background="#ff000000">

<LinearLayout android:orientation="vertical" android:layout_width="fill_parent" android:layout_height="fill_parent">

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/play" android:text="Play" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
<Button android:id="@+id/pause" android:text="Pause" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Spinner android:id="@+id/music" android:layout_width="fill_parent" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:id="@+id/progress" android:text="Progress: 0%" android:layout_width="wrap_content"
          android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/exit" android:text="Exit" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

</LinearLayout>

</LinearLayout>
"""

droid = android.Android()
playerTag = "MyMusic"

mediaList=[]

def getMedia():
    global mediaList
    for dirname, dirnames, filenames in os.walk("/sdcard/sl4a/media/"):
        for filename in filenames:
            mediaList.append(filename)

def main():
    droid.fullShow(layout)
    getMedia()
    droid.fullSetList("music", mediaList)

    pausePos = 0
    curMediaUrl = ""
    while True:
        event = droid.eventWait(100).result
        if event == None:
            if droid.mediaIsPlaying(playerTag).result:
                duration = droid.mediaPlayInfo(playerTag).result['duration']
                position = droid.mediaPlayInfo(playerTag).result['position']
                progress = int(math.ceil((float(position) / duration) * 100))
                droid.fullSetProperty("progress", "text", "Progress: " + str(progress) + "%")
        elif event['name'] == "click":
            id = event["data"]["id"]
            if id == "play":
                mediaName = mediaList[int(droid.fullQueryDetail("music").result['selectedItemPosition'])]
                mediaUrl = "/sdcard/sl4a/media/" + mediaName
                if curMediaUrl == mediaUrl:
                    droid.mediaPlayStart(playerTag)
                    droid.mediaPlaySeek(pausePos)
                else:
                    droid.mediaPlay(mediaUrl, playerTag, True)
                    curMediaUrl = mediaUrl
            elif id == "pause":
                if droid.mediaIsPlaying(playerTag).result:
                    pausePos = droid.mediaPlayInfo(playerTag).result['position']
                    droid.mediaPlayPause(playerTag)
            elif id == "exit":
                break;

    droid.fullDismiss()

if __name__ == "__main__":
    main()
