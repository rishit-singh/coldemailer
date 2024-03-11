import os
import sys
from tinytune.gptcontext import GPTContext, GPTMessage, Model
from tinytune.pipeline import Pipeline, PromptJob
from CoverLetter import CoverLetterGenerator
from PerplexityContext import PerplexityContext, PerplexityMessage

llm = PerplexityContext("mixtral-8x7b-instruct", os.getenv("OPENAI_KEY"))

def Callback(content):
        if (content != None):
            print(content, end="")
        else:   
            print()

llm.OnGenerateCallback = Callback 

llm.Prompt(PerplexityMessage("user", "Hello LLM"))
llm.Run(True)

# with open(sys.argv[1], 'r') as fp:
#     letterGen = CoverLetterGenerator(os.getenv("OPENAI_KEY"), fp.read())
#     letterGen.Setup()
#     letterGen.Generate("""""")
#     letterGen.Save()

