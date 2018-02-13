#sqlfunction.py

import sqlite3

# creating the connection with the database
conn = sqlite3.connect("PersonalDetailsTable.db")
c = conn.cursor()


'''Table Creation'''

def createPersonalTable():
    c.execute("CREATE TABLE IF NOT EXISTS "
              "PersonalTable(StudentID INTEGER PRIMARY KEY AUTOINCREMENT,"
              "Username TEXT,"
              "Password TEXT,"
              "FirstName TEXT,"
              "LastName TEXT)")


def createWordTable():
    c.execute("CREATE TABLE IF NOT EXISTS WordTable("
              "WordID INTEGER PRIMARY KEY AUTOINCREMENT,"
              "TopicID INTEGER,"
              "NativeWord TEXT ,"
              "ForeignWord TEXT )")


def createExerciseTable():
    c.execute("CREATE TABLE IF NOT EXISTS ExerciseTable("
              "ExerciseID INTEGER PRIMARY KEY AUTOINCREMENT,"
              "StudentID INTEGER,"
              "ScoreOnExercise INTEGER,"
              "FOREIGN KEY(StudentID) REFERENCES PersonalTable(StudentID))")


def createWordBankTable():
    c.execute("CREATE TABLE IF NOT EXISTS WordBankTable(WordBankID INTEGER PRIMARY KEY AUTOINCREMENT,"
              "StudentID INTEGER,"
              "WordID INTEGER,"
              "TimesCorrect INTEGER,"
              "Time INTEGER,"
              "FOREIGN KEY(WordID) REFERENCES WordTable(WordID),"
              "FOREIGN KEY(StudentID) REFERENCES PersonalTable(StudentID))")



def create_tables():
    """creates table if the dont already exist"""
    createPersonalTable()
    createExerciseTable()
    createWordTable()
    createWordBankTable()
    conn.execute('pragma foreign_keys = 1')
    conn.commit()


'''Enter information into table'''

def enterExerciseTable(studentid,score):
    c.execute("INSERT INTO ExerciseTable(StudentID,ScoreOnExercise) VALUES(?,?)",
              (studentid,score))
    conn.commit()


def enterPersonalTable(Username,Password,Firstname,Lastname):
    c.execute("INSERT INTO PersonalTable(Username,Password,Firstname,Lastname) VALUES (?,?,?,?)",
              (Username,Password,Firstname,Lastname))
    conn.commit()


def enterWordBankTable(studentid,wordid,timescorrect,time):
    c.execute("INSERT INTO WordBankTable(StudentID,WordID,TimesCorrect,Time) VALUES (?,?,?,?)",
              (studentid,wordid,timescorrect,time))
    conn.commit()


def enterWordTable(topicid,native,foreign):
    c.execute("INSERT INTO WordTable(TopicID,NativeWord,ForeignWord) VALUES (?,?,?)",(topicid,native,foreign))
    conn.commit()


'''SELECT'''

def usernametoid(username):
    """gets username and finds the Student that corresponds"""
    c.execute("SELECT StudentID FROM PersonalTable WHERE username=?", (username,))
    return c.fetchone()[0]


def nativetoid(native):
    """gets the native word from Word Table and return the word ID"""
    c.execute("SELECT WordID FROM WordTable WHERE NativeWord=?",(native,))
    return c.fetchone()[0]

def wordidtonative(wordid):
    """gets the native word from the WordTable using the wordID"""
    c.execute("SELECT NativeWord FROM WordTable WHERE WordID=?",(wordid,))
    return c.fetchone()[0]

def rowidtoWordid(rowid):
    """gets the wordid from the word bank table using the rowid"""
    c.execute("SELECT WordID FROM WordBankTable WHERE rowid=?",(rowid,))
    return c.fetchone()[0]



def foreigntoid(foreign):
    """gets the WordID using the Word table and a foreign word"""
    # the try and accept clause happens because for some reason
    #wordID 72 would never work

    foreign = str(foreign)+ "\n"
    c.execute("SELECT WordID FROM WordTable WHERE ForeignWord=?",(foreign,))
    return c.fetchone()[0]

def nativetoforeign(native):
    """"puts in the native word and returns the foreign word using thr WordTable"""
    c.execute("SELECT ForeignWord FROM WordTable WHERE NativeWord=?",(native,))
    data = str(c.fetchone()[0])
    data = data[0:len(data)-1]
    return data

def foreigntonative(foreign):
    """uses the word table map foreign words to the native words"""
    foreign = str(foreign) + "\n"
    c.execute("SELECT NativeWord FROM WordTable WHERE ForeignWord=?",(foreign,))
    data = str(c.fetchone()[0])
    data = data[0:len(data)]
    return data


def knowness(studentid,wordid):
    """returns values used for calculating knowness"""
    c.execute("SELECT TimesCorrect,Time FROM WordBankTable WHERE StudentID=? AND WordID=?",(studentid,wordid))
    return c.fetchall()


def findscore(username):
    """"returns all the scores on the exercises for a specififc  user"""
    data = usernametoid(username)
    print(data)
    c.execute("SELECT ScoreOnExercise FROM ExerciseTable WHERE StudentID=?", data)
    scores =  c.fetchall()
    return scores

def usernameUnique(username):
    """checks if the username is unique to the PersonalTable"""
    username = str(username),
    c.execute('SELECT * FROM PersonalTable WHERE Username=?', username)
    data =  c.fetchall()
    if data == []:
        return True
    else:
        return False


def password(username):
    """fetches the password associated with the username"""
    try:
        username = str(username),
        c.execute("SELECT Password From PersonalTable WHERE Username=?", username)
        data = c.fetchone()
        return data[0]
    except TypeError:
        return ""



"""UPDATE"""

def updateknowness(timescorrect,time,studentid,wordid):
    """changes the times_correct and time entries of a students word """
    c.execute("UPDATE WordBankTable SET TimesCorrect=?,Time=? WHERE StudentID=? AND WordID = ?",
              (timescorrect,time,studentid,wordid))
    conn.commit()

"""Delete"""

def deleteStudentid(value):
    """"deletes student record from the personal details table"""
    c.execute("DELETE FROM PersonalTable WHERE StudentID=?",(value,))
    conn.commit()

def delete_wordbank_record(studentid,wordid):
    """"deletes a record from the workBankTable"""
    c.execute("DELETE FROM WordBankTable WHERE StudentID=? AND WordID=?",(studentid,wordid))
    conn.commit()


"""Other"""



def csvToArray(file):
    """takes a file and turns it into an array"""
    array = []
    f = open(file, "r")
    lineout = "has to be filled"
    # if the line is empty its at the end of the document
    while lineout != "":
        lineout = f.readline()
        array.append(lineout.split(","))
    return array


def noOfRecords():
    """counts the number of words in the WordTable and returns the integer"""
    c.execute("SELECT rowid FROM WordTable")
    return len(c.fetchall())

def wordbankids(studentid):
    """fetches all the word bank ids for a specific user in the WordBank Table"""
    c.execute("SELECT rowid FROM WordBankTable WHERE StudentID=?", (studentid,))
    return c.fetchall()

def rowidtoNative(rowid):
    """uses the row id in the word table to fetch a foreign word"""
    c.execute("SELECT NativeWord FROM WordTable WHERE rowid=?",(rowid,))
    return c.fetchone()[0]


def inTableandBank(wordid):
    """checks to see if a word is in both the wordTable and thw WordBankTable"""
    c.execute("SELECT WordID FROM WordBankTable WHERE WordID=?",(wordid,))
    data = c.fetchall()
    if data == [] :
        return False
    else:
        return True


def get_topic_words(topic_words):
    """returns all the words from WordTable that have a specific topic id"""
    c.execute("SELECT NativeWord FROM WordTable WHERE TopicID=?", (topic_words,))
    return c.fetchall()

def get_knowness(studentid,wordid):
    """fetches the variables to compute the knowness from the WordBank table"""
    c.execute("SELECT Time,TimesCorrect FROM WordBankTable WHERE StudentID=? AND WordID=?",(studentid,wordid))
    data = c.fetchall()
    time = data[0][0]
    times_correct = data[0][1]
    return time,times_correct

def bankid_knowness(bankid):
    """uses the bank id to calculate the knowness of a word"""
    c.execute("SELECT Time,TimesCorrect FROM WordBankTable WHERE WordBankID=?",(bankid,))
    return c.fetchone()

def bankid_wordid(bankid):
    """uses the word bank table to find what the word id is for any given WordBank id"""
    c.execute("SELECT WordID FROM WordBankTable WHERE WordBankID=?",(bankid,))
    try:
        return c.fetchone()[0]

    except TypeError:
        return "0"

def user_exercises(userid):
    """returns an array of the scores for each exercise"""
    c.execute("SELECT ScoreOnExercise FROM ExerciseTable WHERE StudentID=?",(userid,))
    data = c.fetchall()
    return [data[i][0] for i in range(len(data))]

def exercise_completed(studentid):
    """counts the amount of record for a given StudentID are given in the Exercise table"""
    c.execute("SELECT * FROM ExerciseTable WHERE StudentID=?",(studentid,))
    return len(c.fetchall())

def get_name(username):
    """fetches the names of a person dependant upon their username"""
    c.execute("SELECT FirstName,LastName FROM PersonalTable WHERE Username=?",(username,))
    return c.fetchone()


