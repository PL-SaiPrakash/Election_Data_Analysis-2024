import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel('combined_report.xlsx')

# Convert columns to numeric, forcing errors to NaN
df['Total Votes'] = pd.to_numeric(df['Total Votes'], errors='coerce')
df['Margin'] = pd.to_numeric(df['Margin'], errors='coerce')

# Drop rows with NaN values in numeric columns if necessary
df = df.dropna(subset=['Total Votes', 'Margin'])

# Descriptive statistics
total_votes_stats = df['Total Votes'].describe()
margin_stats = df['Margin'].describe()

# Party analysis
party_performance = df['Party Name'].value_counts()
party_vote_share = df.groupby('Party Name')['Total Votes'].mean()
party_margin = df.groupby('Party Name')['Margin'].mean()

# Candidate analysis
top_performers = df.nlargest(5, 'Total Votes')
close_contests = df.nsmallest(5, 'Margin')

# Print the results
print("Total Votes Statistics:\n", total_votes_stats)
print("\nMargin Statistics:\n", margin_stats)
print("\nParty Performance:\n", party_performance)
print("\nParty Vote Share:\n", party_vote_share)
print("\nParty Margin:\n", party_margin)
print("\nTop Performers:\n", top_performers)
print("\nClose Contests:\n", close_contests)

# Visualization
sns.set(style="whitegrid")

# Bar chart for Party Performance
plt.figure(figsize=(10, 6))
sns.barplot(x=party_performance.index, y=party_performance.values, palette="viridis")
plt.title('Number of Constituencies Won by Each Party')
plt.xlabel('Party Name')
plt.ylabel('Number of Constituencies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram for Total Votes
plt.figure(figsize=(10, 6))
sns.histplot(df['Total Votes'], bins=20, kde=True, color='blue')
plt.title('Distribution of Total Votes')
plt.xlabel('Total Votes')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Histogram for Margin
plt.figure(figsize=(10, 6))
sns.histplot(df['Margin'], bins=20, kde=True, color='green')
plt.title('Distribution of Winning Margins')
plt.xlabel('Winning Margin')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Pie chart for Party Vote Share
plt.figure(figsize=(10, 6))
party_vote_share.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='viridis')
plt.title('Average Vote Share of Each Party')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Bar chart for Party Margin
plt.figure(figsize=(10, 6))
sns.barplot(x=party_margin.index, y=party_margin.values, palette="magma")
plt.title('Average Winning Margin by Each Party')
plt.xlabel('Party Name')
plt.ylabel('Average Winning Margin')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
