import asyncio
import json
from functools import partial
from ollama import generate


with open('research_agent/agents/config.json', 'r') as config_file:
    config = json.load(config_file)

models_config = config['models']


async def agent_solution_response(user_input, system_message):
    """Agent s` solution.

    Args:
        user_input (str): user input
        system_message (str): message to agent to control it and give the scale of the expected answer 

    Returns:
        agent_response(str): agent response in the expected form
    """
    temperature = models_config['agent_tool_identifier_config']['options']['temperature']
    model = models_config['agent_tool_identifier_config']['model']

    loop = asyncio.get_event_loop()
    generate_func = partial(
        generate,
        model=model,
        prompt=user_input,
        system=system_message,
        options={'temperature': temperature }
    )
    
    try:
        response = await loop.run_in_executor(None, generate_func)
        agent_response = response['response']
        

    except Exception as e:
        raise("debug: agent_solution_response\n" + e)

    return agent_response


async def agent_evaluate_agent_response(user_input, agent_response, system_message):
    """To double check and evaluate the first response and modify it if needed

    Args:
        user_input (str):  user input
        agent_response (str): agent response
        system_message (str): message to agent to control it and give the scale of the expected answer

    Returns:
        improved_response(str): improved response (edited if needed)
    """
    
    temperature = models_config['agent_evaluate_agent_tools_config']['options']['temperature']
    model = models_config['agent_evaluate_agent_tools_config']['model']
    prompt = f"Given the user input: '{user_input}', and considering the available solution the previous agent respnsed:\n`{agent_response}`\nReview the response and ONLY modify the response IF needed. Otherwise just post the original response."

    loop = asyncio.get_event_loop()

    generate_func = partial(
        generate,
        model=model,
        prompt=prompt,
        system=system_message,
        options={'temperature': temperature }
    )
    
    try:
        response = await loop.run_in_executor(None, generate_func)
        agent_response = response['response']
        improved_response = agent_response

    except Exception as e:
        raise("debug: agent_evaluate_agent_response" + e)

    return improved_response