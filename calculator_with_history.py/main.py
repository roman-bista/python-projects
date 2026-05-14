import os

BASE_DIR = os.path.dirname(__file__)
history_file = os.path.join(BASE_DIR, "history.txt")
 

def show_history():
    file=open(history_file,'r')
    lines=file.readlines()
    if len(lines) ==0:
        print("No history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()


def clear_history():
    file=open(history_file,'w')
    file.close()
    print("History cleared..")

def save_to_history(equation,result):
    file=open(history_file,'a')
    file.write(equation+ "=" +str(result)+"\n")
    file.close()


def calculate(user_input):

    parts=user_input.split()
    if len(parts) !=3:
        print("invalid input. use format:number operator number (eg. 8+8)")
        return
                                  
    num1=float(parts[0])
    operator=parts[1]
    num2=float(parts[2])
    

    if operator=="+":
        result= num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        if num2==0:
            print("Cannot divide by zero")
            return
        result=num1/num2
    else:
        print("invalid operator is detected. use only + - * /")
        return
    if int(result)==result:
        result=int(result)
    print("result:", result)
    save_to_history(user_input,result)

def main():
    print(":-----Simple calculator-----:")
    while True:
        user_input=input("Enter calculation (+,-,*,/) or command (history,clear,exit): ")
        if user_input=="exit":
            print("Goodbye thanks for using.")
            break
        elif user_input=="history":
            show_history()
        elif user_input=="clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()