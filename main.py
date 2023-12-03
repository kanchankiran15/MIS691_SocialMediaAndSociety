import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Read csv file
df = pd.read_csv('data\\smmh.csv')
count=1

#define the x-axis values in graph  time-wise
time_order = [
    'Less than an Hour', 'Between 1 and 2 hours', 'Between 2 and 3 hours',
    'Between 3 and 4 hours', 'Between 4 and 5 hours', 'More than 5 hours'
]
#sorting according to above time order
df['Time Spent'] = pd.Categorical(df['Time Spent'], categories=time_order, ordered=True)

threshold = 4  # This is arbitrary and for demonstration purposes.

# Calculate the average score across the mental health-related questions
mental_health_cols = ['ADHD Q1', 'ADHD Q2', 'ADHD Q3', 'ADHD Q4',
                      'Anxiety Q1', 'Anxiety Q2', 'Self Esteem Q1', 'Self Esteem Q2', 'Self Esteem Q3',
                      'Depression Q1', 'Depression Q2', 'Depression Q3']
df['Average Mental Health Score'] = df[mental_health_cols].mean(axis=1)

# Based on the average score, determine if a mental health check-up is recommended
df['Outcome'] = df['Average Mental Health Score'].apply(lambda x: 'Type 3' if x >= threshold else ('Type 2' if x>3 and x<4 else 'Type 1'))

# extracting data from the dataset for below mentioned variables
outcome_counts = df['Outcome'].value_counts()
time_Spent= df.groupby('Time Spent').size()
occupation_counts = df['Occupation'].value_counts()
age_means = df.groupby('Time Spent')[['Age']].mean().mean(axis=1)
adhd_means = df.groupby('Time Spent')[['ADHD Q1', 'ADHD Q2', 'ADHD Q3', 'ADHD Q4']].mean().mean(axis=1)
anxiety_means = df.groupby('Time Spent')[['Anxiety Q1', 'Anxiety Q2']].mean().mean(axis=1)
self_esteem_means = df.groupby('Time Spent')[['Self Esteem Q1', 'Self Esteem Q2', 'Self Esteem Q3']].mean().mean(axis=1)
depression_means = df.groupby('Time Spent')[['Depression Q1', 'Depression Q2', 'Depression Q3']].mean().mean(axis=1)
# correlation matrix for the dataset
correlation_cols = ['Age', 'ADHD Score', 'Anxiety Score', 'Self Esteem Score', 'Depression Score', 'Total Score', 'Outcome']

df['ADHD Score'] = df[['ADHD Q1', 'ADHD Q2', 'ADHD Q3', 'ADHD Q4']].mean(axis=1)
df['Anxiety Score'] = df[['Anxiety Q1', 'Anxiety Q2']].mean(axis=1)
df['Self Esteem Score'] = df[['Self Esteem Q1', 'Self Esteem Q2', 'Self Esteem Q3']].mean(axis=1)
df['Depression Score'] = df[['Depression Q1', 'Depression Q2', 'Depression Q3']].mean(axis=1)
df['Total Score'] = df[['ADHD Score', 'Anxiety Score', 'Self Esteem Score', 'Depression Score']].sum(axis=1)
df['Outcome'] = pd.factorize(df['Outcome'])[0] + 1
correlation_matrix = df[correlation_cols].corr()                                          
                                                

sns.set_palette('deep')
#plot the bar-graph
def plot_means(means, title, xlabel, ylabel, filename):

    plt.figure(figsize=(10, 6))
    bars = plt.bar(means.index, means.values)
    total = sum(means.values)
    if(xlabel=='Outcome' or ylabel=='Age'):
        highest_value = means.min()
        lowest_value = means.max()
    else:
        highest_value = means.max()
        lowest_value = means.min()    

    for bar in bars:
        if bar.get_height() == highest_value:
            bar.set_color('red')
            bar.set_edgecolor('black')
            bar.set_linewidth(2)
        elif bar.get_height() == lowest_value:
            bar.set_color('green')
            bar.set_edgecolor('black')
            bar.set_linewidth(2)
        percentage = f'{(bar.get_height() / total):.1%}'
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), percentage,
                 ha='center', va='bottom', color='black')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)

    plt.tight_layout()
    #saving the graph in output folder
    plt.savefig("output\\"+f"{filename}.png")
    #diplay the graph
    plt.show()

#plot the pie-chart
def plotPie(data, title, filename):
    plt.figure(figsize=(10, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
    plt.title(title)
    #saving the chart in output folder
    plt.savefig("output\\"+f"{filename}.png")
    #diplay the chart
    plt.show()

#plotting the graph and chart by calling above functions- plot_means,plotPie
plot_means(outcome_counts, 'Distribution of Outcome for Mental Health Check-up Recommendation', 'Outcome', 'Number of Participants', str(count)+"_"+'Mental_Health_Check_up_Recommendation')
count=count+1
plot_means(time_Spent, 'Time Spent on Social Media', 'Time Spent', 'Frequency', str(count)+"_"+'Time_Spent_on_Social_Media')
count=count+1
plotPie(occupation_counts, 'Distribution of data based on their Occupation.', str(count)+"_"+'Distribution_Occupation')
count=count+1
plot_means(age_means, 'Time Spent on Social Media by Age', 'Time Group', 'Age', str(count)+"_"+'Time_Spent_on_Social_Media_By_Age')
count=count+1
plot_means(adhd_means, 'Mean ADHD Score by Time Group', 'Time Spent', 'Mean ADHD Score', str(count)+"_"+'adhd_means')
count=count+1
plot_means(anxiety_means, 'Mean Anxiety Score by Time Group', 'Time Spent', 'Mean Anxiety Score', str(count)+"_"+'anxiety_means')
count=count+1
plot_means(self_esteem_means, 'Mean Self Esteem Score by Time Group', 'Time Spent', 'Mean Self Esteem Score', str(count)+"_"+'self_esteem_means')
count=count+1
plot_means(depression_means, 'Mean Depression Score by Time Group', 'Time Spent', 'Mean Depression Score', str(count)+"_"+'depression_means')
count=count+1

dataCorr=pd.read_csv('data\\smmh.csv')

ADHD = ['ADHD Q1', 'ADHD Q2', 'ADHD Q3', 'ADHD Q4']
dataCorr['ADHD Score'] = df[ADHD].sum(axis=1)

Anxiety = ['Anxiety Q1', 'Anxiety Q2']
dataCorr['Anxiety Score'] = df[Anxiety].sum(axis=1)

SelfEsteem = ['Self Esteem Q1', 'Self Esteem Q2','Self Esteem Q3']
dataCorr['Self Esteem Score'] = df[SelfEsteem].sum(axis=1)

Depression = ['Depression Q1', 'Depression Q2','Depression Q3']
dataCorr['Depression Score'] = df[Depression].sum(axis=1)

Total = ['ADHD Score', 'Anxiety Score','Self Esteem Score','Depression Score']
dataCorr['Total Score'] = df[Total].sum(axis=1)


#display correlation matrix and saving into the output folder
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='viridis')
plt.title('Correlation Matrix of Mental Health Scores')
plt.tight_layout()
plt.xticks(rotation=45)
plt.yticks(rotation=45)                      
                       
plt.savefig("output\\"+str(count)+"_"+"correlation_matrix.png")
plt.show()
