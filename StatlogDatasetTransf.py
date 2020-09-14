import pandas as pd
import random  
import sys 
#sys.path.append("E:/Google Drive/PC SHIT/HMMY/Diplomatiki/methods/MCDA")
#from  Pyth.UTASTAR import *


# UTASTAR EXAMPLE
# the separation threshold

epsilon = 0.1

### German Credit Card Approval Dataset
# Use Utastar to create Credit Score
# 20 criteria we can use the value functions the will be created for feautre reduction

df = pd.read_excel(
    r"C:\Users\amichail\OneDrive - Raycap\Dokumente\Thes\german credit score dataset UCI\multicriteria matrix.xlsx",
    sheet_name="main",
    #sheet_name="multimatrix",
)
# Data Processing


# Set correct column names from import
df.columns = df.iloc[0]

# Remove junk row,column
df = df.iloc[1:, 1:]

df["purpose"].replace("Α40 ", "11", regex=True, inplace=True)
# df["purpose"].replace('Α410','10',regex=True,inplace=True)
#df.iloc[15]

# Change qualitative values to quantitative
df.replace("(.)(?!$)", "", regex=True, inplace=True)

# Per columnc change values if needed
# Replace true zero

df["check_account"].replace("4", "0", regex=True, inplace=True)
df["savings_account"].replace("5", "0", regex=True, inplace=True)
df["employment"].replace("1", "0", regex=True, inplace=True)
df["debtors_guarantors"].replace("1", "0", regex=True, inplace=True)
df["property"].replace("4", "0", regex=True, inplace=True)
df["installment_plans"].replace("3", "0", regex=True, inplace=True)
df["job"].replace("1", "0", regex=True, inplace=True)
df["telephone"].replace("1", "0", regex=True, inplace=True)


# Remove index column if needed
# df = df.set_index(list(df)[0])

# Set index name
df.columns.name = "Alternatives"


# Reset index
df = df.reset_index(drop=True)

# Convert all dataframe values to integer
df = df.apply(pd.to_numeric)

#choose good values with good distribution 
#######VAR#########
# temp = pd.DataFrame() 
# temp["Var"] = df.var(axis = 1)
# temp = temp.sort_values("Var")
# nr = temp.index.values
# nr = nr[600:]

#####std########
# temp = df.transpose().describe()
# temp = temp.transpose()
# temp = temp.sort_values('std')
# nr = temp.index.values
# nr = nr[210:690]

#### random #####
#nr = random.sample(range(1000),100)


#480 best solution or first 100 from other sheet 
#### first 100

nr= [x for x in range(480)]
df= df.iloc[nr,:]
df = df.drop(["telephone"],axis=1)
df = df.drop(["foreign"],axis=1)
df = df.drop(["providor_num"],axis=1)



#classdf = df
# the performance table
# removing the class column
performanceTable = df.iloc[:,:-1] # -3
print("\nPerformance Table \n", performanceTable)

# ranks of the alternatives

data = df["Class"].values  
rownames = performanceTable.index.values
alternativesRanks = pd.DataFrame([data], columns=rownames)
print("\nAlternative Ranks\n", alternativesRanks)

#Find min breakpoint block 
""" 
k=0
minoptimum = 10 
while True:

# criteria to minimize or maximize
choices = ["max","min"]
minmaxdata = [random.choice(choices) for i in range(df.shape[1]-1)]
 """

#minmaxdata = ['max' for i in range(20)]
minmaxdata = ["max","min","max","min", "max","max","max","max", "max","max","min","max",  "min","min","max","max", "max"]#,"min","max","min"]

#minmaxdata = ['min','min','max','max','min','min','max','min','min','max','min','max','max','max','max','max','max','min','max','min']

columnnames = performanceTable.columns.values
criteriaMinMax = pd.DataFrame([minmaxdata], columns=columnnames)
print("\nCriteria Min Max \n", criteriaMinMax,) 


#bpdata = [4, 3, 3, 4, 4 , 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 2, 4, 4, 3, 3]
bpdata = [3,4,3,3, 3,3,3,4, 3,3,3,3, 4,3,3,3, 3]#,2,2,2]
#bpdata = [3 for i in range(20)]

#choices = [2,3,4]
#bpdata = [random.choice(choices) for i in range(df.shape[1]-1)]

# number of break points for each criterion
criteriaNumberOfBreakPoints = pd.DataFrame(
    [bpdata],
    columns=performanceTable.columns.values,
)
# print("\nCriteriaNumofBP\n", criteriaNumberOfBreakPoints)