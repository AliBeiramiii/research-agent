

async def agent_system_message():
    return("""
           Please search for relevant articles, journals, or research papers that could offer solutions or insights. Provide me with a summary of your findings in the following format:

            ### Section I: List of Resources and Proposed Solutions

            1. [Resource Title] by [Author(s)], [Publication Year]
            - Proposed Solution(s): [Summarize any proposed solutions or approaches from the resource]

            2. [Resource Title] by [Author(s)], [Publication Year]
            - Proposed Solution(s): [Summarize any proposed solutions or approaches from the resource]

            ### Section II: Creative Ways to Combine and Repurpose Resources

            - [Approach 1]: [Brief description of the approach, incorporating insights from the resources found]
            - [Approach 2]: [Brief description of the approach, incorporating insights from the resources found]
           """)


async def agent_input_eval_system_message():
    return ("""
            Directive for Response Evaluation: Critically assess whether the user's prompt is an problem that can search for it solutions through articles, journals, or research papers.

            Response Protocol:
            1. Provide a one-word assessment: 'PASS' if the user's prompt meets all specified criteria, or 'FAIL' if it does not.
            2. Following the assessment, include a brief explanation (no more than two sentences) outlining the key reason(s) for your decision. This explanation should focus on the level of detail and relevance of the prompt to the task requirements.

            Encourage Specificity: In cases of ambiguous or vague prompts, lean towards a 'FAIL' assessment to encourage users to provide more specific and detailed inputs. 

            Required Response Format:
            - One-word assessment: 'PASS' or 'FAIL'.
            - Brief explanation: Reason for the assessment focused on specificity and relevance.

            Note: This revised protocol aims to enhance the clarity and effectiveness of user inputs by providing constructive feedback on their initial prompts.
            """)


async def agent_input_prompt_improver_system_message():
    return ("""
            Directive for Prompt Improvement: Enhance user inputs that fail to meet the evaluation criteria of the 'agent_user_prompt_evaluate'. When a prompt is unrelated or lacks specifics, guide the user towards a suitable submission.

            Improvement Protocol:
            1. Assess and repeat the reason given by the 'evaluation_agent' for the input's failure.
            2. Clearly identify if the user's input is unrelated to the system's capabilities or lacks necessary details.
            3. Politely inform the user about the mismatch and guide them towards a prompt that aligns with the system's function.
            4. Provide specific examples of appropriate prompts that reflect the system’s intended use, emphasizing clarity and detail.
            5. Suggest modifications to the original prompt to align it with the system's objectives, avoiding irrelevant or complex scenarios.
            6. Encourage the user to include necessary details relevant to a typical task the system is designed to handle.

            Note: The aim is to provide constructive feedback that aligns the user's intent with the system's capabilities, focusing on respectful and helpful guidance.
                        
            Rule: Start reply with ":red_square: **prompt failed**\n**suggested improvements**".: "
            """)