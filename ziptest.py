import os,glob,tarfile,zipfile

home ="C:/Users/Administrator/Desktop/test"
target ="C:/Users/Administrator/Desktop/test/sample.tgz"
target1 ="C:/Users/Administrator/Desktop/test/test.zip"
pattern ="*.py"

os.chdir(home)
t=tarfile.open(target, "w:gz")
z=zipfile.ZipFile(target1,"w",zipfile.ZIP_DEFLATED)
for file in glob.glob(pattern):
    t.add(file)
    z.write(file)
t.close()
z.close()