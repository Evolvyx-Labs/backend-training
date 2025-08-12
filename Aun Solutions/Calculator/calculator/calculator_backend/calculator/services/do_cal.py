import json
import math

class Math:
    def s_root(a):
        b = math.sqrt(a)
        return b

    def power (a,b):
        c= a**b
        return c

    def multiply (a,b):
        c=a*b
        return c

    def devide (a,b):
        c=a/b
        return c
    
    def mod (a,b):
        c=a%b
        return c

    def add (a,b):
        c=a+b
        return c

    def subtract (a,b):
        c=a-b
        return c



prec = [
    {
        'operation': '(',
        'function' : '',
        'order' : 1
    },
    
    {
        'operation': '^',
        'function' : getattr(Math, 'power'),
        'order' : 2
    },

    {
        'operation': '√',
        'function' : getattr(Math, 's_root'),
        'order' : 3
    },

    {
        'operation': '*',
        'function' : getattr(Math, 'multiply'),
        'order' : 4
    },

    {
        'operation': '%',
        'function' : getattr(Math, 'mod'),
        'order' : 5
    },

    {
        'operation': '/',
        'function' : getattr(Math, 'devide'),
        'order' : 5
    },


    {
        'operation': '+',
        'function' : getattr(Math, 'add'),
        'order' : 6
    },

    {
        'operation': '-',
        'function' : getattr(Math, 'subtract'),
        'order' : 7
    },

]



operators = ['(','^','√','*','%','/','+','-',')']


def exp_split(exp, opr=operators):
    current = ''
    result = []
    for i in exp:
        if i in opr:
            if current:
                result.append(current)
                current = ''
            result.append(i)
        else:
            current += i
    if current:
        result.append(current)
    return result




def exp_parser(expression,precedence=prec):
    exp_list = exp_split(expression)
    if len(exp_list)<=1:
        return exp_list[0]

    k=0
    while k < len(precedence):
        i=0
        while i <len(exp_list):
            if exp_list[i]==precedence[k]['operation'] and precedence[k]['operation']=='(':
                temp=[]
                count=1
                start = i
                i=i+1
                while (count!=0 ):
                    if (exp_list[i]=='('):
                        count=count+1
                    elif(exp_list[i]==')'):
                        count=count-1
                        
                    temp.append(exp_list[i])
                    i=i+1
                    end = i
                    
    
                temp.pop()
                if len(temp)==1:
                    sub_result=temp
                else:
                    sub_result = exp_parser(temp,precedence)
                    sub_result = sub_result[:-1]
                exp_list[start:end] = sub_result
                i=0
                

                temp.clear()
            
            elif exp_list[i]==precedence[k]['operation']and precedence[k]['operation']=='√':
                z=float(exp_list[i+1])
                exp_list[i]= str(precedence[k]['function'](z))
                exp_list[i:i+2]=[exp_list[i]] 

            elif exp_list[i]==precedence[k]['operation']:
                x=float(exp_list[i-1])
                y=float(exp_list[i+1])
                exp_list[i]= str(precedence[k]['function'](x,y))
                exp_list[i-1:i+2]=[exp_list[i]] 
            else:
                i=i+1
        k=k+1
        
    return (exp_list[0]), 1
        