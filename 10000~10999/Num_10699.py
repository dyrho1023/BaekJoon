"""
문제
서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

입력
입력은 없다.

출력
서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.
"""

import sys
import time

now = time
print('%4d-%02d-%02d'%(now.localtime().tm_year,now.localtime().tm_mon, now.localtime().tm_mday))
