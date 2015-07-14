import android

layout = """
<? xml version="1.0" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:orientation="vertical" android:layout_width="fill_parent"
android:layout_height="fill_parent" android:background="#ff000000">

<LinearLayout android:orientation="vertical" android:layout_width="fill_parent" android:layout_height="fill_parent">

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Spinner android:id="@+id/smsList" android:layout_width="fill_parent" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/getSmsText" android:text="Read SMS" android:layout_width="fill_parent" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/exit" android:text="Exit" android:layout_width="fill_parent" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:id="@+id/smsText" android:text="" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

</LinearLayout>
"""

droid = android.Android()
smsList=[]

def getSmsBody():
    item = smsList[int(droid.fullQueryDetail("smsList").result['selectedItemPosition'])]
    msgId = item['_id']
    text = droid.smsGetMessageById(msgId, ["body"]).result
    droid.fullSetProperty("smsText", "text", text['body'])

def loadMessages():
    global smsList
    smsList = droid.smsGetMessages(False, "inbox", ["_id", "address"]).result
    droid.fullSetList("smsList", smsList)

def main():
    droid.fullShow(layout)
    loadMessages()
    while True:
        event = droid.eventWait().result
        if event["name"] == "click":
            id = event["data"]["id"]
            if id == "getSmsText":
                getSmsBody()
            elif id == "exit":
                break

    droid.fullDismiss()

if __name__ == "__main__":
    main()
