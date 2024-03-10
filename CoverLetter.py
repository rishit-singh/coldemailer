from tinytune.gptcontext import GPTContext, GPTMessage
import os

class CoverLetterGenerator:
    def __init__(self, apiKey, baseLetter):
        self.BaseLetter = baseLetter
        self.Context = GPTContext("gpt-4-0125-preview", apiKey)
    
        def Callback(content):
            if (content != None):
                print(content, end="")
            else:   
                print()

        self.Context.OnGenerateCallback = Callback

    def Setup(self):
        (self.Context.Prompt(GPTMessage("system", "You're a cover letter generator. You take in cover letters and match them to a job description, then generate a new cover letter that is the most relevant to the job. You only generate the cover letter, and nothing else, not even explainations. Reply with OK only if you understand."))
                .Run(True)
                .Prompt(GPTMessage("user", f"Here's the cover letter {self.BaseLetter}. Dont respond with anything, wait for the job descpription."))
                .Run(True)
        )
        return
    
    def Generate(self, jobDescription):
        (self.Context
            .Prompt(GPTMessage("user", f"""Here's the job description {jobDescription}. Respond with the cover letter only, nothing else."""))).Run(True)

    def Save(self):
        self.Context.Save()

