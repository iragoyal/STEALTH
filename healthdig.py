
# Importing the libraries
from tkinter import *
from tkinter import messagebox                           
import os            
import webbrowser
import numpy as np
import pandas as pd

d='./dataset/'

class HyperlinkManager:
      
    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="blue", underline=1)
        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return

# Importing the dataset
training_dataset = pd.read_csv(d+'Training.csv')
test_dataset = pd.read_csv(d+'Testing.csv')

# Slicing and Dicing the dataset to separate features from predictions
X = training_dataset.iloc[:, 0:132].values
Y = training_dataset.iloc[:, -1].values

# Dimensionality Reduction for removing redundancies
dimensionality_reduction = training_dataset.groupby(training_dataset['prognosis']).max()

# Encoding String values to integer constants
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
y = labelencoder.fit_transform(Y)

# Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Implementing the Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Saving the information of columns
cols     = training_dataset.columns
cols     = cols[:-1]

# Checking the Important features
importances = classifier.feature_importances_
indices = np.argsort(importances)[::-1]
features = cols

# Implementing the Visual Tree
from sklearn.tree import _tree

# Method to simulate the working of a Chatbot by extracting and formulating questions
def print_disease(node):
        #print(node)
        node = node[0]
        #print(len(node))
        val  = node.nonzero() 
        #print(val)
        disease = labelencoder.inverse_transform(val[0])
        return disease
def recurse(node, depth):
            global val,ans
            global tree_,feature_name,symptoms_present
            indent = "  " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                yield name + " ?"
                
#                ans = input()
                ans = ans.lower()
                if ans == 'yes':
                    val = 1
                else:
                    val = 0
                if  val <= threshold:
                    yield from recurse(tree_.children_left[node], depth + 1)
                else:
                    symptoms_present.append(name)
                    yield from recurse(tree_.children_right[node], depth + 1)
            else:
                strData=""
                present_disease = print_disease(tree_.value[node])
#                print( "You may have " +  present_disease )
#                print()
                strData="You may have :" +  str(present_disease)
               
                QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
                
                red_cols = dimensionality_reduction.columns 
                symptoms_given = red_cols[dimensionality_reduction.loc[present_disease].values[0].nonzero()]
#                print("symptoms present  " + str(list(symptoms_present)))
#                print()
                strData="symptoms present:  " + str(list(symptoms_present))
                QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
#                print("symptoms given "  +  str(list(symptoms_given)) )  
#                print()
                strData="symptoms given: "  +  str(list(symptoms_given))
                QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
                confidence_level = (1.0*len(symptoms_present))/len(symptoms_given)
#                print("confidence level is " + str(confidence_level))
#                print()
                strData="confidence level is: " + str(confidence_level)
                QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
#                print('The model suggests:')
#                print()
                strData='The model suggests:'
                QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
                row = doctors[doctors['disease'] == present_disease[0]]
#                print('Consult ', str(row['name'].values))
#                print()
                strData='Consult '+ str(row['name'].values)
                QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
#                print('Visit ', str(row['link'].values))
                #print(present_disease[0])
                hyperlink = HyperlinkManager(QuestionDigonosis.objRef.txtDigonosis)
                strData='Visit '+ str(row['link'].values[0])
                def click1():
                    webbrowser.open_new(str(row['link'].values[0]))
                QuestionDigonosis.objRef.txtDigonosis.insert(INSERT, strData, hyperlink.add(click1))
                #QuestionDigonosis.objRef.txtDigonosis.insert(END,str(strData)+'\n')                  
                yield strData
        
def tree_to_code(tree, feature_names):
        global tree_,feature_name,symptoms_present
        tree_ = tree.tree_
        #print(tree_)
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]
        #print("def tree({}):".format(", ".join(feature_names)))
        symptoms_present = []   
#        recurse(0, 1)
    

def execute_bot():
#    print("Please reply with yes/Yes or no/No for the following symptoms")    
    tree_to_code(classifier,cols)



# This section of code to be run after scraping the data

doc_dataset = pd.read_csv(d+'doctors_dataset.csv', names = ['Name', 'Description'])


diseases = dimensionality_reduction.index
diseases = pd.DataFrame(diseases)

doctors = pd.DataFrame()
doctors['name'] = np.nan
doctors['link'] = np.nan
doctors['disease'] = np.nan

doctors['disease'] = diseases['prognosis']


doctors['name'] = doc_dataset['Name']
doctors['link'] = doc_dataset['Description']

record = doctors[doctors['disease'] == 'AIDS']
record['name']
record['link']




# Execute the bot and see it in Action
#execute_bot()


class QuestionDigonosis(Frame):
    objIter=None
    objRef=None
    def __init__(self,master=None):
        master.title("Physical Health")
        master.geometry("900x359")
        master.resizable(0,0)
        QuestionDigonosis.objRef=self
        super().__init__(master=master)
        self["bg"]="gray10"
        self.createWidget()
        self.iterObj=None

    def createWidget(self):
        def openf():
          
            import mentalhealth
            
        self.lblQuestion=Label(self,text="Question",width=12,bg="bisque")
        self.lblQuestion.grid(row=0,column=0,rowspan=4)

        self.lblDigonosis = Label(self, text="Digonosis",width=12,bg="bisque")
        self.lblDigonosis.grid(row=4, column=0,sticky="n",pady=5)

        # self.varQuestion=StringVar()
        self.txtQuestion = Text(self, width=100,height=4)
        self.txtQuestion.grid(row=0, column=1,rowspan=4,columnspan=20)

        self.varDiagonosis=StringVar()
        self.txtDigonosis =Text(self, width=100,height=14)
        self.txtDigonosis.grid(row=4, column=1,columnspan=20,rowspan=20,pady=5)

        self.btnNo=Button(self,text="Open AI Mental Health Bot",width=32,bg="bisque", command=openf)
        self.btnNo.place(x=340,y=320)
        
        self.btnNo=Button(self,text="No",width=12,bg="bisque", command=self.btnNo_Click)
        self.btnNo.grid(row=25,column=0)
        self.btnYes = Button(self, text="Yes",width=12,bg="bisque", command=self.btnYes_Click)
        self.btnYes.grid(row=25, column=1,columnspan=20,sticky="e")

        self.btnClear = Button(self, text="Clear",width=12,bg="bisque", command=self.btnClear_Click)
        self.btnClear.grid(row=27, column=0)
        self.btnStart = Button(self, text="Start",width=12,bg="bisque", command=self.btnStart_Click)
        self.btnStart.grid(row=27, column=1,columnspan=20,sticky="e")
    def btnNo_Click(self):
        global val,ans
        global val,ans
        ans='no'
        str1=QuestionDigonosis.objIter.__next__()
        self.txtQuestion.delete(0.0,END)
        self.txtQuestion.insert(END,str1+"\n")
        
    def btnYes_Click(self):
        global val,ans
        ans='yes'
        self.txtDigonosis.delete(0.0,END)
        str1=QuestionDigonosis.objIter.__next__()
        
#        self.txtDigonosis.insert(END,str1+"\n")
        
    def btnClear_Click(self):
        self.txtDigonosis.delete(0.0,END)
        self.txtQuestion.delete(0.0,END)
    def btnStart_Click(self):
        execute_bot()
        self.txtDigonosis.delete(0.0,END)
        self.txtQuestion.delete(0.0,END)
        self.txtDigonosis.insert(END,"Please Click on Yes or No for the Above symptoms in Question")                  
        QuestionDigonosis.objIter=recurse(0, 1)
        str1=QuestionDigonosis.objIter.__next__()
        self.txtQuestion.insert(END,str1+"\n")


class MainForm(Frame):
    main_rooth = None

    def __init__(self, master=None):
        MainForm.main_rooth = master
        super().__init__(master=master)
        a = QuestionDigonosis(MainForm.main_rooth)
        a.pack()

rooth = Tk()
frmMainForm=MainForm(rooth)
frmMainForm.pack()
rooth.mainloop()


