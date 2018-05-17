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
```