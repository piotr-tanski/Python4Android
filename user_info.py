import android

droid = android.Android()

name=""
surname=""
address=""
birthday=""
sex=""
colors=[]
action=""

def getName():
    global name
    res = droid.dialogGetInput("Czesc!", "Jak masz na imie?") 
    name = res.result

def getSurname():
    global surname
    res = droid.dialogGetInput("Czesc!", "... a na nazwisko?")
    surname = res.result
    
def getAddress():
    global address
    res = droid.dialogGetInput("Czesc!", "Gdzie mieszkasz?")
    address = res.result
    
def getSex():
    global sex
    options=["kobieta", "mezczyzna"]
    droid.dialogCreateAlert("Jakies plci jestes")
    droid.dialogSetSingleChoiceItems(options)
    droid.dialogSetPositiveButtonText("OK")
    droid.dialogSetNegativeButtonText("Anuluj")
    droid.dialogShow()
    result = droid.dialogGetResponse().result
    wynik = droid.dialogGetSelectedItems().result
    
    sex = options[wynik[0]]
    
def getBirthday():
    global birthday
    droid.dialogCreateDatePicker(2014)
    droid.dialogShow()
    response = droid.dialogGetResponse()
    birthday = response.result
    droid.dialogDismiss()
    
def getColors():
    global colors
    options = ["czerwony", "niebieski", "rozowy"]
    droid.dialogCreateAlert("Ulubione kolory")
    droid.dialogSetMultiChoiceItems(options)
    droid.dialogSetPositiveButtonText("OK")
    droid.dialogSetNegativeBUttonText("Anuluj")
    droid.dialogShow()
    result = droid.dialogGetResponse().result
    for i in droid.dialogGetSelectedItems().result:
        colors.append(options[i])
    
def getAction():
    global action
    options = ["Jazda na rowerze", "Programowanie w C", "Nauka"]
    droid.dialogCreateAlert("Hobby")
    droid.dialogSetSingleChoiceItems(options)
    droid.dialogSetPositiveButtonText("OK")
    droid.dialogSetNegativeButtonText("Anuluj")
    droid.dialogShow()
    result = droid.dialogGetResponse().result
    wynik = droid.dialogGetSelectedItems().result
    
    action = options[wynik[0]]
    
def main():
    getName()
    getSurname()
    getAddress()
    getSex()
    getBirthday()
    getColors()
    getAction()
    
    color=""
    for i in colors:
        color += i + " ";

    droid.makeToast("%s %s\n%s\n%s\n%i-%i-%i\nUlubione kolory: %s\nHobby: %s" % (name, surname, address, sex, birthday['day'], birthday['month'], birthday['year'], color, action))

if __name__ == "__main__":
    main()
