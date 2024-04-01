
"""
Python 在3.5版本的时候引入了类型注解，
以方便静态类型检查工具，IDE等第三方工具
"""

var_1: int = 10
var_2: float = 3.1415
var_3: bool = True


my_list: list[int] = [1,2,3]
my_tuple: tuple(int, str, bool) = (1, "zhangsan", True)
my_dirc: dict[str, int] = {"duanlingyu", 666}
