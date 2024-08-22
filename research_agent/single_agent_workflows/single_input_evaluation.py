from research_agent.agents.input_agents import agent_user_prompt_evaluate, agent_input_prompt_improver


async def single_input_eval(user_input, agent_system_message):
    """Input evaluation

    Args:
        user_input (str): What user wants
        agent_system_message (str): Agent system message to identify the tools needed based on the task explained

    Returns:
        result(Boolean): PASS or FAIL the evaluatoin test
        evaluation_response(str): Agent response evaluation 
    """

    try:
        evaluation_response = await agent_user_prompt_evaluate(user_input, agent_system_message)
        evaluation_response_word = evaluation_response.strip().split('.')[0]

        if 'PASS' in evaluation_response_word:
            result = True
        elif 'FAIL' in evaluation_response_word:
            result = False
        else:
            result = None
        return result, evaluation_response
    
    except Exception as e:
        raise("debug: single_input_eval\n" + e)


async def single_prompt_improver(input, agent_system_message, agent_evaluation):
    """Improve prompt

    Args:
        input (str): user prompt
        agent_system_message (str): [description]
        agent_evaluation (str): [description]

    Returns:
        str: improved prompt 
    """
    try:
        prompt = f"evaluation_agent output:\n\n{agent_evaluation}."
        evaluation_response = await agent_input_prompt_improver(input, agent_system_message, prompt)

        return evaluation_response
    
    except Exception as e:
        raise("debug: single_prompt_improver\n" + e)
