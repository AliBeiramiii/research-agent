import rich
import asyncio
from research_agent.multi_agent_workflows.multi_article_finder import multi_article_finder 
from research_agent.system_messages import agent_input_eval_system_message
from research_agent.single_agent_workflows.single_input_evaluation import single_input_eval, single_prompt_improver


async def workflow_run(user_input):

    agent_message  = await agent_input_eval_system_message()
    evaluation, evaluation_response = await single_input_eval(user_input, agent_message)
    print(evaluation_response)

    if evaluation == True:
        print("task passed check...")
        result= await multi_article_finder(user_input)
        
        return result
    
    else:
        print("task failed check...")
        result= await single_prompt_improver(user_input, agent_message, evaluation_response)
        print(f"here's the result: {result}")
        return result


# Run the main function using asyncio
if __name__ == "__main__":
    user_input = input("Talk to your assistant:")

    result = asyncio.run(workflow_run(user_input))
    rich.print(result)
