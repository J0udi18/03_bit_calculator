# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    # Lists of valid responses
    text_ok = ["text", "t", "txt"]
    intenger_ok = ["integar", "int", "#", "number"]
    image_ok = ["image", "img", ]
    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("file type (iinteger / text / image): ").lower()
       # If user for choice and change response to lowercase
        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"
        
        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()


# Main routine goes here 
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()