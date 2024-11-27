from tkinter import *
import math as m
#tavabe

num1=''
num2=''
oper=''
flag_oper = False
flag_func = False
flag_equal = False
oper_count = 0
#-------------------------------
def clear_entry():
    global num1
    global num2
    global oper
    global flag_oper
    global flag_equal
    global flag_func 

    num1=''
    num2=''
    oper=''
    flag_equal = False
    flag_oper = False
    flag_func = False
    label_result['text']='0'

#----------------
def oper_insert( operator ):
    
    global oper,flag_oper,oper_count
    if oper_count != 0 :
        total() 
        oper_count = 0

    oper = operator
    flag_oper = True
    oper_count = oper_count + 1

#--------------------------------------------
def button_click(number):
    

    global num1
    global num2
    global flag_equal

    if flag_equal ==True and flag_oper == False:
        
        num1 = ''
        flag_equal = False

    if flag_oper == False:
        num1 = num1 + number
        label_result['text'] = num1
        
    else:
         num2 = num2 + number
         label_result['text'] =  num2

def backspace():
    global num1
    global num2
    global oper
    
    current = label_result.cget("text")
    label_result["text"] = current[:-1]
    
    if label_result['text'] == '':
        label_result['text'] = '0'
    
    if oper == '':
        num1 = ''
    else:
        num2 = ''

def toggle_sign():
    
    global num1
    global num2
    
    if flag_oper == False:
        if num1 != '':            
            num1=str(float(num1) * -1) 
            label_result['text'] = num1
        
    else:
        if num2 != '':            
            num2=str(float(num2) * -1)
            label_result['text'] = num2

def fact():
    num = int(label_result.cget("text"))
    value=m.factorial(num)
    label_result["text"]=str(value)
    
def sqrt():
    current = label_result.cget("text")
    try:
        num = float(current) 
        value=m.sqrt(num)
        label_result["text"]=value
    except ValueError:
        label_result["text"] = "Error"

def sinus():
    current_text = label_result.cget("text")
    try:
            angle_degrees = float(current_text)
            angle_radians = m.radians(angle_degrees)
            sin_value = m.sin(angle_radians)
            label_result["text"] = sin_value
    except ValueError:
            label_result["text"] = "Error"
def cosinus():
    current_text = label_result.cget("text")
    try:
            angle_degrees = float(current_text)
            angle_radians = m.radians(angle_degrees)
            cos_value = m.cos(angle_radians)
            label_result["text"] = cos_value
    except ValueError:
            label_result["text"] = "Error"

def tanx():
    current_text = label_result.cget("text")
    try:
            angle_degrees = float(current_text)
            angle_radians = m.radians(angle_degrees)
            tan_value = m.tan(angle_radians)
            label_result["text"] = tan_value
    except ValueError:
            label_result["text"] = "Error"
def cotx():
    current_text = label_result.cget("text")
    try:
        angle_degrees = float(current_text)
        angle_radians = m.radians(angle_degrees)
        tan_value = m.tan(angle_radians)
        cot_value = 1 / tan_value
        label_result["text"] = cot_value
    except ValueError:
        label_result["text"] = "Error"

def square():
    current_text = label_result.cget("text")
    num=float(current_text)
    T2=pow(num,2)
    label_result["text"] = str(T2)
    
def Mod():
    global num1
    global num2
    num1 = float(label_result.cget("text"))
    num2 = float(num2) if num2 else 0  # Ensure num2 is converted to float, default to 0 if it's empty
    ans = m.fmod(num1, num2)
    label_result["text"] = str(ans)
def t10():
    current_text = label_result.cget("text")
    num=float(current_text)
    t10=pow(10,num)
    label_result["text"] = str(t10)

def logaritm():
    current_text = label_result.cget("text")
    try:
        num=float(current_text)
        log_value=m.log(num,10)
        label_result["text"] = str(log_value)
        
    except ValueError:
        label_result["text"] = "Error"

def exp():
    current_text = label_result.cget("text")
    try:
        num = float(current_text)
        exp_result = m.exp(num)
        label_result["text"] = str(exp_result)
    except ValueError:
        label_result["text"] = "Error"
#--------------------------
def total():
    global num2
    global num1
    global oper
    global flag_oper
    global flag_equal
    global oper_count
    total_number = 0 
        
    if oper == '+':
        total_number = float(num1)+float(num2)       

    elif oper == '-':
        total_number = float(num1)-float(num2)       

    elif oper == '*':
        total_number = float(num1)*float(num2)        

    elif oper == '/':
        try:
            total_number = float(num1)/float(num2)
            
        except ZeroDivisionError:
             label_result['text'] = m.inf

    elif oper == 'Mod':
        total_number = float(num1)%float(num2)

    label_result['text'] = str(total_number)
    num1 = str(total_number)
    num2 = ''
    oper = ''
    flag_oper = False
    flag_equal = True   
    oper_count = 0 
    #---------------------        
    
win=Tk()
win.title("Calculator")
win.geometry("1000x600+300+150")
win.resizable(False,False)
win.configure(bg="#17161b")
win.iconbitmap('calculator-icon.ico')


label_result= Label(win,width=25,height=2,text="0",font=("arial",30),bg='gray14',bd=3,relief='sunken',fg='mint cream')
label_result.pack()

frm = Frame(win,bg="#17161b", padx=5, pady=2)
frm.place(y=100)

label_made=Label(win,text="@made by Arshiya Danandeh",font=("arial",15),fg='#fff',bg="#17161b")
label_made.place(y=550)

btn_c=Button(frm,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="orange",command=clear_entry)
btn_c.grid(row=2,column=1, padx=5, pady=5)

btn_div=Button(frm,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: oper_insert('/'))
btn_div.grid(row=2,column=2, padx=5, pady=5)
btn_mul=Button(frm,text="x",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command=lambda: oper_insert('*'))
btn_mul.grid(row=2,column=3, padx=5, pady=5)
btn_left=Button(frm,text="Mod",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : oper_insert('Mod'))  
btn_left.grid(row=2,column=4, padx=5, pady=5)
btn_sum=Button(frm,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : oper_insert('+'))
btn_sum.grid(row=3,column=6, padx=5, pady=5)
btn_minus=Button(frm,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command=lambda: oper_insert('-'))
btn_minus.grid(row=4,column=6, padx=5, pady=5)

btn_7=Button(frm,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('7'))
btn_7.grid(row=3,column=1, padx=5, pady=5)
btn_8=Button(frm,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('8'))
btn_8.grid(row=3,column=2, padx=5, pady=5)
btn_9=Button(frm,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('9'))  
btn_9.grid(row=3,column=3, padx=5, pady=5)
btn_4=Button(frm,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('4'))
btn_4.grid(row=4,column=1, padx=5, pady=5)
btn_5=Button(frm,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('5'))
btn_5.grid(row=4,column=2, padx=5, pady=5)
btn_6=Button(frm,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('6'))  
btn_6.grid(row=4,column=3, padx=5, pady=5)
btn_1=Button(frm,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('1'))
btn_1.grid(row=5,column=1, padx=5, pady=5)
btn_2=Button(frm,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('2'))
btn_2.grid(row=5,column=2, padx=5, pady=5)
btn_3=Button(frm,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('3'))  
btn_3.grid(row=5,column=3, padx=5, pady=5)
btn_0=Button(frm,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('0'))  
btn_0.grid(row=6,column=1,columnspan=3,sticky='w', padx=2, pady=5)

btn_equals=Button(frm,text="=",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="khaki4",command=total) 
btn_equals.grid(row=6,column=3,columnspan=2)

btn_point=Button(frm,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click('.'))
btn_point.grid(row=5,column=4, padx=5, pady=5)
btn_cot=Button(frm,text="cot",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=cotx)
btn_cot.grid(row=3,column=4, padx=5, pady=5)
btn_neper=Button(frm,text="e",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click(str(m.e)))
btn_neper.grid(row=4,column=4, padx=5, pady=5)

btn_sin=Button(frm,text="sin",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=sinus)
btn_sin.grid(row=2,column=5, padx=5, pady=5)
btn_cos=Button(frm,text="cos",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=cosinus)
btn_cos.grid(row=3,column=5, padx=5, pady=5)
btn_tan=Button(frm,text="tan",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=tanx)
btn_tan.grid(row=4,column=5, padx=5, pady=5)
btn_log=Button(frm,text="log",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=logaritm)
btn_log.grid(row=2,column=7, padx=5, pady=5)
btn_10pow=Button(frm,text="10˟",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=t10)
btn_10pow.grid(row=5,column=5, padx=5, pady=5)
btn_sqr=Button(frm,text="x²",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=square)
btn_sqr.grid(row=2,column=6, padx=5, pady=5)
btn_pi=Button(frm,text="π",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:button_click(str(m.pi)))
btn_pi.grid(row=3,column=7, padx=5, pady=5)
btn_factorial=Button(frm,text="n!",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=fact)
btn_factorial.grid(row=4,column=7, padx=5, pady=5)
btn_sqrt=Button(frm,text="√",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=sqrt)
btn_sqrt.grid(row=5,column=7, padx=5, pady=5)
btn_exp=Button(frm,text="Exp",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=exp)
btn_exp.grid(row=6,column=7, padx=5, pady=5)

btn_backspace=Button(frm,text="⌫",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="light coral",command=backspace)
btn_backspace.grid(row=6,column=4,columnspan=5, padx=5, pady=5)

btn_edge=Button(frm,text="±",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=toggle_sign)
btn_edge.grid(row=5,column=6, padx=5, pady=5)


win.mainloop()

