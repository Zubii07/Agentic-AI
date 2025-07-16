from langchain_openai import ChatOpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize model
llm = ChatOpenAI(temperature=0, api_key=os.getenv("OPENAI_API_KEY"))


# 1️⃣ Few-shot examples
examples = [
    {
        "question": "If Ahmed has 3 mangoes and buys 2 more, how many does he have?",
        "reasoning": "Ahmed starts with 3 mangoes. He buys 2 more. 3 + 2 = 5. So, he has 5 mangoes."
    },
    {
        "question": "Sara had 10 rupees and gave 4 to her friend. How much is left?",
        "reasoning": "Sara had 10 rupees. She gave 4 away. 10 - 4 = 6. So, she has 6 rupees left."
    }
]

# 2️⃣ Template for each example
example_prompt = PromptTemplate(
    input_variables=["question", "reasoning"],
    template="Q: {question}\nA: {reasoning}"
)


# 3️⃣ Final few-shot prompt template
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Q: {user_question}\nA:",
    input_variables=["user_question"]
)


# 4️⃣ Chain-of-thought prompting with user input
user_question = "Ali had 5 apples and ate 2. How many are left?"


# 5️⃣ Run the chain
final_prompt = prompt.format(user_question=user_question)
print("🧾 Final Prompt:\n", final_prompt)
response = llm.invoke(final_prompt)
print("\n🧠 Model Output:\n", response.content)
