import sqlite3
from datetime import date
from tkinter import *
from tkinter import filedialog

from lib import FingerPrintScan

openFilePath = r"C:\Users\timni\PycharmProjects\Civil-Register\Data\Altered\SelectedData"

newFingerPrint = ""
labelFingerPrint = None

newName = ""
labelName = None

newStatus = ""
labelStatus = None

newDOB = ""
labelDOB = None

newAge = ""
lableAge = None

newJob = ""
labelJob = None

newAddress = ""
labelAddress = None

newBirthPlace = ""
labelBirthPlace = None
newMothersName = ""
labelMothersName = None
newFathersName = ""
labelFathersName = None
newGrandfathersName = ""
labelGrandfathersName = None

newNicNumber = ""
labelNicNumber = None
newOtherName = ""
labelOtherName = None

newFamilyCount = ""
labelFamilyCount = None
newSexCount = ""
labelSexCount = None
newMCount = ""
labelMCount = None
newFCount = ""
labelFCount = None
newJobVital = ""
labelJobVital = None

newMarriageDate = ""
labelMarriageDate = None
newMarriagePlace = ""
labelMarriagePlace = None
newHusbandName = ""
labelHusbandName = None
newWifeName = ""
labelWifeName = None


def updateData():
    global newName, labelName
    global newStatus, labelStatus
    global newDOB, labelDOB
    global newAge, labelAge
    global newJob, labelJob
    global newAddress, labelAddress
    global newFingerPrint, labelFingerPrint

    """ Read finger from sensor and return image """
    # Select File dialog box
    file = filedialog.askopenfilename(initialdir=openFilePath, title='Select File',
                                      filetypes=(('BMP', '*.bmp'), ('All Files', '*.*')))
    # print("Before file")
    print(file)
    newFileName = ""
    if file:
        filename, best_score, result = FingerPrintScan.matchfingerprint(file)
        print("After file")
        print(filename)
        print(best_score)
        print(result)
        imageNameLocal.set(filename)
        print("After set")
        print(imageNameLocal.get())

        # newIMG = PhotoImage(file=filename)
        # labelFingerPrint.configure(image=newIMG)
        # set newFileName to the file name
        newFileName = filename

    # From newFileName get the data  (2__F_Right_index_finger.BMP -> 2)
    id = newFileName.split("__")[0]

    # From person table in Database get the data
    # PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM person WHERE PersonID = ?", (id,))
    dataPerson = c.fetchone()
    print(dataPerson)

    # From user table in Database get the data
    # UserID, PersonID, Status, DOB, Age, Job, Address, FingerPrint
    c.execute("SELECT * FROM user WHERE UserID = ?", (id,))
    dataUser = c.fetchone()
    print(dataUser)

    # From NICCard table in Database get the data
    # ---- PersonID, NIC, Name, OtherName, DateOfBirth, BirthLocation, Job, Address
    c.execute("SELECT * FROM niccard WHERE PersonID = ?", (id,))
    dataNICCard = c.fetchone()
    print(dataNICCard)

    # From Marriage Certificate table in Database get the data
    # ---- PersonID1, PersonID2, (PersonID1 and PersonID2 as Primary key) DateOfMarriage
    c.execute("SELECT * FROM marriagecertificate WHERE PersonID1 = ? OR PersonID2 = ?", (id, id))
    dataMarriageCertificate = c.fetchone()
    print(dataMarriageCertificate)

    # From Birth Certificate table in Database get the data
    # ---- CertificateID, PersonID, DateOfBirth, MotherID, FatherID, GrandfatherID (Later Calculate Age)
    c.execute("SELECT * FROM birthcertificate WHERE PersonID = ?", (id,))
    dataBirthCertificate = c.fetchone()
    print(dataBirthCertificate)

    # From Vital Stats table in Database get the data
    # ---- PersonID, FamilyCount, MaleCount, FemaleCount, TheirJobs
    c.execute("SELECT * FROM vitalstats WHERE PersonID = ?", (id,))
    dataVitalStats = c.fetchone()
    print(dataVitalStats)

    newName = dataPerson[2]
    if dataMarriageCertificate is not None:
        newStatus = "Married"
    else:
        newStatus = "Not Married"
    newDOB = dataBirthCertificate[2]
    # Calculate Age today - DOB
    today = date.today()
    newAge = today.year - int(newDOB.split("/")[2])
    newJob = dataNICCard[5]
    newAddress = dataNICCard[7]

    if newName is not None:
        labelName.configure(text=newName)
    if newStatus is not None:
        labelStatus.configure(text=newStatus)
    if newDOB is not None:
        labelDOB.configure(text=newDOB)
    if newAge is not None:
        labelAge.configure(text=newAge)
    if newJob is not None:
        labelJob.configure(text=newJob)
    if newAddress is not None:
        labelAddress.configure(text=newAddress)


    global newBirthPlace, labelBirthPlace
    global newMothersName, labelMothersName
    global newFathersName, labelFathersName
    global newGrandfathersName, labelGrandfathersName
    global newNicNumber, labelNicNumber
    global newOtherName, labelOtherName
    global newJobVital, labelJobVital
    global newFamilyCount, labelFamilyCount
    global newSexCount, labelSexCount
    global newMCount, labelMCount
    global newFCount, labelFCount
    global newMarriageDate, labelMarriageDate
    global newMarriagePlace, labelMarriagePlace
    global newHusbandName, labelHusbandName
    global newWifeName, labelWifeName

    newMothersID = dataBirthCertificate[3]
    newFathersID = dataBirthCertificate[4]
    newGrandfathersID = dataBirthCertificate[5]

    # From person table in Database get the data
    # PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
    c.execute("SELECT * FROM person WHERE PersonID = ?", (newMothersID,))
    dataPerson = c.fetchone()
    print(dataPerson)
    newMothersName = dataPerson[2]

    c.execute("SELECT * FROM person WHERE PersonID = ?", (newFathersID,))
    dataPerson = c.fetchone()
    print(dataPerson)
    newFathersName = dataPerson[2]

    c.execute("SELECT * FROM person WHERE PersonID = ?", (newGrandfathersID,))
    dataPerson = c.fetchone()
    print(dataPerson)
    newGrandfathersName = dataPerson[2]

    newHusbandID = dataMarriageCertificate[0]
    newWifeID = dataMarriageCertificate[1]

    c.execute("SELECT * FROM person WHERE PersonID = ?", (newHusbandID,))
    dataPerson = c.fetchone()
    print(dataPerson)
    newHusbandName = dataPerson[2]

    c.execute("SELECT * FROM person WHERE PersonID = ?", (newWifeID,))
    dataPerson = c.fetchone()
    print(dataPerson)
    newWifeName = dataPerson[2]

    newBirthPlace = dataNICCard[5]
    newNicNumber = dataNICCard[1]
    newOtherName = dataNICCard[3]
    newFamilyCount = dataVitalStats[1]
    newSexCount = 0
    newMCount = dataVitalStats[4]
    newFCount = dataVitalStats[5]
    newMarriageDate = dataMarriageCertificate[2]
    newMarriagePlace = "Colombo"
    newJobVital = dataNICCard[5]

    if newBirthPlace is not None:
        labelBirthPlace.configure(text="Birth Place : " + newBirthPlace)
    if newMothersName is not None:
        labelMothersName.configure(text="Mother's Name : " + newMothersName)
    if newFathersName is not None:
        labelFathersName.configure(text="Father's Name : " + newFathersName)
    if newGrandfathersName is not None:
        labelGrandfathersName.configure(text="Grandfather's Name : " + newGrandfathersName)
    if newNicNumber is not None:
        labelNicNumber.configure(text="NIC Number : " + newNicNumber)
    if newOtherName is not None:
        labelOtherName.configure(text="Other Name : " + newOtherName)
    if newFamilyCount is not None:
        labelFamilyCount.configure(text="Family Count : " + newFamilyCount)
    if newMCount is not None:
        labelMCount.configure(text="M count : " + str(newMCount))
    if newFCount is not None:
        labelFCount.configure(text="F count : " + str(newFCount))
    if newMarriageDate is not None:
        labelMarriageDate.configure(text="Marriage Date : " + newMarriageDate)
    if newMarriagePlace is not None:
        labelMarriagePlace.configure(text="Marriage Place : " + newMarriagePlace)
    if newHusbandName is not None:
        labelHusbandName.configure(text="Husband Name : " + newHusbandName)
    if newWifeName is not None:
        labelWifeName.configure(text="Wife Name : " + newWifeName)


def logout():
    root.destroy()


if __name__ == '__main__':
    # Create Object and setup window
    root = Tk()
    root.title('Dashboard')

    # Create Variables for the widgets
    username = StringVar()
    imageNameLocal = StringVar()

    # Set the username and userPosition
    username.set("Username")


    # Create Frames
    top = Frame(root, width=1440, height=100, bg='white')
    top.pack(side=TOP)
    middle = Frame(root, width=1440, height=430, bg='white')
    middle.pack(side=TOP)
    bottom = Frame(root, width=1440, height=240, bg='white')
    bottom.pack(side=BOTTOM)

    """Top Section"""
    """Top Section"""
    """Top Section"""
    """Top Section"""
    """Top Section"""

    # Create Widgets
    # Image Widget for top frame in x=84 y=48 size=34x48
    img = PhotoImage(file='image 2.png')
    label = Label(top, image=img, width=34, height=48, bg='white')
    # resize image to fit label size
    label.image = img
    label.place(x=84, y=30)
    # Label Widget right of image in x=128 y=48 size=200x48
    label = Label(top, text='Civil Registration', font=('arial', 26), fg='black', bg='white')
    label.place(x=128, y=30)
    # Image Widget for top frame in x=1120 y=48 size=51x51
    img = PhotoImage(file='circle.png')
    label = Label(top, image=img, width=51, height=51, bg='white')
    # resize image to fit label size
    label.image = img
    label.place(x=1120, y=30)
    # Label Widget right of image in x=1184 y=48 size=200x48 show username
    label = Label(top, textvariable=username, font=('arial', 20), fg='black', bg='white')
    label.place(x=1184, y=30)
    # Link Widget for top frame in x=1248 y=48 size=200x48 for logout button and call logout function
    link = Label(top, text='Logout', font=('arial', 10), fg='blue', bg='white', cursor='hand2')
    link.place(x=1184, y=60)
    link.bind('<Button-1>', logout)

    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    # Image Widget for middle frame in x=84 y=48 size=276x334
    newFingerPrint = PhotoImage(file='image 1.png')
    # label = Label(middle, image=img, width=250, height=303, bg='white')
    labelFingerPrint = Label(middle, image=newFingerPrint, width=240, height=291, bg='white')
    labelFingerPrint.place(x=84, y=30)

    # Two button below image in x=84 y=374 size=276x48 call ReadFinger function
    btn = Button(middle, text='Capture', font=('arial', 15), width=10, height=1, bg='green', fg='white',
                 command=updateData, cursor='hand2')
    btn.place(x=84, y=348)
    # btn = Button(middle, text='Clear', font=('arial', 15), width=10, height=1, bg='green', fg='white', cursor='hand2',
    #              command=fun)
    # btn.place(x=220, y=348)
    btn = Button(middle, text='Clear', font=('arial', 15), width=10, height=1, bg='green', fg='white', cursor='hand2',
                 command=updateData)
    btn.place(x=220, y=348)

    # Label Right of image in x=420 y=48 size=200x48
    label = Label(middle, text='Basic Information', font=('arial', 20), fg='black', bg='white')
    label.place(x=420, y=30)
    # Label Right of image in x=420 y=96 size=200x48
    label = Label(middle, text='Name', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=96)

    # Label Right to Name to show name in x=600 y=96 size=200x48 show name
    labelName = Label(middle, text=newName, font=('arial', 15), fg='black', bg='white')
    labelName.place(x=600, y=96)

    # Label Right of image in x=420 y=144 size=200x48
    label = Label(middle, text='Status', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=144)
    # Label Right to Status to show status in x=600 y=144 size=200x48 show status
    labelStatus = Label(middle, text=newStatus, font=('arial', 15), fg='black', bg='white')
    labelStatus.place(x=600, y=144)
    # Label Right of image in x=420 y=192 size=200x48
    label = Label(middle, text='Date of Birth', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=192)
    # Label Right to Date of Birth to show dob in x=600 y=192 size=200x48 show dob
    labelDOB = Label(middle, text=newDOB, font=('arial', 15), fg='black', bg='white')
    labelDOB.place(x=600, y=192)
    # Label Right of image in x=420 y=240 size=200x48
    label = Label(middle, text='Age', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=240)
    # Label Right to Age to show age in x=600 y=240 size=200x48 show age
    labelAge = Label(middle, text=newAge, font=('arial', 15), fg='black', bg='white')
    labelAge.place(x=600, y=240)
    # Label Right of image in x=420 y=288 size=200x48
    label = Label(middle, text='Job', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=288)
    # Label Right to Job to show job in x=600 y=288 size=200x48 show job
    labelJob = Label(middle, text=newJob, font=('arial', 15), fg='black', bg='white')
    labelJob.place(x=600, y=288)
    # Label Right of image in x=420 y=336 size=200x48
    label = Label(middle, text='Address', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=336)
    # Label Right to Address to show address in x=600 y=336 size=200x48 show address
    labelAddress = Label(middle, text=newAddress, font=('arial', 15), fg='black', bg='white')
    labelAddress.place(x=600, y=336)

    font_size = 12

    """Bottom Render"""
    """Bottom Render"""
    """Bottom Render"""

    # 4 Section for bottom frame in x=84 y=48 size=276x334
    # Section 1
    # Section 1 Label in x=84 y=48 size=276x48 "Birth Certificate"
    label = Label(bottom, text='Birth Certificate', font=('arial', 14), fg='black', bg='white')
    label.place(x=84, y=0)
    # Birth Certificate (Link)
    # Birth Place :
    # Mother’s Name :
    # Father’s Name :
    # Grandfather’s Name :
    # Label below Birth Certificate in x=84 y=96 size=276x48 "Birth Place"
    labelBirthPlace = Label(bottom, text='Birth Place', font=('arial', font_size), fg='black', bg='white')
    labelBirthPlace.place(x=84, y=48)
    # Label below Birth Place in x=84 y=144 size=276x48 "Mother’s Name"
    labelMothersName = Label(bottom, text='Mother’s Name', font=('arial', font_size), fg='black', bg='white')
    labelMothersName.place(x=84, y=96)
    # Label below Mother’s Name in x=84 y=192 size=276x48 "Father’s Name"
    labelFathersName = Label(bottom, text='Father’s Name', font=('arial', font_size), fg='black', bg='white')
    labelFathersName.place(x=84, y=144)
    # Label below Father’s Name in x=84 y=240 size=276x48 "Grandfather’s Name"
    labelGrandfathersName = Label(bottom, text='Grandfather’s Name', font=('arial', font_size), fg='black', bg='white')
    labelGrandfathersName.place(x=84, y=192)
    # Section 2
    # Section 2 Label in x=420 y=48 size=276x48 "NIC"
    label = Label(bottom, text='NIC', font=('arial', 14), fg='black', bg='white')
    label.place(x=420, y=0)
    # NIC (Link)
    # NIC Number :
    # Other name :
    # Label below NIC in x=420 y=96 size=276x48 "NIC Number"
    labelNicNumber = Label(bottom, text='NIC Number', font=('arial', font_size), fg='black', bg='white')
    labelNicNumber.place(x=420, y=48)
    # Label below NIC Number in x=420 y=144 size=276x48 "Other name"
    labelOtherName = Label(bottom, text='Other name', font=('arial', font_size), fg='black', bg='white')
    labelOtherName.place(x=420, y=96)
    # Section 3
    # Section 3 Label in x=756 y=48 size=276x48 "Vital Stats"
    label = Label(bottom, text='Vital Stats', font=('arial', 14), fg='black', bg='white')
    label.place(x=756, y=0)
    # Vital Stats (Link)
    # Family Count :
    # Sex Count :
    ## -- M Count : -- F Count :
    # Jobs :
    # person name - job
    # Label below Vital Stats in x=756 y=96 size=276x48 "Family Count"
    labelFamilyCount = Label(bottom, text='Family Count', font=('arial', font_size), fg='black', bg='white')
    labelFamilyCount.place(x=756, y=48)
    # Label below Family Count in x=756 y=144 size=276x48 "Sex Count"
    # labelFamilyCount = Label(bottom, text='Sex Count', font=('arial', font_size), fg='black', bg='white')
    # labelFamilyCount.place(x=756, y=96)
    # Label below Sexuality Count in x=756 y=192 size=276x48 "M count"
    labelMCount = Label(bottom, text='Mal Count', font=('arial', font_size), fg='black', bg='white')
    labelMCount.place(x=756, y=96)
    # Label Right to M Count in x=756 y=240 size=276x48 "F Count"
    labelFCount = Label(bottom, text='Female Count', font=('arial', font_size), fg='black', bg='white')
    labelFCount.place(x=756, y=144)

    # Section 4
    # Section 4 Label in x=1092 y=48 size=276x48 "Marriage Certificate"
    label = Label(bottom, text='Marriage Certificate', font=('arial', 14), fg='black', bg='white')
    label.place(x=1092, y=0)
    # Marriage Certificate (Link)
    # Marriage Date :
    # Marriage Place :
    # Husband Name :
    # Wife Name :
    # Label below Marriage Certificate in x=1092 y=96 size=276x48 "Marriage Date"
    labelMarriageDate = Label(bottom, text='Marriage Date', font=('arial', font_size), fg='black', bg='white')
    labelMarriageDate.place(x=1092, y=48)
    # Label below Marriage Date in x=1092 y=144 size=276x48 "Marriage Place"'
    labelMarriagePlace = Label(bottom, text='Marriage Place', font=('arial', font_size), fg='black', bg='white')
    labelMarriagePlace.place(x=1092, y=96)
    # Label below Marriage Place in x=1092 y=192 size=276x48 "Husband Name"
    labelHusbandName = Label(bottom, text='Husband Name', font=('arial', font_size), fg='black', bg='white')
    labelHusbandName.place(x=1092, y=144)
    # Label below Husband Name in x=1092 y=240 size=276x48 "Wife Name"
    labelWifeName = Label(bottom, text='Wife Name', font=('arial', font_size), fg='black', bg='white')
    labelWifeName.place(x=1092, y=192)

    root.mainloop()
