# Need to load the environment variables from the .env file before importing langchain_openai
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI


def main():

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompts = [
        "What is langchain?",
        "What is LangSmith?",
        "What is the difference between langchain and LangSmith?",
    ]

    for i, prompt in enumerate(prompts):
        response = llm.invoke(prompt).content
        ## indexing the run
        print(f"Run {i + 1}")
        print(f"Prompt: {prompt}")
        print(f"Response: {response}\n")
        print("================================\n")


if __name__ == "__main__":
    main()
