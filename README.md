# gpt-2-jokes
Joke generation with OpenAI's GPT2

This model uses Max Woolf's [`gpt-2-simple`](https://github.com/minimaxir/gpt-2-simple)
The model was trained using [short-jokes](https://www.kaggle.com/abhinavmoudgil95/short-jokes)
This project was done in collaboration with [Liam Greenlee](https://www.github.com/liamgreenlee) for ECE 498 at the University of Maine`

# Running it
To run the model simply clone the repository and run `docker build .`

# Generation
The model can be run by importing the jokes python library in the docker container.
`import jokes`
Then run `jokes.genjoke()`

`jokes.genjoke(prefix = "", temperature = .7, length = 80, truncate = True)`
