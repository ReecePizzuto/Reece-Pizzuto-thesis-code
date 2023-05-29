import random
import time

t = time.localtime()

all_remaining_letters = []
current_letter = ""
running = False
start_time = ""
detection = []
answers = dict()
finished = False
videoExam = False
correct_answers = 0


def initialize_sign_language_application(all_letter):
    global all_remaining_letters
    global videoExam
    for value in all_letter.values():
        all_remaining_letters.append(value)
    print("Welcome to the Maltese Sign language Exam")
    print("If you want the video exam press 1")
    print("If you want the image exam press 2")
    val = input()
    if val == '1':
        videoExam = True

def detect_letter(frame_detection):
    global running
    global detection
    global current_letter
    global start_time
    global answers
    global correct_answers
    global videoExam

    if not videoExam:
        return

    if not running:
        running = True
        detection = []
        current_letter = random.choice(all_remaining_letters)

        print("you have 10 seconds to detect: " + current_letter)
        print("enter any character to start")
        input()
        print("go")
        start_time = time.time()

    if frame_detection not in detection:
        detection.append(frame_detection)
    time_elapsed = time.time() - start_time

    if time_elapsed > 10 or current_letter in detection:
        # Checking that the letter I has also been detected when signing the letter J
        if current_letter == 'LetterJ' and 'LetterI' not in detection:
            return

        if current_letter in detection:
            print("correct answer")
            correct_answers += 1
        else:
            print("incorrect answer")

        answers[current_letter] = detection
        all_remaining_letters.remove(current_letter)
        running = False

        if len(all_remaining_letters) <= 0:
            print("Exam finished please check results below ")
            print("you got " + str(correct_answers) + " correct out of 30")

            print("Statistics for the researcher")
            for key, value in answers.items():
                print(key, value)
            exit()
