import os
path_new = "D:/DE/Tuning_SQL/Module06_Operations_Monitoring_new.html"
try:
    with open(path_new, 'w') as f:
        f.write("test")
    print("Successfully wrote to new file!")
    print("New file exists:", os.path.exists(path_new))
except Exception as e:
    print("Failed writing new file:", type(e), e)
