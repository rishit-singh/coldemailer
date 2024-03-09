import os
import sys
from tinytune.gptcontext import GPTContext, GPTMessage, Model
from tinytune.pipeline import Pipeline, PromptJob
from CoverLetter import CoverLetterGenerator

with open(sys.argv[1], 'r') as fp:
    letterGen = CoverLetterGenerator(os.getenv("OPENAI_KEY"), fp.read())
    letterGen.Setup()
    letterGen.Generate("""""")
    letterGen.Save()

