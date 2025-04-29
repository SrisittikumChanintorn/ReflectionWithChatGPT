import os
from openai import OpenAI


# Economist Chatbot
def economist(query, llm, model_name, role):

    full_query = f"\nUser: {query}"

    messages = [
        {"role": "system", "content": f"{role}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

def reflection(query, llm, model_name, reflection_content):

    full_query = f"\nUser: {query}"


    messages = [
        {"role": "system", "content": f"{reflection_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

def final_reflection(query, llm, model_name, reflection_content):

    full_query = f"\nUser: {query}"

    messages = [
        {"role": "system", "content": f"{reflection_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result