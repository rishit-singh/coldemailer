import os
import sys
from tinytune.gptcontext import GPTContext, GPTMessage, Model
from tinytune.pipeline import Pipeline, PromptJob
from CoverLetter import CoverLetterGenerator
from PerplexityContext import PerplexityContext, PerplexityMessage

llm = PerplexityContext("pplx-70b-online", os.getenv("PERPLEXITY_KEY"))

def Callback(content):
        if (content != None):
            print(content, end="")
        else:   
            print()

llm.OnGenerateCallback = Callback 

(llm.Prompt(PerplexityMessage("user", ""))
    .Run(True))

print(llm.Messages[-1].Content.find('```'))
message = str(llm.Messages[-1].Content[llm.Messages[-1].Content.find('```json'):])

message = message[:message.find('```')]

print()
print(message)
# with open(sys.argv[1], 'r') as fp:
#     letterGen = CoverLetterGenerator(os.getenv("OPENAI_KEY"), fp.read())
#     letterGen.Setup()
#     letterGen.Generate("""""")
#     letterGen.Save()

