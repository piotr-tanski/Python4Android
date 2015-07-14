import android

layout="""
<? xml version="1.0" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:orientation="vertical" android:layout_width="fill_parent"
android:layout_height="fill_parent" android:background="#ff000000">

<LinearLayout android:orientation="vertical" android:layout_width="fill_parent" android:layout_height="fill_parent">

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/start" android:text="Start Locating" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:id="@+id/location" android:text="Unknown Location" android:layout_width="wrap_content"
android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:id="@+id/provider" android:text="Unknown Provider" android:layout_width="wrap_content"
android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/exit" android:text="Exit" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

</LinearLayout>

</LinearLayout>
"""

droid = android.Android()

isStarted = False

def main():
    droid.fullShow(layout)
    global isStarted
    while True:
        event = droid.eventWait(100).result
        
        locEvent = droid.eventWaitFor("location", 100).result
        if locEvent != None and locEvent['name'] == "location":
            droid.eventPoll(1)
            lat = ""
            lng = ""
            try:
                lat = str(locEvent['data']['gps']['latitude'])
                lng = str(locEvent['data']['gps']['longitude'])
                droid.fullSetProperty("provider", "text", "Provider: GPS")
            except KeyError:
                lat = str(locEvent['data']['network']['latitude'])
                lng = str(locEvent['data']['network']['longitude'])
                droid.fullSetProperty("provider", "text", "Provider: Network")
            droid.fullSetProperty("location", "text", lat + "; " + lng)
        
        if event == None:
            pass
        elif event['name'] == "click":
            id = event["data"]["id"]
            if id == "start":
                if isStarted == False:
                    droid.startLocating(60 * 1000, 50)
                    isStarted = True
                    droid.fullSetProperty("start", "text", "Stop Locating")
                else:
                    droid.stopLocating()
                    isStarted = False
                    droid.fullSetProperty("start", "text", "Start Locating")
            elif id == "exit":
                break

    droid.fullDismiss()

if __name__ == "__main__":
    main()
