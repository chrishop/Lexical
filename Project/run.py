#!/usr/bin/env python3
import pygame,sys,button,font,textentry,sqlfunction,validator,passwordfunct,exercise,time,graph,settings
# creates data base if it doesnt already exist
sqlfunction.create_tables()
# initialsing pygame
pygame.init()
# creating screen size
size = 1920,1010
# creating pygame clock object
clock = pygame.time.Clock()
# creating screen object
screen = pygame.display.set_mode(size,0,32)
# reading settings as variable settings
setting = settings.read_settings()
# turns the string into an array
setting = setting.split(",")
# creates the relevant part of settings and defines it as RRR,GGG,BBB string
background_colour = int(setting[0]),int(setting[1]),int(setting[2])
text_colour = int(setting[3]),int(setting[4]),int(setting[5])
textbox_colour = int(setting[6]),int(setting[7]),int(setting[8])

# login page
# creates login screen surface
loginscreen = pygame.Surface(size)
# creates textbox objects
usernamebox = textentry.Textbox(loginscreen,60,16,textbox_colour,text_colour)
passwordbox = textentry.Textbox(loginscreen,60,16,textbox_colour,text_colour)
# creates username and login buttons
newuserbut = button.Button(loginscreen,180,60)
loginbut = button.Button(loginscreen,180,60)
# defines failsafe username
username = "chopkins"
# defines validation checks
presencecheck = True
passwordcheck = True


# new user page
# creates new user screen surface
newuserscreen = pygame.Surface(size)
# creates textboxes for new user page
usernameboxnu= textentry.Textbox(newuserscreen,60,16,textbox_colour,text_colour)
passwordboxnu = textentry.Textbox(newuserscreen,60,16,textbox_colour,text_colour)
passwordboxnu2 = textentry.Textbox(newuserscreen,60,16,textbox_colour,text_colour)
firstnamebox = textentry.Textbox(newuserscreen,60,16,textbox_colour,text_colour)
lastnamebox = textentry.Textbox(newuserscreen,60,16,textbox_colour,text_colour)
# creates buttons for new user page
loginbutnu = button.Button(newuserscreen,180,60)
backbutnu = button.Button(newuserscreen,180,60)
# defines validation checks
presencechecknu = True
usernamecheck = True
passwordchecknu = True
passwordchecknu2 = True
namecheck = True


# main menu
# create main menu screen
menuscreen = pygame.Surface(size)
# create buttons for main menu pages
backbutm = button.Button(menuscreen,180,60,60)
exercisebut = button.Button(menuscreen,400,80)
reportsbut = button.Button(menuscreen,400,80)
settingsbut = button.Button(menuscreen,400,80)


# Exercise menu
# creates exercise menu screen
exercisemenuscreen = pygame.Surface(size)
# creates buttons for exercise menu scree
backbutex = button.Button(exercisemenuscreen,180,60)
continuebut = button.Button(exercisemenuscreen,500,80)
refreshbut = button.Button(exercisemenuscreen,500,80)
bysubjectbut = button.Button(exercisemenuscreen,500,80)


# settings
# creates setting menu screen
settings_menu_screen = pygame.Surface(size)
# creates text box objects
background_colour_box = textentry.Textbox(settings_menu_screen,60,11,textbox_colour,text_colour)
text_colour_box = textentry.Textbox(settings_menu_screen,60,11,textbox_colour,text_colour)
textbox_colour_box = textentry.Textbox(settings_menu_screen,60,11,textbox_colour,text_colour)
# creates buttons
backbut_s = button.Button(settings_menu_screen)
savebut = button.Button(settings_menu_screen)
# check for setting validations
setting_valid = True


# topic specific
# create topic menu screen
topicmenuscreen = pygame.Surface(size)
# creates buttons for screen
backbutt = button.Button(topicmenuscreen,180,60)
hellobut = button.Button(topicmenuscreen,650,80)
converationbut = button.Button(topicmenuscreen,650,80)
shoppingbut = button.Button(topicmenuscreen,650,80)
transportationbut = button.Button(topicmenuscreen,650,80)
eatingbut = button.Button(topicmenuscreen,650,80)
directionsbut = button.Button(topicmenuscreen,650,80)
sightseeingbut = button.Button(topicmenuscreen,650,80)
accommodationbut = button.Button(topicmenuscreen,650,80)
emergencybut = button.Button(topicmenuscreen,650,80)
numbersbut = button.Button(topicmenuscreen,650,80)


# continue
newexercisesscreen = pygame.Surface(size)
# creates back button
backbutnex = button.Button(newexercisesscreen,180,60,60)
# creates option buttons for exercise
opt1but_c = button.Button(newexercisesscreen,800,60,30)
opt2but_c = button.Button(newexercisesscreen,800,60,30)
opt3but_c = button.Button(newexercisesscreen,800,60,30)
opt4but_c = button.Button(newexercisesscreen,800,60,30)
# initialises variables to control new exercise
correct_c = False
make_exercise = False
wrong_c = False
question_no = 10
question_loop_c = 0

# refresher page
# creates refresher screen
refresher_exercise_screen = pygame.Surface(size)
# creates buttons for exercise
backbut_r = button.Button(refresher_exercise_screen,180,60,60)
opt1but_r = button.Button(refresher_exercise_screen,800,60,30)
opt2but_r = button.Button(refresher_exercise_screen,800,60,30)
opt3but_r = button.Button(refresher_exercise_screen,800,60,30)
opt4but_r = button.Button(refresher_exercise_screen,800,60,30)
# initialises variables to control refresher exercise
correct_r = False
make_exercise_r = True
wrong_r = False
question_no_r = 10
question_loop_r = 0


# topic page
# creates topic exercise page
topic_exercise_screen = pygame.Surface(size)
# creates buttons for exercise
backbut_t = button.Button(topic_exercise_screen,180,60,60)
opt1but_t = button.Button(topic_exercise_screen,800,60,30)
opt2but_t = button.Button(topic_exercise_screen,800,60,30)
opt3but_t = button.Button(topic_exercise_screen,800,60,30)
opt4but_t = button.Button(topic_exercise_screen,800,60,30)
# initialises variables to control topic exercise
correct_t = False
make_exercise_t = True
wrong_t = False
topic_id = 0
question_no_t = 10
question_loop_t = 0


# initialises score variable or all exercises
score = 0


# error page
# creates error page
error_screen = pygame.Surface(size)
# creates back button
backbut_err = button.Button(error_screen,180,60,60)


# report page
# creates report screen
report_screen = pygame.Surface(size)
# creates back button
backbut_rp = button.Button(report_screen,180,60,60)


# sets pg id
pg_id = 0


# starts runtime loop
# starts the infinite while loop
while 1:
    # fetches event from pygame
    events = pygame.event.get()

    # checks for a quit event
    for event in events:
        if event.type == pygame.QUIT:
            # quits both pygame and python
            pygame.quit()
            sys.exit()
            break

    # login page
    if pg_id is 0:
        loginscreen.fill(background_colour)
        # draws text onto the screen
        font.TextToScreen(loginscreen, "Lexical", 0, -460, 100,text_colour)
        font.TextToScreen(loginscreen, "Username", 0, -360,60,text_colour)
        font.TextToScreen(loginscreen, "Password", 0, -180,60,text_colour)
        # makes variables equal to the input of the textbox
        username = usernamebox.make(0, -290, events)
        password = passwordbox.makepass(0, -110, events)
        # draws new user button and check for button pressed
        if newuserbut.create(event, "New?", 400, 360) == True:
            pg_id = 1
        # draws new user button and check for button pressed
        if loginbut.create(event, "Login", 400, 432) is True:
            # if nothing is present inside any of the boxes
            if username == "" or password == "":
                presencecheck = False
            else:
                presencecheck = True
                # if the hashed password maches the hash in the database
                if passwordfunct.check(password, sqlfunction.password(username)) == True:
                    passwordcheck = True
                    pg_id = 2
                else:
                    passwordcheck = False

        # Error messages
        if presencecheck is False:
            font.TextToScreen(loginscreen, "Fill all Fields", 0, -410, 20, (255, 0, 0))

        if passwordcheck is False:
            font.TextToScreen(loginscreen, "Password and Username don't match", 0, -230, 20, (255, 0, 0))

    # new user
    if pg_id is 1:
        newuserscreen.fill(background_colour)
        # draws text to screen
        font.TextToScreen(newuserscreen, "Lexical", 0, -460, 100,text_colour)
        font.TextToScreen(newuserscreen, "Username", 0, -360,60,text_colour)
        font.TextToScreen(newuserscreen, "Password", 0, -180,60,text_colour)
        font.TextToScreen(newuserscreen, "Confirm Password", 0, 0, 60, text_colour)
        font.TextToScreen(newuserscreen, "First Name", 0, 180, 60, text_colour)
        font.TextToScreen(newuserscreen, "Last Name", 0, 360, 60, text_colour)
        # makes and gets input from text boxes
        username = usernameboxnu.make(0, -290, events)
        password = passwordboxnu.makepass(0, -110, events)
        password2 = passwordboxnu2.makepass(0, 70, events)
        firstname = firstnamebox.make(0, 250, events)
        lastname = lastnamebox.make(0, 430, events)
        # creates back button
        if backbutnu.create(event, "Back", -860, -460) is True:
            print("Back")
            pg_id = 0
        # creates login button
        if loginbutnu.create(event, "Login", 400, 432) is True:
            # checks for empty fields
            if username is "" or password is "" or password2 is "" or firstname is "" or lastname is "":
                presencechecknu = False
            else:
                presencechecknu = True
                # checks that there isnt an existing username in the database
                if sqlfunction.usernameUnique(username) is True:
                    usernamecheck = True
                    # checks that password is valid
                    if validator.Password(password) is True:
                        passwordchecknu = True
                        # checks the password and confirm password
                        if password == password2:
                            passwordchecknu2 = True
                            # checks the names are valid
                            firstnamevalid = validator.NameValidation(firstname)
                            lastnamevalid = validator.NameValidation(lastname)
                            if firstnamevalid is False or lastnamevalid is False:
                                namecheck = False
                            else:
                                # hashes the password
                                password = passwordfunct.make(password)
                                # stores valid information into the database
                                sqlfunction.enterPersonalTable(username, password, firstnamevalid,
                                                               lastnamevalid)
                                pg_id = 2
                        else:
                            passwordchecknu2 = False

                    else:
                        passwordchecknu = False



                else:
                    usernamecheck = False

        # Error Messages
        if presencechecknu is False:
            font.TextToScreen(newuserscreen, "Fill all Fields", 0, -410, 20, (255, 0, 0))

        if usernamecheck is False:
            font.TextToScreen(newuserscreen, "This username has already been taken", 0, -230, 20, (255, 0, 0))

        if passwordchecknu is False:
            font.TextToScreen(newuserscreen, "Please use a 8-16 digit password with a capital letter and a number", 0,
                              -50, 20, (255, 0, 0))

        if passwordchecknu2 is False:
            font.TextToScreen(newuserscreen, "The passwords do not match, please try again", 0, 130, 20, (255, 0, 0))

        if namecheck is False:
            font.TextToScreen(newuserscreen, "Names do not contain numbers, silly", 0, 310, 20, (255, 0, 0))

    # main menu
    if pg_id is 2:
        menuscreen.fill(background_colour)
        # draws the text to the screen
        font.TextToScreen(menuscreen, "Lexical", 0, -460, 100,text_colour)
        # creates buttons and triggers
        if backbutm.create(event,"Back",) is True:
            pg_id = 0
        if exercisebut.create(event,"Exercise",0,-250) is True:
            pg_id = 3
        if reportsbut.create(event,"Reports",0,0) is True:
            pg_id = 4
        if settingsbut.create(event,"Settings",0,250) is True:
            pg_id = 5

    # exercise menu
    if pg_id is 3:
        score = 0
        exercisemenuscreen.fill(background_colour)
        # draws text to the screen
        font.TextToScreen(exercisemenuscreen,"Lexical",0,-460,100,text_colour)
        if backbutex.create(event,"Back") is True:
            pg_id = 2

        if continuebut.create(event,"Continue",0,-250) is True:
            make_exercise = True
            pg_id = 7

        if refreshbut.create(event,"Refresh",0,0) is True:
            pg_id = 6
            make_exercise_r = True

            
        if bysubjectbut.create(event,"By Subject",0,250) is True:
            pg_id = 8

    # report page
    if pg_id is 4:
        report_screen.fill(background_colour)
        if backbut_rp.create(event,"Back") is True:
            pg_id = 2
        # fetches an array of the scores the users got on their exercises
        y_arr = sqlfunction.user_exercises(sqlfunction.usernametoid(username))
        # draws graph to screen
        graph.Graph(report_screen,1000,800,list(range(len(y_arr)+1))[1:],y_arr,"exercises","score").draw_graph(900,900)
        # gets names to from data base to draw on screen
        font.TextToScreen(report_screen,str(sqlfunction.get_name(username)[0]),50,200,60,text_colour,1)
        font.TextToScreen(report_screen,str(sqlfunction.get_name(username)[1]),50,260,60,text_colour,1)
        font.TextToScreen(report_screen,"Words Known:", 50, 400, 60, (0, 0, 0), 1)
        # fetches the amount of words known
        font.TextToScreen(report_screen,str(len(exercise.Refresher_Question(username).bank_records)), 50, 460, 60,text_colour, 1)
        font.TextToScreen(report_screen,"Exercises Completed:", 50, 600, 60,
                      (0, 0, 0), 1)
        # fetches the amount of exercises completed by a user
        font.TextToScreen(report_screen,str(sqlfunction.exercise_completed(sqlfunction.usernametoid(username))), 50, 660, 60,text_colour, 1)

    # settings menu
    if pg_id is 5:
        settings_menu_screen.fill(background_colour)
        if backbut_s.create(event,"Back") is True:
            pg_id = 2
        # draws text onto the screen
        font.TextToScreen(settings_menu_screen, "Lexical", 0, -460, 100,text_colour)
        font.TextToScreen(settings_menu_screen, "Background Colour", 0, -360,60,text_colour)
        font.TextToScreen(settings_menu_screen, "Text Colour", 0, -180,60,text_colour)
        font.TextToScreen(settings_menu_screen, "Textbox Colour", 0, 0,60,text_colour)
        # creates textbox
        background_colour_input = background_colour_box.make(0, -290, events)
        text_colour_input = text_colour_box.make(0, -110, events)
        textbox_colour_input = textbox_colour_box.make(0, 70, events)
        if savebut.create(event, "Save", 400, 432) is True:
            # creates setting pack from existing variables
            setting_pack = background_colour_input +","+ text_colour_input +","+ textbox_colour_input
            # checks if inputs are valid
            if validator.check_settings(setting_pack) is True:
                # writes settings for file
                settings.write_settings(setting_pack)
                setting_valid = True
            else:
                setting_valid = False

        if setting_valid == False:
            font.TextToScreen(settings_menu_screen, "please enter valid RGB colour codes", 0, -410, 20, (255, 0, 0))


    # refresher
    if pg_id is 6:
        if make_exercise_r is True:
            # creates an object to purge the database of unknown words
            purge = exercise.Refresher_Question(username)
            # clears words that aren't 'known'
            purge.purge_memory()
            # creates exercise object
            refresher_exercise = exercise.Refresher_Question(username)

            #means that the object is only created once
            make_exercise_r = False
        # checks if there are enough words to start the exercise
        if refresher_exercise.check_enough() is True:
            # fetches new words to user in exercise from the database
            words = refresher_exercise.get_new_words()






            refresher_exercise_screen.fill(background_colour)
            # draws text
            font.TextToScreen(refresher_exercise_screen, "Lexical", 0, -460, 100,text_colour)
            font.TextToScreen(refresher_exercise_screen, "Score", 860, -480,60,text_colour)
            # draws score
            font.TextToScreen(refresher_exercise_screen, str(score)[0:3], 860, -420,60,text_colour)
            # draws rectangles
            pygame.draw.rect(refresher_exercise_screen, (250, 250, 250), (validator.centre(0, -150, 400, 400)))
            pygame.draw.rect(refresher_exercise_screen, (250, 250, 250), (validator.centre(0, 150, 1400, 100)))

            # creates back button
            if backbut_r.create(event, "Back") is True:
                pg_id = 3
            # creates option buttons
            if opt1but_r.create(event, words[0], -425, 300) is True:
                # checks the exercise object to see if the option is correct
                if refresher_exercise.check_correct(0) is True:
                    correct_r = True
                else:
                    wrong_r = True
            if opt2but_r.create(event, words[1], -425, 400) is True:
                # checks the exercise object to see if the option is correct
                if refresher_exercise.check_correct(1) is True:
                    correct_r = True
                else:
                    wrong_r = True
            if opt3but_r.create(event, words[2], 425, 300) is True:
                # checks the exercise object to see if the option is correct
                if refresher_exercise.check_correct(2) is True:
                    correct_r = True
                else:
                    wrong_r = True
            if opt4but_r.create(event, words[3], 425, 400) is True:
                # checks the exercise object to see if the option is correct
                if refresher_exercise.check_correct(3) is True:
                    correct_r = True
                else:
                    wrong_r = True
            #draws the correct word in the foreign language above
            font.TextToScreen(refresher_exercise_screen, words[4], 0, 150, 50,text_colour)

            #if a option button pressed
            if correct_r is True or wrong_r is True:
                #defines variables using sql functions
                wordid_r = sqlfunction.foreigntoid(words[4])
                times_correct_r = sqlfunction.knowness(sqlfunction.usernametoid(username),wordid_r)[0][0]
                last_answered = sqlfunction.knowness(sqlfunction.usernametoid(username), wordid_r)[0][1]
                studentid = sqlfunction.usernametoid(username)

                if correct_r is True:
                    # adds the score from getting the question right to the existing score of the exercise
                    score += 10
                    # increases loop counter by one
                    question_loop_r += 1
                    # updates the word in the WordBankTable of the database
                    # increasing the times correct variable by one
                    # and updating the time since it was last answered correctly
                    sqlfunction.updateknowness(times_correct_r+1,time.time(),studentid,wordid_r)

                if wrong_r is True:
                    # increases loop counter by one
                    question_loop_r += 1
                    # resets variables for the next question

                    # if the word has only been answered correctly once before
                    if times_correct_r == 1:
                        # delete the word you got wrong from the WordBankTable
                        sqlfunction.delete_wordbank_record(studentid,wordid_r)
                    else:
                        # update knownesss so that it decreases by one but dont update the time
                        sqlfunction.updateknowness(times_correct_r - 1, last_answered, studentid, wordid_r)

                correct_r = False
                wrong_r = False
                make_exercise_r = True

                # if 10 questions have been answered
                if question_loop_r >= 10:
                    # enter the score from the exercise into the ExerciseTable in the database
                    sqlfunction.enterExerciseTable(studentid, score)
                    # reset the score and question loop ready for the next exercise
                    score = 0
                    question_loop_r = 0
                    #take the user back to the exercise menu screen
                    pg_id = 3

        else:
            # if not enough word for refresher exercise it redirects to an error page
            pg_id = 10





    # new exercise
    if pg_id is 7:
        if make_exercise is True:
            # creates question object
            new_exercise = exercise.New_Question()
            # fetches new words for the question
            words = new_exercise.get_new_words()
            # resets the trigger so that the question object is only made once until re triggered
            make_exercise = False

        newexercisesscreen.fill(background_colour)
        # draws text onto the screen
        font.TextToScreen(newexercisesscreen, "Lexical", 0, -460, 100,text_colour)
        font.TextToScreen(newexercisesscreen, "Score", 860, -480,60,text_colour)
        # draws the score onto the screen
        font.TextToScreen(newexercisesscreen, str(score)[0:3], 860, -420,60,text_colour)
        # draws rectangles
        pygame.draw.rect(newexercisesscreen, (250, 250, 250), (validator.centre(0, -150, 400, 400)))
        pygame.draw.rect(newexercisesscreen, (250, 250, 250), (validator.centre(0, 150, 1400, 100)))

        # creates back button
        if backbutnex.create(event, "Back") is True:
            pg_id = 3
        # creates option buttons and button triggers
        if opt1but_c.create(event, words[0], -425, 300) is True:
            if new_exercise.check_correct(0) is True:
                correct_c = True
            else:
                wrong_c = True

        if opt2but_c.create(event, words[1], -425, 400) is True:
            if new_exercise.check_correct(1) is True:
                correct_c = True
            else:
                wrong_c = True

        if opt3but_c.create(event, words[2], 425, 300) is True:
            if new_exercise.check_correct(2) is True:
                correct_c = True
            else:
                wrong_c = True

        if opt4but_c.create(event, words[3], 425, 400) is True:
            if new_exercise.check_correct(3) is True:
                correct_c = True
            else:
                wrong_c = True
        # draws the target word in the foreign language
        font.TextToScreen(newexercisesscreen, words[4], 0, 150, 50,text_colour)
        if correct_c is True:
            wordid_c = sqlfunction.foreigntoid(words[4])
            # as this word is not known to the user before they see it
            # the word can be entered into the WordBankTable not updated
            # the word is input with a times_correct value of 1 and the current unix timestamp value
            sqlfunction.enterWordBankTable(sqlfunction.usernametoid(username),
                                           sqlfunction.foreigntoid(words[4]), 1, time.time())

            # increments the question loop by 1
            question_loop_c += 1
            # increment the score by 1
            score += 10
            #resets variables for next question
            correct_c = False
            wrong_c = False
            make_exercise = True

        if wrong_c is True:
            # increments question loop by 1
            question_loop_c += 1
            #resets variables for the next question
            correct_c = False
            wrong_c = False
            make_exercise = True
        # although when wrong_c is true and when correct_c is true a very similar action has to be completed
        # it has to be this way because the system is in a constant while loop and the variable resets need
        # triggered every time a option button is pressed not every loop of the program

        # if 10 questions answered
        if question_loop_c >= 10:
            # input score into the exercise table
            sqlfunction.enterExerciseTable(sqlfunction.usernametoid(username), score)
            # reset exercise variables
            score = 0
            question_loop_c = 0
            # takes user back to the userpage
            pg_id = 3

    # topic specific
    # defines column and row values for stucured layout of the topic menu
    col = [-400,400]
    row = [-210,-90,30,150,270]

    if pg_id is 8:
        topicmenuscreen.fill(background_colour)
        font.TextToScreen(topicmenuscreen,"Lexical",0,-460,100,text_colour)
        # back button drawn to the topic menu screen
        if backbutt.create(event,"Back") is True:
            pg_id = 3
        # a series of buttons that set the topic id of the topic and sent you to the topic exercise page
        if hellobut.create(event,"hello",col[0],row[0]) is True:
            topic_id = 1
            pg_id = 9
        if converationbut.create(event,"conversation",col[0],row[1]) is True:
            topic_id = 2
            pg_id = 9
        if shoppingbut.create(event,"shopping",col[0],row[2]) is True:
            topic_id = 3
            pg_id = 9
        if transportationbut.create(event,"transporation",col[0],row[3]) is True:
            topic_id = 4
            pg_id = 9
        if eatingbut.create(event,"eating",col[0],row[4]) is True:
            topic_id = 5
            pg_id = 9
        if directionsbut.create(event,"directions",col[1],row[0]) is True:
            topic_id = 6
            pg_id = 9
        if sightseeingbut.create(event,"sightseeing",col[1],row[1]) is True:
            topic_id = 7
            pg_id = 9
        if accommodationbut.create(event,"accommodation",col[1],row[2]) is True:
            topic_id = 8
            pg_id = 9
        if emergencybut.create(event,"emergency",col[1],row[3]) is True:
            topic_id = 9
            pg_id = 9
        if numbersbut.create(event,"numbers",col[1],row[4]) is True:
            topic_id = 10
            pg_id = 9


    #topic exercises
    if pg_id is 9:
        if make_exercise_t is True:
            # creates question object
            topic_exercise = exercise.Topic_Questions()
            # fetches new words
            words = topic_exercise.get_new_words(topic_id)
            # makes sure question object is created once per question
            make_exercise_t = False

        topic_exercise_screen.fill(background_colour)
        # draws text to the screen
        font.TextToScreen(topic_exercise_screen, "Lexical", 0, -460, 100,text_colour)
        font.TextToScreen(topic_exercise_screen, "Score", 860, -480,60,text_colour)
        # draws the score to the screen
        font.TextToScreen(topic_exercise_screen, str(score)[0:3], 860, -420,60,text_colour)
        # draws rectangles
        pygame.draw.rect(topic_exercise_screen, (250, 250, 250), (validator.centre(0, -150, 400, 400)))
        pygame.draw.rect(topic_exercise_screen, (250, 250, 250), (validator.centre(0, 150, 1400, 100)))

        # when back button is pressed it redirects to the exercise menu screen
        if backbut_t.create(event, "Back") is True:
            pg_id = 3
        # creates option button for exercise
        if opt1but_t.create(event, words[0], -425, 300) is True:
            if topic_exercise.check_correct(0) is True:
                correct_t = True
            else:
                wrong_t = True

        if opt2but_t.create(event, words[1], -425, 400) is True:
            if topic_exercise.check_correct(1) is True:
                correct_t = True
            else:
                wrong_t = True

        if opt3but_t.create(event, words[2], 425, 300) is True:
            if topic_exercise.check_correct(2) is True:
                correct_t = True
            else:
                wrong_t = True

        if opt4but_t.create(event, words[3], 425, 400) is True:
            if topic_exercise.check_correct(3) is True:
                correct_t = True
            else:
                wrong_t = True
        # draws target word to screen
        font.TextToScreen(topic_exercise_screen, words[4], 0, 150, 50,text_colour)

        # if a option button is pressed
        if correct_t is True or wrong_t is True:
            # creates defualt value for variable new_word
            new_word = False
            #finds the word id of the word
            wordid_t = sqlfunction.foreigntoid(words[4])
            #finds student id using the username
            studentid = sqlfunction.usernametoid(username)
            # if it cant find knowness values in the word bank table
            # then the word must be one the user hasn't seen before
            try:
                times_correct_t = sqlfunction.knowness(sqlfunction.usernametoid(username),wordid_t)[0][0]
                last_answered = sqlfunction.knowness(sqlfunction.usernametoid(username), wordid_t)[0][1]
            except IndexError:
                new_word = True



            if correct_t is True:
                # if the word the user is being tested on is new
                if new_word is True:
                    # enter a new word into the word bank table with a times_correct of 1 and current unix time
                    sqlfunction.enterWordBankTable(sqlfunction.usernametoid(username),
                                                   sqlfunction.foreigntoid(words[4]), 1, time.time())

                else:
                    # if the word is known add 1 to times correct and update time
                    sqlfunction.updateknowness(times_correct_t + 1, time.time(), studentid, wordid_t)

                # increments the score by 1
                score += 10

                # increments question loop
                question_loop_t += 1
                # resets question values
                correct_t = False
                wrong_t = False
                make_exercise_t = True



            if wrong_t is True:
                # increments question loop
                question_loop_t += 1
                # resets question loop
                correct_t = False
                wrong_t = False
                make_exercise_t = True
                # if the word is known to the user
                if new_word is False:
                    # if the word has only been answered correctly once
                    if times_correct_t == 1:
                        # deletes record from the word bank table
                        sqlfunction.delete_wordbank_record(studentid, wordid_t)
                    else:
                        # if the word has a times_correct value of above 1
                        # it subtracts one from times correct and doesnt update the unix timestamp
                        sqlfunction.updateknowness(times_correct_t - 1, last_answered, studentid, wordid_t)


            # if 10 questions have been answered
            if question_loop_t >= 10:
                # makes record of score in the exercise table
                sqlfunction.enterExerciseTable(studentid,score)
                # resets exercise triggers
                score = 0
                question_loop_t = 0
                # directs user back to exercise menu
                pg_id = 3


    if pg_id is 10:
        error_screen.fill(background_colour)
        # craw back button to screen
        if backbut_err.create(event,"Back") == True:
            pg_id = 3
        # draws error message to screen
        font.TextToScreen(error_screen,"You dont know enough words to complete this section",0,-110,60,text_colour)
        font.TextToScreen(error_screen,"please try another exercise",0,0,60,text_colour)








    # blit control

    # blits each screen to the pygame window dependant upon the pg_id triggers
    if pg_id is 0:
        pygame.display.set_caption("LoginPage")
        screen.blit(loginscreen,(0,0))

    if pg_id is 1:
        pygame.display.set_caption("NewUserPage")
        screen.blit(newuserscreen,(0,0))

    if pg_id is 2:
        pygame.display.set_caption("MainMenu")
        screen.blit(menuscreen,(0,0))

    if pg_id is 3:
        pygame.display.set_caption("Exercise Menu")
        screen.blit(exercisemenuscreen,(0,0))

    if pg_id is 4:
        screen.blit(report_screen,(0,0))

    if pg_id is 5:
        screen.blit(settings_menu_screen,(0,0))

    if pg_id is 6:
        screen.blit(refresher_exercise_screen,(0,0))

    if pg_id is 7:
        screen.blit(newexercisesscreen,(0,0))

    if pg_id is 8:
        screen.blit(topicmenuscreen,(0,0))

    if pg_id is 9:
        screen.blit(topic_exercise_screen,(0,0))

    if pg_id is 10:
        screen.blit(error_screen,(0,0))

    pygame.display.update()
    clock.tick(30)
