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

clean_data = {
     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 19, 18, 20, 18.5],
    'Math_Score': [85, 78, 92, 70, 88],
    'Science_Score': [90, 76, 88, 65, 82],
    'Enrollment_Date': ['2020-09-01', '2019-08-15', '2020-09-01', '2018-07-10', '2019-08-15'],
}

yearly_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 19, 18, 20, 18.5],
    'Math_Score': [85, 78, 92, 70, 88],
    'Science_Score': [90, 76, 88, 65, 82],
    'Enrollment_Date': ['2020-09-01', '2019-08-15', '2020-09-01', '2018-07-10', '2019-08-15'],
    'Average_Score': [87.5, 77.0, 90.0, 67.5, 85.0],
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
    assert processor.df.iloc[4]['Age'] == 18.5
    assert processor.df['Age'].isnull().sum() == 0  # No NaN values in Age
    assert processor.df['Math_Score'].isnull().sum() == 0  # No NaN values in Math_Score
except:
    failed += 1
    print('.clean_data test failed')


processor = StudentDataProcessor(clean_data)
try:
    processor.add_student('Frank', 21, 85, 90, '2021-09-01')
    assert processor.df.shape[0] == 6  
    assert processor.df.iloc[-1]['Age'] == 21
    assert processor.df.iloc[-1]['Name'] == 'Frank'
    assert processor.df.iloc[-1]['Math_Score'] == 85
    assert processor.df.iloc[-1]['Science_Score'] == 90
except:
    failed += 1
    print('.add_student test failed')


processor = StudentDataProcessor(clean_data)

try:
    processor.compute_average_scores()
    assert 'Average_Score' in processor.df.columns 
    assert processor.df['Average_Score'].sort_values().to_list() == [67.5, 77.0, 85.0, 87.5, 90.0]
except:
    failed += 1
    print('.compute_average_scores test failed')

processor = StudentDataProcessor(clean_data)
try:
    df_reference = pd.DataFrame({
    'Name': ['Charlie', 'Eve'],
    'Age': [18.0, 18.5],
    'Math_Score': [92, 88],
    'Science_Score': [88, 82],
    'Enrollment_Date': ['2020-09-01', '2019-08-15']
    })
    df_reference['Enrollment_Date'] = pd.to_datetime(df_reference['Enrollment_Date'])

    top_students = processor.best_students('Math_Score', 2)
    assert top_students.shape[0] == 2  
    assert top_students.reset_index(drop=True).equals(df_reference)
except:
    failed += 1
    print('.best_students test failed')

processor = StudentDataProcessor(yearly_data)
try:
    df_reference = pd.DataFrame({
        'Math_Score': [88.5, 88.0, 78.0, 70.0],
        'Science_Score': [89.0, 82.0, 76.0, 65.0],
        'Average_Score': [88.75, 85.00, 77.00, 67.50]
    }, index=[18.0, 18.5, 19.0, 20.0])
    grouped = processor.group_by_age()
    assert isinstance(grouped, pd.DataFrame)  
    assert grouped.equals(df_reference)
except:
    failed += 1
    print('.group_by_age test failed')

processor = StudentDataProcessor(clean_data)
try:
    passing_students = processor.filter_passing_students(threshold=75)
    assert isinstance(passing_students, pd.DataFrame)
    assert passing_students.shape[0] == processor.df.shape[0] - 1 #Only David Failed
    assert (passing_students["Math_Score"] > 75).all()
    assert (passing_students["Science_Score"] > 75).all()
except:
    failed += 1
    print('.filter_passing_students test failed')

try:
    processor.merge_with_extra_data(extra_data)
    assert 'Club' in processor.df.columns 
except:
    failed += 1
    print('.merge_with_extra_data test failed')

processor = StudentDataProcessor(clean_data)
try:
    processor.apply_bonus(lambda x: x * 1.1)
    assert (processor.df.sort_values(by = "Name").Math_Score.to_numpy().astype(float) == np.array([85, 78, 92, 70, 88]) * 1.1).all()
    assert (processor.df.sort_values(by = "Name").Science_Score.to_numpy().astype(float) == np.array([90, 76, 88, 65, 82]) * 1.1).all()
except:
    failed += 1
    print('.apply_bonus test failed')

processor = StudentDataProcessor(clean_data)
try:
    df_reference = pd.Series(
    data=[1, 2, 2], 
    index=[2018, 2019, 2020], 
    name="count", 
    dtype="int64"
    )
    students_per_year = processor.students_per_year()
    assert isinstance(students_per_year, pd.Series) 
    assert students_per_year.equals(df_reference)
except:
    failed += 1
    print('.students_per_year test failed')


processor = StudentDataProcessor(yearly_data)
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
    print('All methods passed successfully')