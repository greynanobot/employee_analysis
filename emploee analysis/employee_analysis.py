import pandas as pd
from datetime import datetime

def process_employee_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['Date of Joining'] = pd.to_datetime(df['Date of Joining'], dayfirst=True)
    today = datetime.today()
    df['Tenure (Years)'] = (today - df['Date of Joining']).dt.days / 365
    df['Annual Salary'] = df['Salary'] * 6

    print("\nTotal Salary per Department:")
    print(df.groupby('Department')['Salary'].sum())

    print("\nEmployees with more than 2 years of tenure:")
    print(df[df['Tenure (Years)'] > 2][['Name', 'Department', 'Tenure (Years)']])

    print("\nTop 3 Highest Paid Employees:")
    print(df.nlargest(3, 'Salary')[['Name', 'Department', 'Salary']])

    print("\nEmployees with Annual Salary (Monthly Salary × 6):")
    print(df[['Name', 'Department', 'Salary', 'Annual Salary']])

    print("\nAverage Salary per Department:")
    print(df.groupby('Department')['Salary'].mean())

    return df

process_employee_data("sample_data.csv")
