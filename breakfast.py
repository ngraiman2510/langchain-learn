import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()


def main():
    llm = ChatOpenAI(model="gpt-4o-mini")

    response = llm.invoke("5 healthy breakfast ideas").content
    print(f"Response: {response}\n")
    print("================================\n")


if __name__ == "__main__":
    main()
