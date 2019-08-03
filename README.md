# calcul_mental

Initally for French Elementary School Students but anyone can try.

How to use:

    The script will first ask whether you are ready. 
    Entering 'No' or 'non' would stop the program
    Otherwise, would show a question.
    Enter your answer in numbers.
    The program will tell if your answer is correct or not
    and the calculation time.

Example:
```
$ python calcul_mental.py
Ready?
115 + 9 + 5 + 5 + 7 = ? 141
Correct
time = 26.2807 sec
Ready?
262 + 5 + 4 + 8 + 1 = ? 180
'180' does not seem to be a valid answer.
Please try again :)
262 + 5 + 4 + 8 + 1 = ? 280
Correct
time = 15.6669 sec
Ready?n
Thanks for trying.
You will do even better next time.
[{'answer': '141',
  'lap time': 26.280706882476807,
  'question': '115 + 9 + 5 + 5 + 7 = ? ',
  'result': 'correct'},
 {'answer': '280',
  'lap time': 15.666854858398438,
  'question': '262 + 5 + 4 + 8 + 1 = ? ',
  'result': 'correct'}]

$ python easier_mental.py
Ready? y
48 / 8 = ? 6
Correct ^3^
time = 2.09647 sec
Ready?
6 * 6 = ? 36
Correct ^3^
time = 1.35948 sec
Ready?
16/28 = ? 4/7
Correct ^3^
time = 4.83238 sec
Ready? n
Thanks for trying.
You will do even better next time.
[{'answer': '6',
  'lap time': 2.096471071243286,
  'question': '48 / 8',
  'result': 'correct'},
 {'answer': '36',
  'lap time': 1.3594825267791748,
  'question': '6 * 6',
  'result': 'correct'},
 {'answer': '4/7',
  'lap time': 4.832379102706909,
  'question': '16/28',
  'result': 'correct'}]
```