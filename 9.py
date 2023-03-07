passage = "Chatgpt is an artificial intelligece cahatbot developed by openai and laumched in november 2022." \
          "it is built on top of openai's gpt-3 family of large language models and has been find-tuned (an approach" \
          "to transfer learning) using both supervised and reinforcement learning techniques. Chatgpt"

words = []

words = passage.split()
freq = [words.count(w) for w in words]
print(dict(zip(words, freq)))