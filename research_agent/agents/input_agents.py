import asyncio
import json
from functools import partial
from ollama import generate
from research_agent.system_messages import agent_input_eval_system_message, agent_input_prompt_improver_system_message


with open('research_agent/agents/config.json', 'r') as config_file:
    config = json.load(config_file)

models_config = config['models']


async def agent_user_prompt_evaluate(user_input, agent_system_message):
        """evaluate user input considering agent_input_eval_system_message()

        Args:
            user_input (str): user input
            agent_system_message (str): message to agent to control it and give the scale of the expected user input

        Returns:
            agent_respone(str): PASS or FAIL 
        """
        
        prompt = f"Here is the User Input:{user_input}\n\nHere is the AI Agent's System Message: {agent_system_message}"
        system_message = await agent_input_eval_system_message()
        temperature = models_config['agent_user_prompt_evaluate_config']['options']['temperature']
        model = models_config['agent_user_prompt_evaluate_config']['model']

        loop = asyncio.get_event_loop()
        generate_func = partial(
                generate,
                model=model,
                prompt=prompt,
                system=system_message,
                options={'temperature': temperature}
        )
        
        try:
                response = await loop.run_in_executor(None, generate_func)
                agent_response = response['response']
                
        except Exception as e:
                raise("debug: agent_user_prompt_evaluate" + e)

        return agent_response


async def agent_input_prompt_improver(input, agent_system_message, agent_evaluation):
        """To double check and improve prompt 

        Args:
            input (str): user  input
            agent_system_message (str): message to agent to control it and give the scale of the expected user input
            agent_evaluation (str): agent evaluation of the prompt

        Returns:
            agent_response(str): _description_
        """
        
        temperature = models_config['agent_input_prompt_improver_config']['options']['temperature']
        model = models_config['agent_input_prompt_improver_config']['model']
        prompt = f"Rejected Input:{input}\n\nAgent's System Message: {agent_system_message}\n\nAgent's Evaluation: {agent_evaluation}"
        system_message = await agent_input_prompt_improver_system_message()
        
        loop = asyncio.get_event_loop()

        generate_func = partial(
                generate,
                model=model,
                prompt=prompt,
                system=system_message,
                options={'temperature': temperature}
        )
        
        try:
                response = await loop.run_in_executor(None, generate_func)
                agent_response = response['response']

        except Exception as e:
                raise("debug: agent_input_prompt_improver" + e)

        return agent_response
