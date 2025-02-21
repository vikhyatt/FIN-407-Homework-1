import pandas as pd
import numpy as np

class StudentDataProcessor:
    def __init__(self, data):
        """Initialize with a Pandas DataFrame."""
        self.df = pd.DataFrame(data)
        self.df['Enrollment_Date'] = pd.to_datetime(self.df['Enrollment_Date'], errors='coerce')  # Ensure datetime format

    def clean_data(self):
        """Fill missing values in 'Age' with the median age, and drop rows with missing 'Math_Score'."""
        self.df['Age'] = self.df['Age'].fillna(__________)  # TODO: Fill with median
        self.df.dropna(subset=['Math_Score'], inplace=True)  # Drop missing Math Scores

    def add_student(self, name, age, math_score, science_score, enrollment_date):
        """Add a new student record."""
        new_student = pd.DataFrame([{
            'Name': name,
            'Age': age,
            'Math_Score': math_score,
            'Science_Score': science_score,
            'Enrollment_Date': pd.to_datetime(enrollment_date)
        }])
        self.df = pd.concat([self.df, new_student], ignore_index=True)  # Append new student

    def compute_average_scores(self):
        """Create a new column 'Average_Score' as the mean of 'Math_Score' and 'Science_Score'."""
        self.df['Average_Score'] = self.df[['Math_Score', 'Science_Score']].mean(axis=1)

    def best_students(self, subject, n=3):
        """Return top 'n' students based on the given subject ('Math_Score' or 'Science_Score')."""
        return self.df.nlargest(n, subject)  # Get top n rows

    def group_by_age(self):
        """Return the average scores grouped by Age."""
        return self.df.groupby('Age')[['Math_Score', 'Science_Score']].mean()

    def filter_passing_students(self, threshold=50):
        """Return students who passed both subjects (scores above threshold)."""
        return self.df[(self.df['Math_Score'] > threshold) & (self.df['Science_Score'] > threshold)]

    def merge_with_extra_data(self, extra_df):
        """Merge the current DataFrame with extra_df on the 'Name' column (left join)."""
        self.df = pd.merge(self.df, extra_df, on='Name', how='left')

    def pivot_scores(self):
        """Return a pivot table with 'Name' as index and subjects as columns."""
        return self.df.pivot_table(values=['Math_Score', 'Science_Score'], index='Name')

    def apply_bonus(self, bonus_function):
        """Apply a bonus function to both 'Math_Score' and 'Science_Score'."""
        self.df[['Math_Score', 'Science_Score']] = self.df[['Math_Score', 'Science_Score']].apply(bonus_function)

    def calculate_rolling_average(self, window=3):
        """Calculate a rolling average of scores for students with repeated test scores."""
        self.df[['Math_Score', 'Science_Score']] = self.df[['Math_Score', 'Science_Score']].rolling(window=window, min_periods=1).mean()

    def students_per_year(self):
        """Return the number of students enrolled per year."""
        return self.df['Enrollment_Date'].dt.year.value_counts().sort_index()

    def create_multi_index(self):
        """Set a MultiIndex with 'Enrollment_Date' and 'Name'."""
        self.df.set_index(['Enrollment_Date', 'Name'], inplace=True)

    def fill_missing_scores(self):
        """Fill missing scores with the average score of that subject."""
        for col in ['Math_Score', 'Science_Score']:
            self.df[col] = self.df[col].fillna(self.df[col].mean())  # Fill missing scores

    def rank_students(self):
        """Rank students based on their Average_Score."""
        self.df['Rank'] = self.df['Average_Score'].rank(method='dense', ascending=False)

    def advanced_filtering(self):
        """Return students who are in the top 20% of the class."""
        threshold = self.df['Average_Score'].quantile(0.8)
        return self.df[self.df['Average_Score'] >= threshold]

    def yearly_performance(self):
        """Calculate the yearly average performance of students."""
        return self.df.groupby(self.df['Enrollment_Date'].dt.year)[['Math_Score', 'Science_Score']].mean()
    
    def normalize_scores(self):
        """Normalize scores between 0 and 1 using Min-Max Scaling."""
        for col in ['Math_Score', 'Science_Score']:
            self.df[col] = (self.df[col] - self.df[col].min()) / (self.df[col].max() - self.df[col].min())

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 19, 18, 20, np.nan],
    'Math_Score': [85, 78, 92, 70, 88],
    'Science_Score': [90, 76, 88, 65, 82],
    'Enrollment_Date': ['2020-09-01', '2019-08-15', '2020-09-01', '2018-07-10', '2019-08-15']
}

extra_data = pd.DataFrame({
    'Name': ['Alice', 'Charlie', 'Eve'],
    'Club': ['Robotics', 'Chess', 'Debate']
})

# Example Usage:
processor = StudentDataProcessor(data)
processor.clean_data()
processor.add_student("Frank", 21, 80, 75, "2021-06-20")
processor.compute_average_scores()
processor.rank_students()

print("Ranked Students:\n", processor.df)
print("Students Per Year:\n", processor.students_per_year())
print("Top 20% Students:\n", processor.advanced_filtering())
print("Yearly Performance:\n", processor.yearly_performance())