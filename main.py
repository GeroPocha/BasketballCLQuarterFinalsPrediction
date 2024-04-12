from openai import OpenAI
import re
from data_string import data

api_key = "Insert Your OpenAI API Key here :)"
client = OpenAI(api_key=api_key)

prompt_template = """
Based on the comprehensive season data for the Basketball Champions League, specifically focusing on the performance of the Telekom Baskets Bonn and Peristeri bwin, who are currently tied in their quarterfinal series at 1-1, predict the winner of their next match. It is crucial to make a definitive prediction between 'Bonn', 'Peristeri', or 'Even' if a clear winner cannot be determined, but a decision is preferred. At the end of your response, indicate the result with 'Final Prediction:' 
"""

log_file_path = "./basketball_predictions.txt"

with open(log_file_path, "w") as log_file:
    for i in range(1, 101):

        response = client.chat.completions.create(
            model="gpt-4-turbo-2024-04-09",
            messages=[
                {"role": "system", "content": data},
                {"role": "user", "content": prompt_template}
            ]
        )

        prediction_response = response.choices[0].message.content.strip()
        match = re.search(r"Final Prediction: (\w+)", prediction_response)
        if match:
            final_prediction = match.group(1)
        else:
            final_prediction = "No clear prediction"

        print(f"{i}. Prediction: {final_prediction}")

        log_file.write(f"{i}. Pick: {final_prediction}\n")

print(f"Predictions saved to {log_file_path}")