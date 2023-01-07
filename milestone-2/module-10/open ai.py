import openai

openai.api_key = ("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")
prompt = input('enter your command')
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="prompt",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)