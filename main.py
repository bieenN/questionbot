from interactive_console_client import InteractiveConsoleClient


def main(candidates_path, questions_log_path):
    #test
    #TODO your initialization code goes here, replacing the `manager = None` statement
    #
    manager = None
    #
    client = InteractiveConsoleClient(manager)
    client.run()


if __name__ == '__main__':
    main("faq.json", "asked_questions_log.txt")
