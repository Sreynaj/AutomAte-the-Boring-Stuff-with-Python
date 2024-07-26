import os
import random

# Create a directory for the quiz files if it doesn't exist
folder_name = 'quizzes'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
    'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
    'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

for quizNum in range(35):
    quizFilePath = os.path.join(folder_name, 'capitalsquiz%s.txt' % (quizNum + 1))
    answerKeyFilePath = os.path.join(folder_name, 'capitalsquiz_answers%s.txt' % (quizNum + 1))

    with open(quizFilePath, 'w') as quizFile, open(answerKeyFilePath, 'w') as answerKeyFile:
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        states = list(capitals.keys())
        random.shuffle(states)

        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
