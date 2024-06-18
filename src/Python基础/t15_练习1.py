from src.my_utils.file_util import *
from src.my_utils.str_util import *

print(str_reverse("helloworld"))
print(sbustr("helloworld", 0, 5, 2))

print_file_info("../../data/fileLearning.txt")
append_to_file("追加数据", "../../data/abc.txt")
print_file_info("../../data/abc.txt")
