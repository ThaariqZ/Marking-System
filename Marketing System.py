# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.
# Any code taken from other sources is referenced within my code soluton.
# Student ID: 20221900 / W20537582
# Date: 12/12/2023



#Calling graphics.py
from graphics import *

#initializing variables
role=0
option=""
outcome=0
progress=0
module_trailer=0
module_retriever=0
exclude=0
pass_mark=0
defer_mark=0
fail_mark=0
total_marks=0
list=[]



#Function to get relevant marks for the loop
def get_valid_mark(marks):
    
    while True:
        try:
            mark = int(input(marks))
            if mark in range(0, 121, 20):
                return mark
            else:
                print("Out of Range")
        except ValueError:
            print("Integer Required")
        except KeyboardInterrupt:
            print("Error, Try again")

#function to create the histogram
def draw_histogram():
    height_1=0
    height_2=0
    height_3=0
    height_4=0
    global progress, module_retriever, module_trailer, exclude


    try:
        
        # Create a graphics window.
        win = GraphWin("Histogram", 400, 360)

        # Window
        label = Text(Point(80, 24), 'Histogram Results')
        label.draw(win)

        #creating the 1st column
        height_1=300-(progress*10)
        label = Text(Point(60, (height_1-15)), progress)
        box = Rectangle(Point(24, 300), Point(96, height_1)) 
        box.setFill("#B2FF85")
        box.draw(win)
        label.draw(win)

        #creating 2nd column
        height_2=300-(module_trailer*10)
        label = Text(Point(145, (height_2-15)), module_trailer)
        box = Rectangle(Point(106, 300), Point(178, height_2)) 
        box.setFill("#97B984")
        box.draw(win)
        label.draw(win)

        #creating 3rd column
        height_3=300-(module_retriever*10)
        label = Text(Point(225, (height_3-15)), module_retriever)
        box = Rectangle(Point(195, 300), Point(260, height_3)) 
        box.setFill("#90B657")
        box.draw(win)
        label.draw(win)

        #creating 4th column
        height_4=300-(exclude*10)
        label = Text(Point(310, (height_4-15)), exclude)
        box = Rectangle(Point(280, 300), Point(342, height_4))
        box.setFill("#CBA3B1")
        box.draw(win)
        label.draw(win)

        #naming the  columns
        label = Text(Point(60, 310), "Progress")
        label.draw(win)
        label = Text(Point(145, 310), "Trailer")
        label.draw(win)
        label = Text(Point(230, 310), "Retriever")
        label.draw(win)
        label = Text(Point(310, 310), "Exclude")
        label.draw(win)
        label = Text(Point(70,340),f"{outcome} outcomes in total.")
        label.draw(win)

        win.getMouse()
        win.close()

    except GraphicsError:  #This is in case user presses the close button
        print("")

#Function to get a text file of the outcomes and display that outcomes.
def get_list_file():
    global list
    file=open('Progress Outcomes.txt','w')#Writing the text file with the outcomes
    file.write("Part 3: \n")
    for x in range(len(list)):
        file.write(list[x])
        file.write('\n')
    file.close()
    file=open('Progress Outcomes.txt','r')#Reading the text file and printing the outcomes from the file
    for line in file:
        print(line, end='')
    file.close()

#function to get the outcomes as a list
def outcome_list():
    global list
    for x in list:
        print("Part 2: ")
        print(*list, sep="\n")
        print("\n")
        break

#program used when a staff member is using
def program_loop_for_staff():

    global list,progress,module_retriever,module_trailer,exclude,outcome

    while True:
        try:
            option=input("Enter 'y' to run the program & 'q' to quit : ").lower()
            if option == "y":
                pass_mark = get_valid_mark("Enter pass Mark: ")
                defer_mark = get_valid_mark("Enter defer Mark: ")
                fail_mark = get_valid_mark("Enter fail Mark: ") 

                total_marks=pass_mark+defer_mark+fail_mark
                
                #Program to choose progress
                if total_marks != 120:
                    print("Total Incorrect\n")
                    

                elif pass_mark == 120:
                    print("Progress\n")
                    list.append(f"Progress - {str(pass_mark)} , {str(defer_mark)} , {str(fail_mark)}")
                    progress += 1

                elif pass_mark == 100:
                    print("Progress (module trailer) \n")
                    list.append(f"Progress(module trailer) - {str(pass_mark)} , {str(defer_mark)} , {str(fail_mark)}")
                    module_trailer += 1

                elif fail_mark>=80 and fail_mark<=120:
                    print("Exclude\n")
                    list.append(f"Exclude - {str(pass_mark)} , {str(defer_mark)} , {str(fail_mark)}")
                    exclude += 1

                else:
                    print("Do not progress - module retriever \n")
                    list.append(f"Module retriever - {str(pass_mark)} , {str(defer_mark)} , {str(fail_mark)}")
                    module_retriever += 1


            #terminating the loop for staff
            elif option == "q":
                print("Program was terminated\n")
                outcome = progress+module_trailer+module_retriever+exclude
                break
            else:
                print("Invalid Input \n")
        
                print("Would you like to enter another set of data")
        except KeyboardInterrupt:
            print("Invalid Input")

            

    #Calling the respective functions
    outcome_list()
    get_list_file()
    draw_histogram()

#program used when a student is using
def program_for_students(): 

    global progress,module_retriever, module_trailer, exclude,total_marks

    while True:
        pass_mark = get_valid_mark("Enter pass Mark: ")
        defer_mark = get_valid_mark("Enter defer Mark: ")
        fail_mark = get_valid_mark("Enter fail Mark: ") 

        total_marks=pass_mark+defer_mark+fail_mark
        
        #Program to choose progress
        if total_marks != 120:
            print("Total Incorrect\n")
            

        elif pass_mark == 120:
            print("Progress\n")
            break

        elif pass_mark == 100:
            print("Progress (module trailer) \n")
            break

        elif fail_mark>=80 and fail_mark<=120:
            print("Exclude\n")
            break

        else:
            print("Do not progress - module retriever \n")
            break

    
#Choosing specific role and running the relevant program
while True:
    try:
        role=int(input("""Welcome to the Progression Predictor!

                If you are a Staff Member enter 1
                If you are a Student enter 2

Enter the specific role number here (1 or 2): """))

        if role == 1:
            program_loop_for_staff()
            break

        elif role == 2:
            program_for_students()
            break
            
        else:
            print("Invalid Input")
    except ValueError:
        print("Enter Valid Input") 
    except KeyboardInterrupt:
        print("Error Try Again")
