from research_agent.agents.article_agents import agent_solution_response, agent_evaluate_agent_response
from research_agent.system_messages import agent_system_message


async def multi_article_finder(user_input_text):
    """Finding the soultion for the prompt, then check the answer and improve agent s` response.

    Args:
        user_input_text (str): _description_

    Returns:
        str: _description_
    """
    try:
        system_message = await agent_system_message()
        # Now use the passed user_input_text instead of args.input
        agent_response = agent_solution_response(user_input_text, system_message)
        improved_decision = await agent_evaluate_agent_response(user_input_text, agent_response, system_message)

        return improved_decision
    
    except Exception as e :
        raise(f"debug: multi_article_finder\n{e}")