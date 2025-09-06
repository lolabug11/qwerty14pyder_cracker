import random as r
import time as t

password = "7hT&zP9!fWq@zD1" #randomly generated 16 char password from chatgpt
def rand_num():
    return r.randint(1, 94)
def get_char():
    chars = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h", "8": "i", "9": "j", "10": "k", "11": "l", "12": "m", "13": "n", "14": "o", "15": "p", "16": "q", "17": "r", "18": "s", "19": "t", "20": "u", "21": "v", "22": "w", "23": "x", "24": "y", "25": "z", "26": "A", "27": "B", "28": "C", "29": "D", "30": "E", "31": "F", "32": "G", "33": "H", "34": "I", "35": "J", "36": "K", "37": "L", "38": "M", "39": "N", "40": "O", "41": "P", "42": "Q", "43": "R", "44": "S", "45": "T", "46": "U", "47": "V", "48": "W", "49": "X", "50": "Y", "51": "Z", "52": "0", "53": "1", "54": "2", "55": "3", "56": "4", "57": "5", "58": "6", "59": "7", "60": "8", "61": "9", "62": "!", "63": "\"", "64": "#", "65": "$", "66": "%", "67": "&", "68": "'", "69": "(", "70": ")", "71": "*", "72": "+", "73": ",", "74": "-", "75": ".", "76": "/", "77": ":", "78": ";", "79": "<", "80": "=", "81": ">", "82": "?", "83": "@", "84": "[", "85": "\\", "86": "]", "87": "^", "88": "_", "89": "`", "90": "{", "91": "}", "92": "~"}
    char = rand_num() #gets a random charicters index
    char -= 1
    char = str(char)
    char = chars[char] #gets random char
    return char
def get_password(length_of_pass):
    generated_password = ''
    current_char = ''
    for i in range(length_of_pass):
        current_char = get_char()
        generated_password += current_char
    return generated_password
def try_cracking(times_to_try, length_of_pass):
    start_time = t.time()
    for i in range(times_to_try):
        guess = get_password(length_of_pass)
        if guess == password:
            print(f'The password is {guess}')
            end_time = t.time()
            elapsed_time = end_time - start_time
            mins, secs = divmod(elapsed_time, 60)  # Convert to minutes and seconds
            print('✓')
            return mins, secs
            # print(f"Task completed in: {int(mins):02}:{int(secs):02} (MM:SS)")
            break
        print(i)
    mins , secs = 59,59
    return mins,secs
def try_cracking_one(times_to_try, length_of_pass):
    start_time = t.time()
    for i in range(times_to_try):
        guess = get_password(length_of_pass)
        if guess == password:
            print(f'The password is {guess}')
            end_time = t.time()
            elapsed_time = end_time - start_time
            mins, secs = divmod(elapsed_time, 60)  # Convert to minutes and seconds
            print('✓')
            # print(f"Task completed in: {int(mins):02}:{int(secs):02} (MM:SS)")
            break
        print(i)



def test_avererage_time():
    times = {}
    mins = {}
    secs = {}
    amount_of_data_points = int(input('How many data points do you want?\n'))
    times_to_try = int(input('How many passwords to you want to try?\n'))
    length_of_pass = int(input('How long is the password your trying to crack?\n'))
    for i in range(amount_of_data_points+1):
        times[i] = try_cracking(times_to_try=times_to_try, length_of_pass=length_of_pass)
    for i in range(amount_of_data_points+1):
        mins[i] = times[i][0]
    for i in range(amount_of_data_points+1):
        secs[i]= times[i][1]
    total_mins = sum(mins.values())
    total_secs = sum(secs.values())
    average_mins = total_mins / amount_of_data_points
    average_secs = total_secs / amount_of_data_points
    print(f"The average time is: {int(average_mins):02}:{int(average_secs):02} (MM:SS)")
choice = input('Do you want to find the average or do a 1 time Break?')
if 'average' in choice.lower():
    test_avererage_time()
else:
    times_to_try = int(input('How many passwords to you want to try?\n'))
    length_of_pass = int(input('How long is the password your trying to crack?\n'))
    try_cracking_one(times_to_try, length_of_pass)
