class InteractiveConsoleClient:
    """do not modify this code"""

    def __init__(self, manager):
        self.manager = manager

    def run(self):
        self._show(self.WELCOME_MESSAGE)
        while self._read_and_answer_question():
            pass
        self._show(self.GOODBYE_MESSAGE)

    def _read_and_answer_question(self):
        question_text = self._read_question()
        if not question_text:
            return False
        self._answer_question(question_text)
        return True

    def _read_question(self):
        question = input(self.QUESTION_PROMPT)
        return question

    def _answer_question(self, question_text):
        candidate, _score = self.manager.answer_question(question_text)
        if candidate:
            self._show_answer(candidate)
        else:
            self._show_no_answer()

    def _show_answer(self, candidate):
        self._show(self.ANSWER_TEMPLATE.format(question=candidate.question, answer=candidate.answer))

    def _show_no_answer(self):
        self._show(self.NO_ANSWER_MESSAGE)

    def _show(self, message):
        print(message)

    WELCOME_MESSAGE = "Hello, I am a question answering bot."
    GOODBYE_MESSAGE = "Goodbye!"
    QUESTION_PROMPT = "\nPlease enter a question, and press the ENTER key: "
    NO_ANSWER_MESSAGE = "I cannot answer this."
    ANSWER_TEMPLATE = "I think that you asked '{question}' and conclude that the answer is '{answer}'."
