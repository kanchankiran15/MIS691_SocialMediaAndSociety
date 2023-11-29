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

# extracting data from the dataset for below mentioned variables
time_Spent= df.groupby('Time Spent').size()
occupation_counts = df['Occupation'].value_counts()
age_means = df.groupby('Time Spent')[['Age']].mean().mean(axis=1)
adhd_means = df.groupby('Time Spent')[['ADHD Q1', 'ADHD Q2', 'ADHD Q3', 'ADHD Q4']].mean().mean(axis=1)
anxiety_means = df.groupby('Time Spent')[['Anxiety Q1', 'Anxiety Q2']].mean().mean(axis=1)
self_esteem_means = df.groupby('Time Spent')[['Self Esteem Q1', 'Self Esteem Q2', 'Self Esteem Q3']].mean().mean(axis=1)
depression_means = df.groupby('Time Spent')[['Depression Q1', 'Depression Q2', 'Depression Q3']].mean().mean(axis=1)
# correlation matrix for the dataset
correlation_matrix = df[['ADHD Q1', 'ADHD Q2', 'ADHD Q3', 'ADHD Q4', 'Anxiety Q1', 'Anxiety Q2',
                         'Self Esteem Q1', 'Self Esteem Q2', 'Self Esteem Q3',
                         'Depression Q1', 'Depression Q2', 'Depression Q3']].corr()

sns.set_palette('deep')
#plot the bar-graph
def plot_means(means, title, xlabel, ylabel, filename):

    plt.figure(figsize=(10, 6))
    bars = plt.bar(means.index, means.values)

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

#display correlation matrix and saving into the output folder
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='viridis')
plt.title('Correlation Matrix of Mental Health Scores')
plt.tight_layout()
plt.savefig("output\\"+str(count)+"_"+"correlation_matrix.png")
plt.show()