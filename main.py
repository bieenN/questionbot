from interactive_console_client import InteractiveConsoleClient
import json
import utils

class QuestionHandler:
    def __init__(self, candidates_path, questions_log_path):
        # Initalise access components
        self.CatalogAccess = CatalogAccess(candidates_path)

        self.LogAccess = LogAccess(questions_log_path)

    def answer_question(self, question_text):
        faq_dict = self.CatalogAccess.retrieve_faq()
        return MatchingEngine(question_text, faq_dict).get_candidate()

class MatchingEngine:
    def __init__(self, user_question, faq_dict):
        self.user_question = user_question
        self.faq_dict = faq_dict

    def get_candidate(self):
        computable_user_question = self.format_question(self.user_question)
        total_faq_questions = len(self.faq_dict)
        
        question_increment = 0

        #List to store jaccard similarity scores of each question relating to the user question
        jaccard_similarity_score_list = []
    
        while question_increment < total_faq_questions:
            computable_faq_question = self.format_question(self.faq_dict[question_increment]['question'])

            jaccard_similarity_score_list.append(utils.jaccard_similarity_score(computable_user_question, computable_faq_question))

            question_increment += 1

        highest_similarity_score = max(jaccard_similarity_score_list)
        candidate_question = [highest_similarity_score, jaccard_similarity_score_list.index(highest_similarity_score)]
        
        #Return the candidate using a candidate object along with the score stored in the candidate_question variable
        return Candidate(self.faq_dict[candidate_question[1]]['question'], self.faq_dict[candidate_question[1]]['answer']), candidate_question[0]

    def format_question(self, question):
        return utils.words_to_lowercase(utils.text_to_words(utils.strip_punctuation(question)))
        
class Candidate:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

#write check to make sure question is longer than 1 word
class CatalogAccess:
    def __init__(self, candidates_path):
        self.candidastes_path = candidates_path

        self.faq_file_json = json.load(open('faq.json', 'r'))

    def retrieve_faq(self):
        return self.faq_file_json

class LogAccess:
    def __init__(self, questions_log_path):
        self.questions_log_path = questions_log_path


def main(candidates_path, questions_log_path):
    manager = QuestionHandler(candidates_path, questions_log_path)
    
    client = InteractiveConsoleClient(manager)
    client.run()

if __name__ == '__main__':
    main("faq.json", "asked_questions_log.txt")


