#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#@author: znifeng

"""
dev的单元测试
"""
import os, sys
import json
import pytest, coverage
from dev import *
reload(sys) 
sys.setdefaultencoding("utf-8") 



#search_specific_element方法的正常测试case
def test_search_specific_element_normal_case():
    element_list = [{
        "name": "field1",
        "_field_value_text": "100"
    },
    {
        "name": "field2",
        "_field_value_text": "200"
    }]
    specific_element_name = "field1"
    expected_element={
        "name": "field1",
        "_field_value_text": "100"
    }

    obtained_element = search_specific_element(element_list, specific_element_name)
    assert obtained_element == expected_element

#search_specific_element方法的异常测试case: field_name为不存在的字段
def test_search_specific_element_abnormal_case():
    element_list=[{
        "invalid_name":"field1",
        "_field_value_text": "100"
    }]
    specific_element_name = "field1"
    expected_element=dict()

    obtained_element = search_specific_element(element_list, specific_element_name)
    assert obtained_element == expected_element

#find_field_from_response方法的正常测试case1: plan是一个list, field是一个dict
def test_find_field_from_response_normal_case_1():
    result = {
        "result": {
            "plans": {
                "plan": [
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan1",
                        "field": {
                            "name": "field1",
                            "_field_value_text": "100"
                        }
                    },
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan2",
                        "field": {
                            "name": "field2",
                            "_field_value_text": "200"
                        }
                    }
                ]
            }
          
        }
    }
    expected_element = {
        "name": "field1",
        "_field_value_text": "100"
    }

    obtained_element, obtained_parent_element = find_field_from_response(result, "plan1", "field1")
    assert obtained_element == expected_element

#find_field_from_response方法的正常测试case1: plan是一个dict，field是一个list
def test_find_field_from_response_normal_case_2():
    result = {
        "result": {
            "plans": {
                "plan": {
                    "type": "display",
                    "simple": "true",
                    "name": "plan1",
                    "field": [
                        {
                            "name": "field1",
                            "_field_value_text": "100"
                        },
                        {
                            "name": "field2",
                            "_field_value_text": "200"
                        }
                    ]
                }
            }
          
        }
    }
    expected_element = {
        "name": "field2",
        "_field_value_text": "200"
    }

    obtained_element, obtained_parent_element = find_field_from_response(result, "plan1", "field2")
    assert obtained_element == expected_element

#find_field_from_response方法的异常测试case: result为空
def test_find_field_from_response_abnormal_case():
    result=None
    expected_element = dict()
    obtained_element, obtained_parent_element = find_field_from_response(result, "plan1", "field1")
    assert obtained_element == expected_element

#remove_ignored_element方法的正常测试case: field_parent_element是一个list
def test_remove_ignored_element_normal_case_1():
    field_element = {
        "name": "field1",
        "_field_value_text": "100"
    }
    field_parent_element = [{
        "name": "field1",
        "_field_value_text": "100"
    },
    {
        "name": "field2",
        "_field_value_text": "200"
    }]

    expected_element = [{
        "name": "field2",
        "_field_value_text": "200"
    }]

    remove_ignored_element(field_element, field_parent_element)
    #field_parent_element已经被移除了field_element
    obtained_element = field_parent_element
    assert obtained_element == expected_element

#remove_ignored_element方法的正常测试case: field_parent_element是一个dict
def test_remove_ignored_element_normal_case_2():
    field_element = {
        "name": "field1",
        "_field_value_text": "100"
    }
    field_parent_element = {
        "type": "display",
        "simple": "true",
        "name": "plan1",
        "field": {
            "name": "field1",
            "_field_value_text": "100"
        }
    }
    expected_element = {
        "type": "display",
        "simple": "true",
        "name": "plan1"
    }
    remove_ignored_element(field_element, field_parent_element)
    #field_parent_element已经被移除了field_element
    obtained_element = field_parent_element
    assert obtained_element == expected_element

#remove_ignored_element方法的异常测试case: field_element为空
def test_remove_ignored_element_abnormal_case_1():
    field_element = dict()
    field_parent_element = {
        "type": "display",
        "simple": "true",
        "name": "plan1",
        "field": {
            "name": "field1",
            "_field_value_text": "100"
        }
    }
    expected_element = field_parent_element
    remove_ignored_element(field_element, field_parent_element)
    #field_parent_element已经被移除了field_element
    obtained_element = field_parent_element
    assert obtained_element == expected_element

#remove_ignored_element方法的异常测试case: field_parent_element为空
def test_remove_ignored_element_abnormal_case_2():
    field_element = {
        "name": "field1",
        "_field_value_text": "100"
    }
    field_parent_element = dict()
    expected_element = dict()
    remove_ignored_element(field_element, field_parent_element)
    #field_parent_element已经被移除了field_element
    obtained_element = field_parent_element
    assert obtained_element == expected_element

#compare方法的正常测试case: 不传ignore_plan_fields
def test_compare_normal_case_1():
    r1 = {
        "result": {
            "plans": {
                "plan": [
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan1",
                        "field": {
                            "name": "field1",
                            "_field_value_text": "100"
                        }
                    },
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan2",
                        "field": [
                        {
                            "name": "field2",
                            "_field_value_text": "200"
                        },
                        {
                            "name": "field3",
                            "_field_value_text": "300"
                        },
                        {
                            "name": "field4",
                            "_field_value_text": "400"
                        }
                        ]
                    }
                ]
            }
        }
    }

    r2 = {
        "result": {
            "plans": {
                "plan": [
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan1",
                        "field": {
                            "name": "field1",
                            "_field_value_text": "10000"
                        }
                    },
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan2",
                        "field": [
                        {
                            "name": "field2",
                            "_field_value_text": "20000"
                        },
                        {
                            "name": "field3",
                            "_field_value_text": "300"
                        },
                        {
                            "name": "field4",
                            "_field_value_text": "40000"
                        }
                        ]
                    }
                ]
            }
        }
    }
    expected_isSame = False

    obtained_isSame = compare(r1, r2)
    assert obtained_isSame == expected_isSame

#compare方法的正常测试case: 传ignore_plan_fields，包含1个plan的单个field，以及1个plan的多个field
def test_compare_normal_case_2():
    r1 = {
        "result": {
            "plans": {
                "plan": [
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan1",
                        "field": {
                            "name": "field1",
                            "_field_value_text": "100"
                        }
                    },
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan2",
                        "field": [
                        {
                            "name": "field2",
                            "_field_value_text": "200"
                        },
                        {
                            "name": "field3",
                            "_field_value_text": "300"
                        },
                        {
                            "name": "field4",
                            "_field_value_text": "400"
                        }
                        ]
                    }
                ]
            }
        }
    }

    r2 = {
        "result": {
            "plans": {
                "plan": [
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan1",
                        "field": {
                            "name": "field1",
                            "_field_value_text": "10000"
                        }
                    },
                    {
                        "type": "display",
                        "simple": "true",
                        "name": "plan2",
                        "field": [
                        {
                            "name": "field2",
                            "_field_value_text": "20000"
                        },
                        {
                            "name": "field3",
                            "_field_value_text": "300"
                        },
                        {
                            "name": "field4",
                            "_field_value_text": "40000"
                        }
                        ]
                    }
                ]
            }
        }
    }


    ignore_plan_fields={
        "plan1":["field1"],
        "plan2":["field2", "field4"]
    }
    expected_isSame = True

    obtained_isSame = compare(r1, r2, ignore_plan_fields)
    assert obtained_isSame == expected_isSame

