import csv

from numpy import append
student = []

with open('./python/Student_Data.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # print(line)
        student.append(line)

# print(student)

sql = []

cmd = """CREATE TABLE Student(
        Sr_No int(20), 
        PRN int(7) PRIMARY KEY,
        First_Name varchar(255), 
        Middle_Name varchar(255),
        Last_Name varchar(255));
)"""

insert_query = """
INSERT INTO Student(
    Sr_No,
    PRN,
    First_Name,
    Middle_Name,
    Last_Name
) 
""" 


values = """
"""

single_col_query = """
"""

# print(student)
for _ in student:
    # print(_[0], _[1], _[4], _[5], _[3])
    # values = values + '('+ _[0] + ', ' + _[1] + ', \'' + _[4] + '\', \'' + _[5] + '\', \'' + _[3] + '\'),' 
    single_col_query = single_col_query + "WHEN " + _[1] + ' THEN \'' + _[1] + '@gcoej.ac.in\'\n' 
    # print(values)

print(single_col_query[:])

'''
INSERT INTO Student(
    Sr_No,
    PRN,
    First_Name,
    Middle_Name,
    Last_Name
)
VALUES
(1, 2041001, 'VAIBHAV', 'SURESH', 'AGHAV'),(2, 2041002, 'PRATIK', 'PRAMOD', 'BAGADE'),(3, 2041003, 'ASIT', 'PRAMOD', 'BAKDE'),(4, 2041004, 'DRAKSHI', 'ANILRAO', 'BA'LPANDE'),(5, 2041005, 'SHRUSHTI', 'JAYANT', 'BANSOD'),(6, 2041006, 'MANISHA', 'RAMKISHAN', 'BHANDE'),(7, 2041007, 'DIKSHA', 'SHALIK', 'BHANGALE'),(8, 2041008, 'SANJANA', 'AJAY', 'BHARAMBE'),(9, 2041009, 'SHAMUVEL', 'GURAV', 'BHARGAV'),(10, 2041010, NIKITA', 'SANJU', 'BHOI'),(11, 2041011, 'RUPAL', 'KISHOR', 'BHURE'),(12, 2041012, 'MAYUR', 'RAMESH', 'BODHARE'),(13, 2041013, 'PRATIK', 'GANPAT', 'BORADE'),(14, 2041014, 'AJINKYA', 'BHAUSAHEB', 'BORATE'),(15, 2041015, 'DIPAK', 'DILIP', 'CHAHAKAR'),(16, 2041016, 'BHUSHAN', 'RAJU', 'CHANORE'),(17, 2041017, 'TEJAS', 'KASHINATH', 'CHAUDHARI'),(18, 2041018, 'ASHWINI', 'NARENDRA', 'DANGE'),(19, 2041019, 'YASH', 'RAM', 'DESHMUKH'),(20, 2041020, 'TANMAY', 'NARESH', 'DHANVIJAY'),(21, 2041021, 'KHUSHAL', 'RUPESH', 'DHUMAL'),(22, 2041022, 'HITESH', 'ABHIJIT', 'DONGE'),(23, 2041024, 'ABHISHEK', 'VINAYAK', 'GAWANDE'),(24, 2041025, 'AJAY', 'SATISH', 'GHODKE'),(25, 2041026, 'AKANKSHA', 'ATMARAM', 'GOSAVI'),(26, 2041028, 'VISHWJEET', 'RAJESHWAR', 'JADHAV'),(27, 2041029, 'YASH', 'VILAS', 'JADHAV'),(28, 2041030, 'MRUNAL', 'BHUMESHWAR', 'JAGNADE'),(29, 2041031, 'TEJAS', 'PRAKASH', 'KADBE'),(30, 2041032, 'SIDDHI', 'NARHARI', 'KAKPURE'),(31, 2041033, 'GAYATRI', 'MANOHAR', 'KOLATE'),(32, 2041034, 'PRANAV', 'GAJANAN', 'LANDE'),(33, 2041035, 'SHRUTI',
'ONKAR', 'MESHRAM'),(34, 2041036, 'NARSING', 'VYANKATRAO', 'NANDGAVE'),(35, 2041037, 'PRASHANT', 'PARSHURAM', 'NAWALE'),(36, 2041038, 'SANKET', 'GANESH', 'PADUL'),(37, 2041039, 'NIKITA', 'DNYANESHWAR', 'PATIL'),(38, 2041040, 'POOJA', 'MADHUKAR', 'PATIL'),(39, 2041041, 'PRUTHVIRAJ', 'SUBHASH', 'PATIL'),(40, 2041042, 'ROSHANI', 'SANJAY', 'PATIL'),(41, 2041043, 'VAISHNAVI', 'GAJANAN', 'PATIL'),(42, 2041044, 'VARAD', 'RAJENDRA', 'PATIL'),(43, 2041045, 'RUSHIKESH', 'MILIND', 'PAWAR'),(44, 2041046, 'VAIBHAV', 'PITAMBAR', 'PAWAR'),(45, 2041047, 'YASH', 'GANESHKUMAR', 'PETKAR'),(46, 2041048, 'DIPAK', 'UMESH', 'PIMPARE'),(47, 2041049, 'PRERNA', 'SHIVAJI', 'GITE'),(48, 2041050, 'ABHISHEK', 'MAHENDRASING', 'RAJPUT'),(49, 2041051, 'SAKSHI', 'PRADIP', 'RATHOD'),(50, 2041052, 'YASH', 'BABANRAO', 'RAUT'),(51, 2041053, 'RITIK', 'DAYANAND', 'MANDAL'),(52, 2041054, 'ROHIT', 'MAROTI', 'RAMTEKE'),(53, 2041055, 'RUTUJA', 'SURESH', 'RUBDE'),(54, 2041056, 'SANGRAM', 'BABAN', 'BHISE'),(55, 2041057, 'SAPANA', '', 'KHARCHE'),(56, 2041058, 'AKSHAY', 'SANJAY', 'SATAV'),(57, 2041059, 'RISHABHRAJ', 'VIJAYKUMAR', 'SHARMA'),(58, 2041060, 'AMOL', 'SURESH', 'SHINDE'),(59, 2041061, 'SAITEJ', 'GORAKSHA', 'SHINDE'),(60, 2041062, 'VILAS', 'MAHENDRA', 'SONJE'),(61, 2041064, 'VISHAKHA', 'SUNIL', 'PATIL'),(62, 2041065, 'GAURAV', 'DNYANESHWAR', 'WANI'),(63, 2041066, 'DEEPAK', 'ABHAYNARAYAN', 'YADAV'),(64, 2142101, 'KALYANI', 'RAVINDRA', 'PATIL'),(65, 2142102, 'SAKSHI', 'SUNIL', 'PATIL'),(66, 2142201, 'ADITYA', 'DIGAMBAR', 'BAMBARDE'),(67, 2142202, 'VAISHNAVI', 'ANIL KUMAR', 'BAURASI'),(68, 2142203, 'DIPTI', 'DEORAO', 'BHOYAR'),(69, 2142204, 'GOVINDRAJ', 'HARIHARRAO', 'DESHPANDE'),(70, 2142205, 'KESHAV', 'MUNJAJI', 'KADAM'),(71, 2142206, 'VAISHNAVI', 'RAJENDRA', 'NARKHEDE'),(72, 2142207, 'SHRADDHA', 'DEVIDAS', 'NAVGHARE'),(73, 2142208, 'VISHAL', 'PUNDLIK', 'PAWAR'),(74, 2142209, 'NIKITA', 'ANIL', 'SHIMPI');
'''

# Inserting Multiple values in the Single-Column 
# NOTE: step-1 ALTER TABLE <table-name> MODIFY <id> int NOT NULL AUTO_INCREMENT;
# NOTE: step-1 ALTER TABLE student MODIFY id int NOT NULL AUTO_INCREMENT;
# NOTE: step-2 
# INSERT INTO temp ( <column-name> ) 
# select 'hello'
# union 
# select 'world'


# INSERT INTO student(First_Name) VALUES ('Hello'), ('World');

# NOTE: PASSWORD QUERY -->
'''
UPDATE student
SET Password = CASE PRN
WHEN 2041001 THEN '2041001_VAIBHAV'
WHEN 2041002 THEN '2041002_PRATIK'
WHEN 2041003 THEN '2041003_ASIT'
WHEN 2041004 THEN '2041004_DRAKSHI'
WHEN 2041005 THEN '2041005_SHRUSHTI'
WHEN 2041006 THEN '2041006_MANISHA'
WHEN 2041007 THEN '2041007_DIKSHA'
WHEN 2041008 THEN '2041008_SANJANA'
WHEN 2041009 THEN '2041009_SHAMUVEL'
WHEN 2041010 THEN '2041010_NIKITA'
WHEN 2041011 THEN '2041011_RUPAL'
WHEN 2041012 THEN '2041012_MAYUR'
WHEN 2041013 THEN '2041013_PRATIK'
WHEN 2041014 THEN '2041014_AJINKYA'
WHEN 2041015 THEN '2041015_DIPAK'
WHEN 2041016 THEN '2041016_BHUSHAN'
WHEN 2041017 THEN '2041017_TEJAS'
WHEN 2041018 THEN '2041018_ASHWINI'
WHEN 2041019 THEN '2041019_YASH'
WHEN 2041020 THEN '2041020_TANMAY'
WHEN 2041021 THEN '2041021_KHUSHAL'
WHEN 2041022 THEN '2041022_HITESH'
WHEN 2041024 THEN '2041024_ABHISHEK'
WHEN 2041025 THEN '2041025_AJAY'
WHEN 2041026 THEN '2041026_AKANKSHA'
WHEN 2041028 THEN '2041028_VISHWJEET'
WHEN 2041029 THEN '2041029_YASH'
WHEN 2041030 THEN '2041030_MRUNAL'
WHEN 2041031 THEN '2041031_TEJAS'
WHEN 2041032 THEN '2041032_SIDDHI'
WHEN 2041033 THEN '2041033_GAYATRI'
WHEN 2041034 THEN '2041034_PRANAV'
WHEN 2041035 THEN '2041035_SHRUTI'
WHEN 2041036 THEN '2041036_NARSING'
WHEN 2041037 THEN '2041037_PRASHANT'
WHEN 2041038 THEN '2041038_SANKET'
WHEN 2041039 THEN '2041039_NIKITA'
WHEN 2041040 THEN '2041040_POOJA'
WHEN 2041041 THEN '2041041_PRUTHVIRAJ'
WHEN 2041042 THEN '2041042_ROSHANI'
WHEN 2041043 THEN '2041043_VAISHNAVI'
WHEN 2041044 THEN '2041044_VARAD'
WHEN 2041045 THEN '2041045_RUSHIKESH'
WHEN 2041046 THEN '2041046_VAIBHAV'
WHEN 2041047 THEN '2041047_YASH'
WHEN 2041048 THEN '2041048_DIPAK'
WHEN 2041049 THEN '2041049_PRERNA'
WHEN 2041050 THEN '2041050_ABHISHEK'
WHEN 2041051 THEN '2041051_SAKSHI'
WHEN 2041052 THEN '2041052_YASH'
WHEN 2041053 THEN '2041053_RITIK'
WHEN 2041054 THEN '2041054_ROHIT'
WHEN 2041055 THEN '2041055_RUTUJA'
WHEN 2041056 THEN '2041056_BABAN'
WHEN 2041057 THEN '2041057_'
WHEN 2041058 THEN '2041058_AKSHAY'
WHEN 2041059 THEN '2041059_RISHABHRAJ'
WHEN 2041060 THEN '2041060_AMOL'
WHEN 2041061 THEN '2041061_SAITEJ'
WHEN 2041062 THEN '2041062_VILAS'
WHEN 2041064 THEN '2041064_VISHAKHA'
WHEN 2041065 THEN '2041065_GAURAV'
WHEN 2041066 THEN '2041066_DEEPAK'
WHEN 2142101 THEN '2142101_KALYANI'
WHEN 2142102 THEN '2142102_SAKSHI'
WHEN 2142201 THEN '2142201_ADITYA'
WHEN 2142202 THEN '2142202_VAISHNAVI'
WHEN 2142203 THEN '2142203_DIPTI'
WHEN 2142204 THEN '2142204_GOVINDRAJ'
WHEN 2142205 THEN '2142205_KESHAV'
WHEN 2142206 THEN '2142206_VAISHNAVI'
WHEN 2142207 THEN '2142207_SHRADDHA'
WHEN 2142208 THEN '2142208_VISHAL'
WHEN 2142209 THEN '2142209_NIKITA'
END
WHERE PRN BETWEEN 2041001 AND 2041066;
'''

# NOTE: PASSWORD QUERY -->
'''
UPDATE student
SET E_mail = CASE PRN
WHEN 2041001 THEN '2041001@gcoej.ac.in'
WHEN 2041002 THEN '2041002@gcoej.ac.in'
WHEN 2041003 THEN '2041003@gcoej.ac.in'
WHEN 2041004 THEN '2041004@gcoej.ac.in'
WHEN 2041005 THEN '2041005@gcoej.ac.in'
WHEN 2041006 THEN '2041006@gcoej.ac.in'
WHEN 2041007 THEN '2041007@gcoej.ac.in'
WHEN 2041008 THEN '2041008@gcoej.ac.in'
WHEN 2041009 THEN '2041009@gcoej.ac.in'
WHEN 2041010 THEN '2041010@gcoej.ac.in'
WHEN 2041011 THEN '2041011@gcoej.ac.in'
WHEN 2041012 THEN '2041012@gcoej.ac.in'
WHEN 2041013 THEN '2041013@gcoej.ac.in'
WHEN 2041014 THEN '2041014@gcoej.ac.in'
WHEN 2041015 THEN '2041015@gcoej.ac.in'
WHEN 2041016 THEN '2041016@gcoej.ac.in'
WHEN 2041017 THEN '2041017@gcoej.ac.in'
WHEN 2041018 THEN '2041018@gcoej.ac.in'
WHEN 2041019 THEN '2041019@gcoej.ac.in'
WHEN 2041020 THEN '2041020@gcoej.ac.in'
WHEN 2041021 THEN '2041021@gcoej.ac.in'
WHEN 2041022 THEN '2041022@gcoej.ac.in'
WHEN 2041024 THEN '2041024@gcoej.ac.in'
WHEN 2041025 THEN '2041025@gcoej.ac.in'
WHEN 2041026 THEN '2041026@gcoej.ac.in'
WHEN 2041028 THEN '2041028@gcoej.ac.in'
WHEN 2041029 THEN '2041029@gcoej.ac.in'
WHEN 2041030 THEN '2041030@gcoej.ac.in'
WHEN 2041031 THEN '2041031@gcoej.ac.in'
WHEN 2041032 THEN '2041032@gcoej.ac.in'
WHEN 2041033 THEN '2041033@gcoej.ac.in'
WHEN 2041034 THEN '2041034@gcoej.ac.in'
WHEN 2041035 THEN '2041035@gcoej.ac.in'
WHEN 2041036 THEN '2041036@gcoej.ac.in'
WHEN 2041037 THEN '2041037@gcoej.ac.in'
WHEN 2041038 THEN '2041038@gcoej.ac.in'
WHEN 2041039 THEN '2041039@gcoej.ac.in'
WHEN 2041040 THEN '2041040@gcoej.ac.in'
WHEN 2041041 THEN '2041041@gcoej.ac.in'
WHEN 2041042 THEN '2041042@gcoej.ac.in'
WHEN 2041043 THEN '2041043@gcoej.ac.in'
WHEN 2041044 THEN '2041044@gcoej.ac.in'
WHEN 2041045 THEN '2041045@gcoej.ac.in'
WHEN 2041046 THEN '2041046@gcoej.ac.in'
WHEN 2041047 THEN '2041047@gcoej.ac.in'
WHEN 2041048 THEN '2041048@gcoej.ac.in'
WHEN 2041049 THEN '2041049@gcoej.ac.in'
WHEN 2041050 THEN '2041050@gcoej.ac.in'
WHEN 2041051 THEN '2041051@gcoej.ac.in'
WHEN 2041052 THEN '2041052@gcoej.ac.in'
WHEN 2041053 THEN '2041053@gcoej.ac.in'
WHEN 2041054 THEN '2041054@gcoej.ac.in'
WHEN 2041055 THEN '2041055@gcoej.ac.in'
WHEN 2041056 THEN '2041056@gcoej.ac.in'
WHEN 2041057 THEN '2041057@gcoej.ac.in'
WHEN 2041058 THEN '2041058@gcoej.ac.in'
WHEN 2041059 THEN '2041059@gcoej.ac.in'
WHEN 2041060 THEN '2041060@gcoej.ac.in'
WHEN 2041061 THEN '2041061@gcoej.ac.in'
WHEN 2041062 THEN '2041062@gcoej.ac.in'
WHEN 2041064 THEN '2041064@gcoej.ac.in'
WHEN 2041065 THEN '2041065@gcoej.ac.in'
WHEN 2041066 THEN '2041066@gcoej.ac.in'
WHEN 2142101 THEN '2142101@gcoej.ac.in'
WHEN 2142102 THEN '2142102@gcoej.ac.in'
WHEN 2142201 THEN '2142201@gcoej.ac.in'
WHEN 2142202 THEN '2142202@gcoej.ac.in'
WHEN 2142203 THEN '2142203@gcoej.ac.in'
WHEN 2142204 THEN '2142204@gcoej.ac.in'
WHEN 2142205 THEN '2142205@gcoej.ac.in'
WHEN 2142206 THEN '2142206@gcoej.ac.in'
WHEN 2142207 THEN '2142207@gcoej.ac.in'
WHEN 2142208 THEN '2142208@gcoej.ac.in'
WHEN 2142209 THEN '2142209@gcoej.ac.in'
END
WHERE PRN BETWEEN 2041001 AND 2142209;
'''