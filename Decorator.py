# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:57:32 2022

@author: tmark
"""

#중첩함수
def out_func(a):#외부함수 정의
    def in_func():#중첩되는 내부 함수 정의
        print('저장된 인자값은'+a+'입니다.')#외부함수에서 받은 인자값인 a출력
        return '내부함수 in 호출되었습니다.'#내부함수가 호출되었음을 알리는 리턴
    return in_func#외무함수의 리턴값으로는 내부함수를 호출

#First-class function
save_func=out_func('4e3')#외부함수에 인자값을 주며 'save_func'변수에 저장

#Closure
print(save_func())#인자값이 주어진 중첩함수를 호출

#데코레이터 정의
def im_decorator(decofunc):#데코레이터 이름
    def deco():#데코레이터 함수가 입혀주는 내용들
        print('front_deco')
        decofunc()
        print('back_deco')
    return deco

@im_decorator#아래에 정의되는 함수에 데코레이터 적용
def iwantdeco():
    print('I want deco by decorator!')

iwantdeco()














