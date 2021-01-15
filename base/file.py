file = r"D:\is.txt"
one_file = open(file,"w")
one_file.write("hello python")
one_file = open(file,"r")
s =one_file.read()
one_file.close()
print("成功创建文件")
print(s)

