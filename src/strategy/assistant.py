import openai

class Assistant:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_recommendations(self, user_input):
        openai.api_key = self.api_key

        # Make an API call to OpenAI to generate recommendations
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        recommendations = response.choices[0].text.strip()
        
        return recommendations
