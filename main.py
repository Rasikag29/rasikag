import pandas as pd
import matplotlib.pyplot as plt
import time

#Read and get the Excel file into a DataFrame
get_data=pd.ExcelFile('subjectcode.xlsx')
df = pd.read_excel(get_data, sheet_name='Sheet1')

#get Group name as input
Group_name=str(input("Enter the group name:"))
#to get headings of each coulmn
colum_headings = " | ".join(df.columns)
print(colum_headings)
#check if the group name exists in the excel or not
if Group_name in df['Group Name'].values.tolist():
    row_index=df.index[df['Group Name']== Group_name].tolist()[0]
    row_value=df.iloc[row_index].values.tolist()
    print(row_value)
else:
    print("Given Correct Group Name !!!!!!!!!!!!!!")
#check if the group name exists in the excel or not
a=input("Do you want to show your Eligibity criteria : ")
if(a=="yes"):
    if Group_name in df['Group Name'].values.tolist():
        row_index=df.index[df['Group Name']== Group_name].tolist()[0]
        colum_limit=2
        row_value=df.iloc[row_index,:colum_limit].values.tolist()
        print("Group Name and code :",row_value)
        colum_start=2
        colum_limit=3
        row_value=df.iloc[row_index,colum_start:colum_limit].values.tolist()
        print("Subject in the Group : ",row_value)
        colum_start = 3
        colum_limit = 5
        row_value = df.iloc[row_index, colum_start:colum_limit].values.tolist()
        print("Bachelor of Science and Years : ", row_value)
        colum_start = 5
        colum_limit = 7
        row_value = df.iloc[row_index, colum_start:colum_limit].values.tolist()
        print("Bachelor of Engineering and Years:", row_value)
        colum_start = 7
        colum_limit = 9
        row_value = df.iloc[row_index, colum_start:colum_limit].values.tolist()
        print("Bachelor of Commerce and Years :", row_value)
else:
    print(" You entered No as a input ")
#pylot all the graph for Bachelor Degree
graph=input("ENTER THE CHART NAME:  ")
#plot the scatter graph
if(graph =='scatter'):
    categories = ['Bachelor of Science', 'Bachelor of Engineering ', 'Bachelor of Commerce']
    opportunity = [72, 10, 36]
    plt.scatter(categories,opportunity,color='blue',marker='o',label="Fixed label")
    plt.xlabel('categories')
    plt.ylabel('opportunity')
    plt.title(' Bachelor Degree Opportunity')
    plt.legend()
    time.sleep(3)
    plt.show()
#plot the pie graph
elif(graph =='pie'):
    categories = ['Bachelor of Science', 'Bachelor of Engineering ', 'Bachelor of Commerce']
    opportunity= [72, 10, 36]
    plt.figure(figsize=(6, 6))  # Adjust the figure size if needed
    plt.pie(opportunity, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title(' Bachelor Degree Opportunity')
    time.sleep(3)
    plt.show()
#plot the bar graph
elif(graph=='bar'):
    categories = ['Bachelor of Science', 'Bachelor of Engineering ', 'Bachelor of Commerce']
    opportunity= [72, 10, 36]
    plt.bar(categories,opportunity)
    plt.xlabel('categories')
    plt.ylabel('opportunity')
    plt.title("Bachelor Degree Oppurunity")
    time.sleep(3)
    plt.show()
#plot the  line graph
elif(graph=='line'):
    categories = ['Bachelor of Science', 'Bachelor of Engineering ', 'Bachelor of Commerce']
    opportunity= [72, 10, 36]
    plt.plot(categories,opportunity,marker="o",linestyle='-',color='green',label='Fixed Data')
    plt.xlabel('categories')
    plt.ylabel('opportunity')
    plt.title("Bachelor Degree Oppurunity")
    plt.legend()
    time.sleep(3)
    plt.show()
else:
    print("You Entered the wrong input!!!!!!!")

