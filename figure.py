""" figure 모듈 설명
길이를 입력하면 함수에 따라 정사각형, 원, 정삼각형의 넓이를 구할 수 있는 모듈입니다.
"""


import math # math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기
class Line:
    """ class Line에 대한 설명
    외부에서 접근 불가능한 __length 필드가 있습니다.
    생성자를 통해 초기 __length의 값을 지정할 수 있습니다.
    해당 필드에 접근하기 위한 메소드 set_length와, get_length가 있습니다.
    """
    def __init__(self, length=1):
        """ 길이의 초깃값을 지정하는 메소드입니다.
        length는 0이하가 될 수 없고 int 또는 float 형이어야 합니다.
        그렇지 않을 경우 __length 필드는 기본 값 1이 됩니다.
        Args:
            length: 길이입니다. 기본 값은 1입니다.
        Returns:
            반환값이 없습니다.
        """
        if (type(length)!=int and type(length)!=float) or length<=0:
            self.__length = 1
        else: self.__length = length

    def set_length(self, length):
        """ 길이를 지정하는 메소드입니다.
        length는 0이하가 될 수 없고 int 또는 float 형이어야 합니다.
        그렇지 않을 경우 __length 필드의 값은 변경되지 않습니다.
        Args: 
            length: 길이입니다.
        Returns:
            반환값이 없습니다.
        """
        if (type(length)==int or type(length)==float) and length>0:
            self.__length = length

    def get_length(self):
        """ 길이를 구하는 함수입니다.
        Returns:
            int or float: 길이를 반환합니다.
        """
        return self.__length
    
def area_square(line):
    """ 길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 정사각형의 한 변입니다.
    Returns:
        int or float: 정사각형의 넓이를 반환합니다.
    """
    if type(line) != Line: return 0

    return line.get_length() ** 2

def area_circle(line):
    """ 길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 반지름의 길이입니다.
    Returns:
        int or float: 원의 넓이를 반환합니다.
    """
    if type(line) != Line: return 0

    return line.get_length() ** 2 * math.pi

def area_regular_triangle(line):
    """ 길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 정삼각형의 한 변입니다.
    Returns:
        int or float: 정삼각형의 넓이를 반환합니다.
    """
    if type(line) != Line: return 0

    return line.get_length() ** 2 * math.sqrt(3) / 4
