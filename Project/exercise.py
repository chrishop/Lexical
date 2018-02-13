import random,sqlfunction,pygame,time,math

pygame.init()




class Question:
    def __init__(self):
        "exercise_type as in continue,refesh or topic specific"
        self.questionWords = []
        self.current_time = time.time()
        self.score = []




    def calculate_knowness(self,studentid,wordid):
        """uses the times correct and time values in the database
        to product a value to calculate the chance of them knowing the word"""
        knowness_vals = sqlfunction.get_knowness(studentid,wordid)
        # subtract the database unix from the actual unix time value
        time = self.current_time - knowness_vals[0]
        # the equation to calculate knowness by
        # the constant "62324" means that the words will have a knowness value of 0.5 in 12 hours
        #  (if the times correct is 1)
        knowness = math.e**(-time/62324*knowness_vals[1])

        # (to examiner)if you want to be able to test the refresher question text quicker without having to wait
        # unhash the line below it will mean you should be able to do a refresher exercise within 5 mins
        # (assuming that you've already done a couple of exercises)

        # knowness = math.e ** (-time / 432 * knowness_vals[1])

        return knowness





class Buttons(Question):
    """questions which concern a button
    (i was going to add support for texr but never got round to it)"""
    def __init__(self):
        """initialises all the variables including the ones belonging
        to the question class"""
        super(Buttons,self).__init__()
        # pick a random index to be the position of the correct answer
        self.correct_index = random.randint(0, 3)
        # a variable representing the amount of times a valid word has been added to the list
        self.passed = 0
        # the trigger if a word already in the words chosen for the question is chosen again by chance
        self.already_chosen = False

    def check_correct(self, option):
        """small function checks if the answer chosen in the question was correct"""
        if self.correct_index == option:
            return True
        else:
            return False








class New_Question(Buttons,Question):
    def __init__(self):
        """creates the object of a new question"""
        super(New_Question,self).__init__()
        # creates vaiable which is the number of record in the WordsTable
        self.recordno = sqlfunction.noOfRecords()


    #buttons are in english target in foreign

    def get_new_words(self):
        """gets the words to display in the exercise in the form of a 4 index long array"""

        self.passed = 0

        # loops until the array is 3 index long
        while self.passed < 4:
            self.already_chosen = False
            # chooses a random rowid
            rowid = random.randint(1,self.recordno)
            # if the word chosen isnt in both the WordTable and the WordBankTable
            if sqlfunction.inTableandBank(rowid) is False:
                # defines the word as a native word from the corresponding rowid from the WordTable
                word = sqlfunction.rowidtoNative(rowid)
                # starts a for loop for as many times as the question word array is long
                for i in self.questionWords:
                    # if any given word in the array is the same as the word attempting
                    # to enter the array its rejected
                    if i == word:
                        self.already_chosen = True
                # if the word hasnt already been chosen then it adds it to the array
                if self.already_chosen is False:
                    self.questionWords.append(word)

                    # increments the passed value
                    self.passed += 1

        # adds the foreign word at end of the array that is the counterpart to one of the native words in the array
        self.questionWords.append(sqlfunction.nativetoforeign(self.questionWords[self.correct_index]))

        return self.questionWords




class Refresher_Question(Buttons,Question):
    def __init__(self,username):
        # inherits all the inital varibales of both the button class and the questions class
        super(Refresher_Question,self).__init__()
        # defines the inital username variable within the class
        self.username = username
        # defines  bank_records as an array where each index contains the records of a user
        # from the WordBankTable
        self.bank_records = sqlfunction.wordbankids(sqlfunction.usernametoid(self.username))
        self.bank_records = [self.bank_records[i][0] for i in range(len(self.bank_records))]




    def get_new_words(self):

        # loops until the array is 3 index long
        while self.passed < 4:
            self.already_chosen = False
            # chooses a random rowid
            rowid = self.bank_records[random.randint(0,len(self.bank_records)-1)]
            # a list of word id of words the user knows
            wordid = sqlfunction.rowidtoWordid(rowid)
            # a list of native words that the user knows
            word = sqlfunction.wordidtonative(wordid)
            # calculates the knowness value of all the words in the word id table
            knowness = Question.calculate_knowness(self,sqlfunction.usernametoid(self.username),wordid)
            # if the knowness value is less than 0.5
            if knowness < 0.5:
                # if the word has already been chosen already_chosen will become true
                for i in self.questionWords:
                    if i == word:
                        self.already_chosen = True
                # if already chosen is false
                if self.already_chosen is False:
                    # word is added to the question words array
                    self.questionWords.append(word)
                    # increments passed by one
                    self.passed += 1
        # adds a foreign word to the end of array (is the word that you have to guess in the exercise)
        self.questionWords.append(sqlfunction.nativetoforeign(self.questionWords[self.correct_index]))



        return self.questionWords

    def purge_memory(self):
        """removes records with a knowness below a certain value"""

        #for the number of rows in the bank
        studentid = sqlfunction.usernametoid(self.username)

        # if a word has a knowness of less than 0.00001 (in other words its been completely forgotten )
        for i in self.bank_records:
            wordid = sqlfunction.bankid_wordid(i)
            knowness = Question.calculate_knowness(self,studentid,wordid)

            if knowness < 0.01:
                sqlfunction.delete_wordbank_record(studentid,wordid)

    def check_enough(self):
        """checks that at least 10 words have a knowness of at least 0.5 in the WordBankTable
         for a specific user so that there are enough words for the new words functions to get"""

        pass_amount = 0
        for i in self.bank_records:
            foo = Question.calculate_knowness(self,sqlfunction.usernametoid(self.username), sqlfunction.bankid_wordid(i))
            if foo < 0.5:
                # increments pass amount by 1
                pass_amount += 1
        if pass_amount < 10:
            return False
        else:
            return True



class Topic_Questions(Buttons,Question):
    """class that runs topic questions"""
    def __init__(self):
        # inherits variables from button and question class
        super(Topic_Questions,self).__init__()


    def get_new_words(self,topic_id):
        """generates words for each  topic question"""

        # selects all the words in a given topic
        pool = sqlfunction.get_topic_words(topic_id)

        while self.passed < 4:
            self.already_chosen = False
            # selects a word from the pool at random
            word = list(pool[random.randint(0,len(pool)-1)])[0]
            # checks if the word is already in the list
            for i in self.questionWords:
                if i == word:
                    self.already_chosen = True
            # if the word isnt already in the questionWords array it adds it to the questionWord array
            if self.already_chosen is False:
                self.questionWords.append(word)
                self.passed += 1
        # adds a native word on at the end
        self.questionWords.append(sqlfunction.nativetoforeign(self.questionWords[self.correct_index]))

        return self.questionWords


