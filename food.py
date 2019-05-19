import pandas as pd
import pulp as plp

data = pd.read_csv('food data0.csv')
data.set_index('name',inplace=True)

class Food:
    def __init__(self,name,priceperserving, servingsize,kcal,carb,protein,fat,fiber,suger,A,C,Calcium,Iron,Cholesterol):
       self.name=name
       self.priceperserving=priceperserving
       self.servingsize=servingsize
       self.kcal=kcal
       self.carb=carb
       self.protein=protein
       self.fat = fat
       self.fiber = fiber
       self.suger=suger
       self.A=A
       self.C=C
       self.Calcium=Calcium
       self.Iron = Iron
       self.Cholesterol=Cholesterol
       global data
       data.loc[name]=[priceperserving, servingsize,kcal,carb,protein,fat,fiber,suger,A,C,Calcium,Iron,Cholesterol]

def addfood(namevar,pricevar,servingsizevar,kcalvar,carbvar, provar,fatvar,fibervar,sugervar,Avar,Cvar,Calciumvar,Ironvar,Cholestertolvar):
    newobject=Food(namevar,pricevar,servingsizevar,kcalvar,carbvar, provar,fatvar,fibervar,sugervar,Avar,Cvar,Calciumvar,Ironvar,Cholestertolvar)
    
def addfood():
    namevar = input('type name: ')
    pricevar = input('type price per serving: ')
    servingsizevar = input('type serving size: ')
    kcalvar = input('type kcal: ')
    carbvar = input('type carb: ')
    provar = input('type protein: ')
    fatvar = input('type fat: ')
    fibervar = input('type fiber: ')
    sugervar = input('type suger: ')
    Avar = input('type vitamin A: ')
    Cvar = input('type vitamin C: ')
    Calciumvar = input('type Calcium: ')
    Ironvar = input('type Iron: ')
    Cholestertolvar = input('type Cholesterol: ')
    newobject=Food(namevar,float(pricevar),float(servingsizevar),float(kcalvar),float(carbvar), float(provar),float(fatvar),float(fibervar),float(sugervar),float(Avar),float(Cvar),float(Calciumvar),float(Ironvar),float(Cholestertolvar))
    
def addmultifood():
    while True:
        addfood()
        #newobject=Food(namevar,pricevar,servingsizevar,kcalvar,provar)
        quiz = input('do you still have food? ')
        if quiz == 'no': break



data.to_csv('food data.csv')

def optimalgrocery(): 
    
    food_items = list(data.index)
    costs = dict(zip(food_items,data['price/serving']))
    servingsize = dict(zip(food_items,data['serving size']))
    calories = dict(zip(food_items,data['kcal']))
    protein = dict(zip(food_items,data['protein']))
    fat = dict(zip(food_items,data['fat']))
    carb = dict(zip(food_items,data['carb']))
    fiber = dict(zip(food_items,data['fiber']))
    suger = dict(zip(food_items,data['suger']))
    A = dict(zip(food_items,data['A']))
    C = dict(zip(food_items,data['C']))
    Calcium = dict(zip(food_items,data['Calcium']))
    Iron = dict(zip(food_items,data['Iron']))
    Cholesterol = dict(zip(food_items,data['Cholesterol']))
    
    #create problem
    prob = plp.LpProblem("Simple Diet Problem",plp.LpMinimize)
    
    #define variables
    food_vars = plp.LpVariable.dicts("name",food_items,lowBound=0,cat= plp.LpContinuous)
    
    #objective funcion
    prob += plp.lpSum([costs[i]*food_vars[i] for i in food_items])
    
    #Set of constraints
    
    prob +=  plp.lpSum([calories[f] * food_vars[f] for f in food_items]) >= 1200.0
    prob +=  plp.lpSum([calories[f] * food_vars[f] for f in food_items]) <= 1800.0
    
    prob +=  plp.lpSum([protein[f] * food_vars[f] for f in food_items]) >= 45
    prob +=  plp.lpSum([protein[f] * food_vars[f] for f in food_items]) <= 80
    
    prob +=  plp.lpSum([fat[f] * food_vars[f] for f in food_items]) >= 45.0
    prob +=  plp.lpSum([fat[f] * food_vars[f] for f in food_items]) <= 77.0
    
    prob +=  plp.lpSum([carb[f] * food_vars[f] for f in food_items]) >= 50.0
    prob +=  plp.lpSum([carb[f] * food_vars[f] for f in food_items]) <= 150.0
    
    prob +=  plp.lpSum([fiber[f] * food_vars[f] for f in food_items]) >= 21.0
    prob +=  plp.lpSum([fiber[f] * food_vars[f] for f in food_items]) <= 30.0
    
    prob +=  plp.lpSum([suger[f] * food_vars[f] for f in food_items]) <= 50
    
    prob +=  plp.lpSum([Cholesterol[f] * food_vars[f] for f in food_items]) <= 150
    prob +=  plp.lpSum([C[f] * food_vars[f] for f in food_items]) >=30
    prob +=  plp.lpSum([Iron[f] * food_vars[f] for f in food_items]) >=30

    #solve    
    prob.solve()
    
    for v in prob.variables():
        if v.varValue>0:
             print(v.name, "=", round(v.varValue,2),'gr')
    
       
    obj =  plp.value(prob.objective)
    print("The total cost of this grocery is: ${}".format(round(obj,2)))
    print("Status:", plp.LpStatus[prob.status])
    
    for chat in data.columns:
        x=0
        for i in food_items:
            x+=food_vars[i].varValue*data[chat].loc[i]
        print(chat,':',round(x,2))  


      

