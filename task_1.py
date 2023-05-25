import pandas as pd
import os

folder_path = 'excel_example'
merged_data = pd.DataFrame()

for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        data = pd.read_excel(file_path)
        data['source_file'] = filename
        merged_data = pd.concat([merged_data, data])

merged_data.sort_values(by=['Number', 'source_file'], inplace=True)
merged_data.drop('source_file', axis=1, inplace=True)
merged_data.to_excel('output.xlsx', index=False)

# import pandas as pd
# import os
# from collections import deque
#
# folder_path = 'excel_example'
# merged_data = pd.DataFrame()
#
# file_queue = deque(sorted(os.listdir(folder_path)))
# while file_queue:
#     filename = file_queue.popleft()
#     if filename.endswith('.xlsx'):
#         file_path = os.path.join(folder_path, filename)
#         data = pd.read_excel(file_path)
#         data['source_file'] = filename
#         merged_data = pd.concat([merged_data, data])
#
# merged_data.sort_values(by=['Number', 'source_file'], inplace=True)
# merged_data.drop('source_file', axis=1, inplace=True)
# merged_data.to_excel('output.xlsx', index=False)
