import pandas as pd
import numpy as np

class StudentDataProcessor:
    def __init__(self, data):
        """Initialize with a Pandas DataFrame."""
        self.df = pd.DataFrame(data)
        self.df['Enrollment_Date'] = pd.to_datetime(self.df['Enrollment_Date'], errors='coerce')  # Ensure datetime format

    def clean_data(self):
        """Fill missing values in 'Age' with the median age, and drop rows with missing 'Math_Score'."""
        # TODO: Fill missing Age values with the median value of Age
        # TODO: Drop rows with missing Math Scores
        # Do not return anything, the modification should be done inplace
        return None

    def add_student(self, name, age, math_score, science_score, enrollment_date):
        """Add a new student record."""
        #TODO: Add a new student to the DataFrame.
        # The operation must be done inplace. Make sure to convert the enrollment_date to datetime format
        return None

    def compute_average_scores(self):
        """Create a new column 'Average_Score' as the mean of 'Math_Score' and 'Science_Score'."""
        #TODO: Create a new column Average_Score inplace.
        return None

    def best_students(self, subject, n):
        """Return top 'n' students based on the given subject ('Math_Score' or 'Science_Score' or 'Average_Score')."""
        return #TODO: Return the names of the top-n students for the given subject

    def group_by_age(self):
        """Return the average scores grouped by Age."""
        return #TODO: Return average score grouped by Age

    def filter_passing_students(self, threshold=50):
        """Return students who passed both subjects (scores above threshold)."""
        return #TODO

    def merge_with_extra_data(self, extra_df):
        """Merge the current DataFrame with extra_df on the 'Name' column (left join)."""
        #TODO: Modify inplace
        return None

    def apply_bonus(self, bonus_function):
        """Apply bonus_function to both 'Math_Score' and 'Science_Score' and update the 'Average_Score' accordingly."""
        #TODO: Modify inplace
        return None

    def students_per_year(self):
        """Return the number of students enrolled per year."""
        return #TODO

    def rank_students(self):
        """Rank students based on their Average_Score."""
        #TODO: Create a new column named "Rank" and assign a Rank to each student based on Average_Score.
        # In case the scores are same, assign the Rank based on Age. 
        return None

    def yearly_performance(self):
        """Calculate the yearly average performance of students."""
        return #TODO: Compute average of Average_Score for each year 
    
    def normalize_scores(self):
        """Normalize scores between 0 and 1 using Min-Max Scaling."""
        #TODO: Normalize Math_Score, Science_Score independently 
        # TODO: Then update Average_Score based on these normalized scores
        return None


if __name__ == main():
    # Sample Data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [18, 19, 18, 20, np.nan],
        'Math_Score': [85, 78, 92, 70, 88],
        'Science_Score': [90, 76, 88, 65, 82],
        'Enrollment_Date': ['2020-09-01', '2019-08-15', '2020-09-01', '2018-07-10', '2019-08-15']
    }
    
    #Sample for extra_data used in merge_with_extra_data
    extra_data = pd.DataFrame({
        'Name': ['Alice', 'Charlie', 'Eve'],
        'Club': ['Robotics', 'Chess', 'Debate']
    })
