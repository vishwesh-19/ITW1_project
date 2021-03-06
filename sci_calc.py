from tkinter import *;
from tkinter import messagebox;
import numpy as np
import math

#Check whether the input string is a number or not
def is_number(s):
    if(s != ''):
        if (s.replace('.', '', 1).isdigit()):
            return True
        if (s.isdigit()):
            return True;
        if s[0] in ['-', '+', '.', '0', ' ']:
            if (s[1] == '.'):
                if (s[2:].isdigit()):
                    return True
            if (s[1] == '0' and s[2] == '.'):
                if (s[3:].isdigit()):
                    return True
            if s[1:].isdigit():
                return True;
        return False;

# Convert input number from string to integer if no "." is there in string else convert it to float    
def casting(num):
    if('.' in num):
        return float(num);
    else:
        return int(num)


# Addition function
def actionPlus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='red', bg='#9ed8ee')
    Showtemplabel.insert(0, '+');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')
    ans = "0";
    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1) == True and is_number(num2) == True and num1 != ' ' and num2 != ' '):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 + num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='red', bg='#9ed8ee')
        Showtemplabel.insert(0, '+');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Subtraction function
def actionMinus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='green', bg='#ece7e2')
    Showtemplabel.insert(0, '-');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0";

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 - num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='green', bg='#ece7e2')
        Showtemplabel.insert(0, '-');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Multiplication function
def actionMul():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='blue', bg='#cacba9')
    Showtemplabel.insert(0, 'x');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 * num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='blue', bg='#cacba9')
        Showtemplabel.insert(0, 'x');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Division function
def actionDiv():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, '/');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 / num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, '/');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
#Percentage function
def action_percent():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, '%');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str((num1/num2) * 100);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, '%');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
#Trigonometric Functions
#Cosine
def action_cos():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'cos');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.cos(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'cos');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Sine Function
def action_sin():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'sin');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.sin(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'sin');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Tan Function
def action_tan():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
    
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'tan');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.tan(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'tan');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Inverse Trigonometric Functions        
# Arc cosine Function
def action_acos():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'acos');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.acos(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'acos');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
# Arc sine function
def action_asin():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'asin');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.asin(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'asin');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
# Arc tangent function
def action_atan():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'atan');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='atan')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.atan(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'atan');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
# Logarithmic Function
def action_ln():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'ln');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.log(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'ln');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Log Function(log base 10)
def action_log():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'log_10');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.log(num1)/math.log(10))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'log_10');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Power Function
def action_power():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'power');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 ** num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'power');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
# Square Function
def action_sq():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'square');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1);
        ans = str(num1 ** 2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'square');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
# Square-root Function
def action_sq_root():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'sq_root');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1);
        ans = str(num1 ** 0.5);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'sq_root');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
# Exponential Function
def action_exp():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'exp');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.exp(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'exp');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
# Antilog Function(10 raised to the power entered number)        
def action_antilog():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, '10 ^num');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1);
        ans = str(10 ** num1);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, '10 ^num');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
# Pie function
def action_pi():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'pi');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    ans = str(math.pi)
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'pi');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    
# Floor Function
def action_floor():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'floor');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.floor(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'Floor');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
    
#Ceil Function
def action_ceil():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'ceil');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(math.ceil(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'ceil');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Factorial Function
def factorial(n):
    if(n==0):
        return 1
    elif(n>=1):
        return(n*factorial(n-1))
    else:
        return("Error")
    
def action_fact():  
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)
  
    Showtemplabel.config(fg='yellow', bg='#8dad96')
    Showtemplabel.insert(0, 'factorial');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    if(is_number(num1)==True):
        num1 = casting(num1)
        ans = str(factorial(num1))
        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='yellow', bg='#8dad96')
        Showtemplabel.insert(0, 'Factorial');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

# Main Window        
root = Tk()
root.title('ITW1 Project : Scientific Calculator')
root.geometry('500x300+200+250')
Titlelabel = Label(root, fg = 'green' , font = 'none 10 bold underline' ,text = 'Scientific Calculator', compound = CENTER)
Titlelabel.place(relx=0.1, rely=0.1, anchor='center')
Showlabel = Entry(root);
Showtemplabel = Entry(root);
Numberentry1 = Entry(root);
Numberentry2 = Entry(root);
Numberentry1.place(relx=0.3, rely=0.3, anchor='center')
Numberentry2.place(relx=0.3, rely=0.4, anchor='center')

# Operation Buttons(+,-,x,/)
plusbutton = Button(root, text="+", width = 5, command = actionPlus);
plusbutton.place(relx=0.1, rely=0.7)

minusbutton = Button(root, text="-", width = 5, command = actionMinus);
minusbutton.place(relx=0.2, rely=0.7)

mulbutton = Button(root, text="x", width = 5, command = actionMul);
mulbutton.place(relx=0.3, rely=0.7)

divbutton = Button(root, text="/", width = 5, command = actionDiv);
divbutton.place(relx=0.4, rely=0.7)

#Percent Button
percent_button = Button(root, text="%", width = 5, command = action_percent)
percent_button.place(relx=0.5, rely=0.7)

# Power Buttons
pow_button = Button(root, text="pow", width = 5, command = action_power)
pow_button.place(relx=0.6, rely=0.7)

sq_button = Button(root, text="sqr", width = 6, command = action_sq)
sq_button.place(relx=0.7, rely=0.7)

sq_root_button = Button(root, text="sqrt", width = 5, command = action_sq_root)
sq_root_button.place(relx=0.8, rely=0.7)

# Buttons for Trigonometric Functions(cos,sin,tan)
cos_button = Button(root, text="cos", width = 5, command = action_cos)
cos_button.place(relx=0.1, rely=0.8)

sin_button = Button(root, text="sin", width = 5, command = action_sin)
sin_button.place(relx=0.2, rely=0.8)

tan_button = Button(root, text="tan", width = 5, command = action_tan)
tan_button.place(relx=0.3, rely=0.8)

# Buttons for Inverse Trigonometric Functions(cos,sin,tan)
acos_button = Button(root, text="acos", width = 5, command = action_acos)
acos_button.place(relx=0.4, rely=0.8)

asin_button = Button(root, text="asin", width = 5, command = action_asin)
asin_button.place(relx=0.5, rely=0.8)

atan_button = Button(root, text="atan", width = 5, command = action_atan)
atan_button.place(relx=0.6, rely=0.8)

#Logarithmic Functions
ln_button = Button(root, text="ln", width = 5, command = action_ln)
ln_button.place(relx=0.7, rely=0.8)

log_button = Button(root, text="log", width = 5, command = action_log)
log_button.place(relx=0.8, rely=0.8)

# Exponential Button
exp_button = Button(root, text="exp", width = 5, command = action_exp)
exp_button.place(relx=0.9, rely=0.8)

# Antilog Button
antilog_button = Button(root, text="antilog", width = 5, command = action_antilog)
antilog_button.place(relx=0.1, rely=0.9)

# Pi button
pi_button = Button(root, text="pi", width = 5, command = action_pi)
pi_button.place(relx=0.2, rely=0.9)

# Floor and Ceil Function
floor_button = Button(root, text="floor", width = 5, command = action_floor)
floor_button.place(relx=0.3, rely=0.9)

ceil_button = Button(root, text="ceil", width = 5, command = action_ceil)
ceil_button.place(relx=0.7, rely=0.9)

# Factorial Button
fact_button = Button(root, text="!", width = 5, command = action_fact)
fact_button.place(relx=0.8, rely=0.9)

root.resizable(True, True);
root.mainloop();
