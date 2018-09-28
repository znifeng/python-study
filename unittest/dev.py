#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#@author: znifeng
import os, sys
import json

reload(sys) 
sys.setdefaultencoding("utf-8") 


"""compare
判断base请求json结果和test请求json结果的diff
请求返回结果的特点：
    1. plan如果只有一个，则为dict格式；plan如果有多个，则为list[dict1, dict2, ...]格式
    2. field同plan

参数说明:
    1. base_result_json: json形式的base环境的请求结果
    2. test_result_json: json形式的test环境的请求结果
    3. ignore_plan_fields: 允许忽略的字段。一个field隶属于某一个plan，一个plan可能需要忽略多个field字段。参数的格式为dict：
    ignore_plan_fields= {
        "plan1":["field1", "field2"],
        "plan2":["field3"]
    }

"""
def compare(base_result_json, test_result_json, ignore_plan_fields=None):
    if ignore_plan_fields == None:
        return base_result_json == test_result_json

    for plan in ignore_plan_fields:
        fields = ignore_plan_fields[plan]
        for field in fields:
            base_field_element, base_field_parent_element = find_field_from_response(base_result_json, plan, field)
            remove_ignored_element(base_field_element, base_field_parent_element)
            test_field_element, test_field_parent_element = find_field_from_response(test_result_json, plan, field)
            remove_ignored_element(test_field_element, test_field_parent_element)

    return base_result_json == test_result_json
 

"""remove_ignored_element
从field_parent_element移除field_element
参数说明:
    1. field_element: 要忽视的field元素
    2. field_parent_element: 要忽视的field元素的父元素
"""
def remove_ignored_element(field_element, field_parent_element):
    if not field_element or not field_parent_element:
        return 
    if isinstance(field_parent_element, dict):
        del(field_parent_element['field'])
    elif isinstance(field_parent_element, list):
        field_parent_element.remove(field_element)
    return 

"""find_field_from_response
从请求的json结果中寻找指定plan下的field元素及其父元素，返回结果为该field的key-value字典。
参数说明：
    1. result_json: json形式的请求结果
    2. plan_name: field所属的plan名
    3. field_name: field名字
"""
def find_field_from_response(result_json, plan_name, field_name):
    expected_field = dict()
    expected_field_parent = None
    try:
        plan_element = result_json['result']['plans']['plan']
        if isinstance(plan_element, dict):
            specific_plan_element = plan_element
        elif isinstance(plan_element, list):
            specific_plan_element = search_specific_element(plan_element, plan_name)

        specific_field_element = specific_plan_element['field'] if specific_plan_element['name'] == plan_name else None

        if isinstance(specific_field_element, dict):
            expected_field = specific_field_element if specific_field_element['name'] == field_name else None
            #specific_plan_element 为plan字典
            expected_field_parent = specific_plan_element
        elif isinstance(specific_field_element, list):
            expected_field = search_specific_element(specific_field_element, field_name)
            #specific_field_element 为field数组
            expected_field_parent = specific_field_element

    except Exception as e:
        print repr(e)

    return expected_field, expected_field_parent


"""search_specific_element
从element list数组中找到指定element_name的元素，返回结果为该element_name对应的dict。
此方法可以用于从plan list中寻找plan，以及从field list中寻找field
参数说明：
    1. element_list: element数组，格式[element_dict1, element_dict2, ...]，每个element_dict为一个字典{}
    2. specific_element_name: 要寻找的特定element的名字

element list格式，例如field list:
[
    {
        "name": "formula",
        "_field_value_text": "q_and_c"
    },
    {
        "name": "sort_lvls",
        "_field_value_text": "120"
    }
]

"""
def search_specific_element(element_list, specific_element_name):
    expected_element = dict()
    try:
        for element in element_list:
            if element['name'] == specific_element_name:
                expected_element = element
                break
    except Exception as e:
        print repr(e)
    return expected_element