import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=plq76207;PWD=ZmeqbSx0vyVOuxoG;","","")
print("connection successfully")


sql="""CREATE TABLE login (
    Name varchar(255),
    Email varchar(255),
    Password varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)

sql="""CREATE TABLE Customerdetails (
    Name varchar(255),
    ShopName varchar(255),
    Location varchar(255),
    Address varchar(255),
    City varchar(255),
    State varchar(255),
    MobileNumber varchar(255),
    Quantity varchar(255))"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)