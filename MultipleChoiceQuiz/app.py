from Question import Question

questions = [
  Question('Who won the 2018 world cup\n(a) France\n(b) Italy\n(c)brazil\n', 'a'),
  Question('What country did America earn independence from\n(a) Germany\n(b) Spain\n(c) Great Britain\n', 'c'),
  Question('What language is this program in\n(a) JavaScript\n(b) Python\n(c) C++\n', 'b')
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  return score

print('Your score is: ' + str(run_test(questions)) + '/' + str(len(questions)))