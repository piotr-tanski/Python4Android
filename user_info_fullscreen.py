import android

layout="""
<? xml version="1.0" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:orientation="vertical" android:layout_width="fill_parent"
android:layout_height="fill_parent" android:background="#ff000000">

<ScrollView> 
<LinearLayout android:orientation="vertical" android:layout_width="fill_parent" android:layout_height="fill_parent">

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:text="First Name: " android:layout_width="wrap_content"
          android:layout_height="wrap_content"/>
<EditText android:id="@+id/name" android:width="100px" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:text="Last Name: " android:layout_width="wrap_content"
          android:layout_height="wrap_content"/>
<EditText android:id="@+id/surname" android:width="100px" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:text="Adres zamieszkania, numer domu / mieszkania" android:layout_width="wrap_content" android:layout_height="wrap_content" />
</LinearLayout>
<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<EditText android:id="@+id/address" android:width="300px" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
<EditText android:id="@+id/house" android:width="100px" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
<EditText android:id="@+id/apartNo" android:width="100px" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/getDate" android:text="Birthday" android:layout_width="fill_parent" android:layout_height="wrap_content"/>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<TextView android:text="Favorite color" android:layout_width="wrap_content" android:layout_height="wrap_content" />
</LinearLayout>
<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Spinner android:id="@+id/colors" android:layout_width="fill_parent" android:layout_height="wrap_content"/>
</LinearLayout>

<RadioGroup xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="fill_parent" android:layout_height="wrap_content" android:orientation="horizontal">
<RadioButton android:id="@+id/radio_kobieta" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Female" android:checked="true"/>
<RadioButton android:id="@+id/radio_mezczyzna" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="male"/>
</RadioGroup>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<CheckBox android:layout_height="wrap_content" android:id="@+id/checkBox1" android:layout_width="234dp" android:text="Reading books" android:checked="true"></CheckBox>
</LinearLayout>
<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<CheckBox android:layout_height="wrap_content" android:id="@+id/checkBox2" android:layout_width="234dp" android:text="C/C++ programming" android:checked="false"></CheckBox>
</LinearLayout>
<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<CheckBox android:layout_height="wrap_content" android:id="@+id/checkBox3" android:layout_width="234dp" android:text="Video games" android:checked="false"></CheckBox>
</LinearLayout>

<LinearLayout android:orientation="horizontal" android:layout_width="fill_parent" android:layout_height="wrap_content">
<Button android:id="@+id/summary" android:text="Summary" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
<Button android:id="@+id/exit" android:text="Exit" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</LinearLayout>

</LinearLayout>
</ScrollView>
</LinearLayout>
"""

droid = android.Android()

birthday=""
colors=["Red", "Blue", "Pink"]

def getBirthDate():
    global birthday
    droid.dialogCreateDatePicker(2014)
    droid.dialogShow()
    response = droid.dialogGetResponse()
    birthday = response.result
    droid.dialogDismiss()

def printSummary():
    name = droid.fullQueryDetail("name").result['text']
    surname = droid.fullQueryDetail("surname").result['text']
    address = droid.fullQueryDetail("address").result['text']
    house = droid.fullQueryDetail("house").result['text']
    apartNo = droid.fullQueryDetail("apartNo").result['text']
    color = colors[int(droid.fullQueryDetail("colors").result['selectedItemPosition'])]

    sex = "Female"
    isFemale = droid.fullQueryDetail("radio_kobieta").result['checked']
    if isFemale == "false":
        sex = "Male"

    hobby = ""
    if droid.fullQueryDetail("checkBox1").result['checked'] == "true":
        hobby += droid.fullQueryDetail("checkBox1").result['text'] + " "
    if droid.fullQueryDetail("checkBox2").result['checked'] == "true":
        hobby += droid.fullQueryDetail("checkBox2").result['text'] + " "
    if droid.fullQueryDetail("checkBox3").result['checked'] == "true":
        hobby += droid.fullQueryDetail("checkBox3").result['text'] + " "

    if birthday == "":
        droid.makeToast("%s %s\n%s\n%s %s / %s\nFavorite color: %s\nHobbies: %s" % (name, surname, sex, address, house, apartNo, color, hobby))
    else:    
        droid.makeToast("%s %s\n%s, %i-%i-%i\n%s %s / %s\nFavorite color: %s\nHobbies: %s" % (name, surname, sex, birthday['day'], birthday['month'], birthday['year'], address, house, apartNo, color, hobby))


def main():
    droid.fullShow(layout)
    droid.fullSetList("colors", colors)
    while True:
        event = droid.eventWait().result
        if event["name"] == "click":
            id = event["data"]["id"]
            if id == "getDate":
                getBirthDate()
            elif id == "summary":
                printSummary()
            elif id == "exit":
                break

    droid.fullDismiss()

if __name__ == "__main__":
    main()
