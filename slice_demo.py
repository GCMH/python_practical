name = "中国abc"
nums = "123456789"

stu_names = ("张三", "李四", "王五", "赵六")

print(name[1])
print(name[-2]) # -x 倒数第x个
print(name[1:4])# [x:y] 保护x不包含y 
print(name[:3]) #[:x] = [0:x]
print(name[3:]) #[x:] = [x:len(str)]
print(name[:])  #[:] = [0:len(str)]
print(nums[0:9:2]) # [x:y:step] for(int i = x; i < y :i += step) str[i]+=str[i]

print(stu_names[-1])
print(stu_names[1:3])

