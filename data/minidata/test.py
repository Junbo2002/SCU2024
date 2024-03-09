str = """INSERT INTO `preference` VALUES ('100', '42600', '1210711');"""

# 分别提取出'100', '42600', '1210711'
import re
pattern = re.compile(r"VALUES \('(\d+)', '(\d+)', '(\d+)'\);")
result = pattern.findall(str)
print(result[0])  # [('100', '42600', '1210711')]