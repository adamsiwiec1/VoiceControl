from voice import talk, listen4_command

# Convert words to numbers - I did all this before trying it & now realized google already returns a number.
# ima keep it here since i wasted 10 min on it

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}

def words_to_int(input):

    print("The original string is : " + input)
    res = ''.join(help_dict[ele] for ele in input.split())
    print(f"After replace: {res}")
    try: return int(res)
    except: talk("Sorry, I'm not smart enough to handle your request.")


def translate_test():
    talk("Please say a number: ")
    command = listen4_command()
    print(command)
    # int = words_to_int(command)
    # print(f"Success! {int}")

translate_test()