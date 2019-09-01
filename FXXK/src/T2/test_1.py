#!/usr/bin/python
#-*-coding:utf-8-*-
import pytest
import allure

#feature :标注测试用例属于哪一个模块的
@allure.feature('模块一')
def test_1():
    assert 0==0

@allure.feature('模块一')
def test_2():
    assert 0<2

#story:对一个测试用例的详细描述
@allure.feature('模块二')
@allure.story('这是一个很牛逼的测试用例')
def test_3():
    assert 0 > 123

@allure.feature('模块二')
@allure.story('这是一个很菜的测试用例')
def test_4():
    '''
    这是对函数的参数，返回值的注释
    '''
    #测试用例的描述是通过函数的注释时来获取到的
    assert "香港是中国的"=="清早起来拥抱太阳"


#测试用例的优先级
'''
Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
2、 Critical级别：严重缺陷（ 功能点缺失）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
'''

@allure.feature('模块三')
@allure.severity('blocker')
def test_5():
    assert  0==0

@allure.feature('模块三')
@allure.severity('critical')
def test_6():
    assert  0==0

@allure.feature('模块三')
@allure.severity('normal')
def test_7():
    assert  0==0

@allure.feature('模块三')
@allure.severity('minor')
def test_8():
    assert  0==0

@allure.feature('模块三')
@allure.severity('trivial')
def test_9():
    assert  0==0

#step 记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
#isintance(参数一，参数二） 判断数据类型的类，参数一和参数二是否为用一类型
@allure.feature('模块四')
@allure.step("字符串相加：{0}，{1}")
def str_add(str1, str2):
    if not isinstance(str1, str):
        return f"{str1}不是字符串类型"
    if not isinstance(str2, str):
        return f"{str2}不是字符串类型"
    return str1 + str2

@allure.feature('模块四')
def test_10():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'


@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add1(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('test_module_01')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_11():
    str1 = 'hello'
    str2 = 'world'
    assert str_add1(str1, str2) == 'helloworld'
