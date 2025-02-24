import numpy as np
import pandas as pd
from task2 import StudentDataProcessor 

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

processor = StudentDataProcessor(data)
failed = 0

try:
    assert processor.df.shape == (5, 5)
except:
    failed += 1
    print('.shape test failed')

try:
    processor.clean_data()
    assert processor.df['Age'].isnull().sum() == 0  # No NaN values in Age
    assert processor.df['Math_Score'].isnull().sum() == 0  # No NaN values in Math_Score
except:
    failed += 1
    print('.clean_data test failed')

try:
    processor.add_student('Frank', 21, 85, 90, '2021-09-01')
    assert processor.df.shape[0] == 6  
except:
    failed += 1
    print('.add_student test failed')

try:
    processor.compute_average_scores()
    assert 'Average_Score' in processor.df.columns  
except:
    failed += 1
    print('.compute_average_scores test failed')

try:
    top_students = processor.best_students('Math_Score', 2)
    assert top_students.shape[0] == 2  
except:
    failed += 1
    print('.best_students test failed')

try:
    grouped = processor.group_by_age()
    assert isinstance(grouped, pd.DataFrame)  
except:
    failed += 1
    print('.group_by_age test failed')

try:
    passing_students = processor.filter_passing_students(threshold=75)
    assert isinstance(passing_students, pd.DataFrame)
    assert passing_students.shape[0] == processor.df.shape[0] - 1 #Only David Failed
except:
    failed += 1
    print('.filter_passing_students test failed')

try:
    processor.merge_with_extra_data(extra_data)
    assert 'Club' in processor.df.columns 
except:
    failed += 1
    print('.merge_with_extra_data test failed')

try:
    processor.apply_bonus(lambda x: x * 1.1)
except:
    failed += 1
    print('.apply_bonus test failed')

try:
    students_per_year = processor.students_per_year()
    assert isinstance(students_per_year, pd.Series)  
except:
    failed += 1
    print('.students_per_year test failed')

try:
    processor.rank_students()
    assert 'Rank' in processor.df.columns  
except:
    failed += 1
    print('.rank_students test failed')

try:
    yearly_perf = processor.yearly_performance()
    assert isinstance(yearly_perf, pd.DataFrame)  
except:
    failed += 1
    print('.yearly_performance test failed')

try:
    processor.normalize_scores()
    assert processor.df['Math_Score'].max() <= 1 and processor.df['Math_Score'].min() >= 0
    assert processor.df['Science_Score'].max() <= 1 and processor.df['Science_Score'].min() >= 0
except:
    failed += 1
    print('.normalize_scores test failed')

if failed == 0:
    print('All methods evaluated successfully')