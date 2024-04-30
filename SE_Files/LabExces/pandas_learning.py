# Week 12-Pandas

import pandas as pd
import numpy as np

# 1.Write a Pandas program to create a dataframe from a dictionary and display it.
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

kiikii_panda_box_dict = {
    "box1": [78, 85, 96, 80, 86],
    "box2": [84, 94, 89, 83, 86],
    "box3": [86, 97, 96, 72, 83],
}

kiikii_dataframe_box = pd.DataFrame(kiikii_panda_box_dict)

# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index
# labels. Sample Python dictionary data and list labels: exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
# 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5,
# np.nan, 8, 19], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
# 'yes', 'no', 'no', 'yes']} labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_data_dict = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']

labeled_exam_dataframe = pd.DataFrame(exam_data_dict, index=labels)

# Learning to work with the memory_usage() function in  Pandas:
exam_memory_tracker = labeled_exam_dataframe.memory_usage()

# df = pd.read_csv("data.csv")
# print(df.columns)
# print(df.iloc[:, 1])


# 1.Write a Pandas program to create a dataframe from a dictionary and display it.
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

numeric_data_dict = {
    'X': [78, 85, 96, 80, 86], 
    'Y': [84, 94, 89, 83, 86], 
    'Z': [86, 97, 96, 72, 83]
    }
dataframe = pd.DataFrame(numeric_data_dict)


# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which
# has the index labels.
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
# 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


se_exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
se_exam_info_dataframe = pd.DataFrame(se_exam_data, index=labels)

# 3. Write a Pandas program to display a summary of the basic information 
# about a specified DataFrame and its data.
# Sample  Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

math_exam_data = {
    'name': ['Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20],
    'attempts': [1, 3, 2, 3, 2, 3],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes']
}
math_dict_labels = ['-', '.', '*', '-', '*', '.']

math_exam_data_summary = pd.DataFrame(math_exam_data, index = math_dict_labels)
math_exam_detailed_infos = math_exam_data_summary.info()

# 4. Write a Pandas program to get the first 3 rows of a given DataFrame.
# Sample  Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
os_exam_data = {
    'name': ['Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20],
    'attempts': [1, 3, 2, 3, 2, 3],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes']
}
os_dict_labels = ['-', '.', '*', '-', '*', '.']

os_dataframe_box = pd.DataFrame(os_exam_data, index=os_dict_labels)
first_three_os_data_rows = os_dataframe_box.head(3)





if __name__ == '__main__':
    print(labeled_exam_dataframe)
    print(labeled_exam_dataframe)
    print(f"memory usage of each of each columon: {exam_memory_tracker}")
