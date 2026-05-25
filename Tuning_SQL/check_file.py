import os, stat
path = "D:/DE/Tuning_SQL/Module06_Operations_Monitoring.html"
print("Exists:", os.path.exists(path))
try:
    mode = os.stat(path).st_mode
    print("Current Mode:", mode)
    print("Writable flag in mode:", bool(mode & stat.S_IWRITE))
    os.chmod(path, stat.S_IWRITE)
    print("os.chmod successfully ran")
    # Try opening it for writing in append mode
    with open(path, 'a') as f:
        print("Successfully opened for append!")
except Exception as e:
    print("Error encountered:", type(e), e)
