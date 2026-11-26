import pandas as pd

def top_three_salaries(employee: pd.DataFrame, 
                       department: pd.DataFrame) -> pd.DataFrame:

    employee['rnk'] = (employee.groupby('departmentId')['salary']
                               .rank(method = 'dense', ascending = False))

    return (employee.loc[employee.rnk <= 3]
                    .merge(department, left_on='departmentId', right_on = 'id')
                    .rename(columns = {'name_y':'Department', 'name_x':'Employee'})
                    .iloc[:,[1,2,6]])
    
    
    