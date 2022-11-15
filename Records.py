# -- User Table
# ---- UserID, Name, Password

# -- Person Table for General Public
# ---- PersonID, NIC, Name, Email, Password, Phone, Address, ImageID

# -- Birth Certificate
# ---- CertificateID, PersonID, DateOfBirth, MotherID, FatherID, GrandfatherID (Later Calculate Age)

# -- NIC Card
# ---- PersonID, NIC, Name, OtherName, DateOfBirth, BirthLocation, Job, Address

# -- Vital Stats
# ---- FamilyCount, FamilyCount, GenderCount, TheirJobs

# -- Marriage Certificate
# ---- PersonID1, PersonID2, (PersonID1 and PersonID2 as Primary key) DateOfMarriage

