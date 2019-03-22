import filecmp

file1 ="C:/Users/Administrator/Desktop/test/baby.py"
file2="C:/Users/Administrator/Desktop/test/Fact.py"

print(filecmp.cmp(file1,file2,shallow=False))