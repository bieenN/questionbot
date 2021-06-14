from typing import Match
import pytest
from main import *
import os
import utils

#Static file paths for testing
faq_json = "faq_test.json"
log_file = "asked_questions_log_test.txt"

#QuestionHandler Testing
@pytest.fixture
def manager():
    return QuestionHandler(faq_json, log_file)

def test_handlerCreateCatelogAccessObj(manager):
    catelog_access_variable = manager.CatelogAccess.candidastes_path
    assert catelog_access_variable == faq_json

def test_handlerCreateLogAccessObj(manager):
    log_access_variable = manager.LogAccess.questions_log_path
    assert log_access_variable == log_file

#Matching Engine Testing
@pytest.fixture
def faq_dict(manager):
    faq_dict = manager.CatelogAccess.retrieve_faq()
    return faq_dict

#Testing Fixtures for different questions
@pytest.fixture
def question_input_scenario1(faq_dict):
    question_text = "What is the weather today?"
    return MatchingEngine(question_text, faq_dict)

@pytest.fixture
def question_input_scenario2(faq_dict):
    question_text = "What is the                                     weather today?"
    return MatchingEngine(question_text, faq_dict)

@pytest.fixture
def question_input_scenario3(faq_dict):
    question_text = "What is the                  asdasd                   weather today?What is the                    asdasd                 weather today?"
    return MatchingEngine(question_text, faq_dict)

@pytest.fixture
def question_input_scenario4(faq_dict):
    question_text = "123123123 ASHDJASDK @&*(&!@#*(&!@*(# HAJSKDJKASHKDJHZXJHCH(&#*$# ZJNXCN12yu-@H#HASd`"
    return MatchingEngine(question_text, faq_dict)

#Fixture Tests
def test_question_scenario1(question_input_scenario1):
    Engine = question_input_scenario1
    candidate, score = Engine.get_candidate()
    assert candidate.question == "What is the weather like today?"

def test_question_scenario2(question_input_scenario2):
    Engine = question_input_scenario2
    candidate, score = Engine.get_candidate()
    assert candidate.question == "What is the weather like today?"

def test_question_scenario3(question_input_scenario3):
    Engine = question_input_scenario3
    candidate, score = Engine.get_candidate()
    assert candidate.question == "What is the weather like today?"

def test_question_scenario4(question_input_scenario4):
    Engine = question_input_scenario4
    candidate, score = Engine.get_candidate()
    #Should equal the first dict in FAQ as no question should get above 0 jaccard similarity score
    assert candidate.question == "What day is today?"

#Test LogAccess
def test_logWrite():
    Access = LogAccess(log_file)
    question_text = "This is a text write"

    Access.log_question(question_text)

    test_log_file = open(log_file, 'r')
    
    assert question_text in test_log_file.read()

#Test CatelogAccess
def test_jsonCleanBadEntry():
    Access = CatelogAccess(faq_json)
    #Bad entry should be removed
    assert Access.faq_file_json == [{'question': 'What day is today?', 'answer': 'Monday'}, {'question': 'What is the weather like today?', 'answer': 'Same as yesterday.'}, {'question': 'Will the weather be sunny today?', 'answer': 'Maybe.'}, {'question': 'Did it snow yesterday?', 'answer': 'No.'}]

def test_returnFaq():
    Access = CatelogAccess(faq_json)
    
    assert Access.retrieve_faq()[0]['question'] == "What day is today?"







    








