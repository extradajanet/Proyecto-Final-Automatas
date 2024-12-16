from antlr4 import *
from codeToPyLexer import codeToPyLexer
from codeToPyParser import codeToPyParser
from TraduceCode import TraduceCode

def main():
    input_file = "entrada1.txt"

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
        lexer = codeToPyLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = codeToPyParser(token_stream)
        tree = parser.inicio()

        listener = TraduceCode()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)  # La traducción se imprime directamente aquí.

        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
