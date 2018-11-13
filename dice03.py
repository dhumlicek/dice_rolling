from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint


app = Flask(__name__)
 
@app.route("/")
def index():
    #return "Index"
    return render_template('index.html')
 

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    number = request.form['number']
    return 'Hello %s %s have fun learning python <br/> The number of Dice rolls are %s <br/> <a href="/">Back Home</a>' % (first_name, last_name, number)


@app.route('/dice_roll', methods=['POST'])
def diceRoll():
    x = 0
    roll_total = 0
    number = request.form['number']
    roll_list = list()
    dr_list = list()
    dot ='o '

    #while x < 2:
    #    r_num = randint(0,5)
    #    dot ='o '
    #    s = '-----\n|' + dot[r_num < 1] + ' ' + dot[r_num < 3] + '|\n|' + dot[r_num < 5]
    #    print(s + dot[r_num&1] + s[::-1])
    #    roll_total += (r_num + 1)
    #    x += 1

    while x < 2:
        r_num = randint(0,5)
        roll_list.append(r_num)
        roll_total += (r_num + 1)
        s = '-----<br/>|' + dot[r_num < 1] + ' ' + dot[r_num < 3] + '|<br/>|' + dot[r_num < 5]
        dr_list.append(s + dot[r_num&1] + s[::-1])
        x += 1
   
    

    #return roll_total
    #return('Number of Dice rolls:\t%s <br/>' \
    #        'Dice roll total:\t%s<br/>' \
    #        'Roll 1:\t%s<br/>Roll 2:\t%s<br/>' \
    #        '<a href="/">Back Home</a>' % (number, roll_total, roll_list[0], roll_list[1]))

    return render_template(
        'dice.html',**locals())

#
#def validateNum(user_num):
#    try:
#        number = int(user_num)
#        if number > 0:
#            print("Rolling the dice %s times...\n\n" % number)
#            flag = True
#            return number, flag
#        else:
#            print("Please enter a positive integer")
#            flag = False
#            number = None
#            return number, flag
#    except ValueError:
#        print("I am afraid %s is not a positive integer" % user_num)
#        flag = False
#        number = None
#        return number, flag
#
#
#val = False
#while val == False:
#    unum = input("How many times do you want to roll the dice? \n (HINT: each roll is a pair of dice) : ")
#    valnum, val = validateNum(unum)
#    #print(valnum)
#    #print(val)
#    
#n = 0
#total = 0
#full_total = 0
#
#while n < valnum:
#
#    print("-"*15," Dice roll: %s" % (n + 1))
#    total = diceRoll()
#    print("\nDice roll total: %s" % total)
#    full_total += total
#    n += 1
#
#print("-"*15,"\n\nRolled dice %s times.\nTotal Roll amount : %s" % (valnum, full_total))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)