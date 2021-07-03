import os
import openai

openai.api_key = "INSERT KEY"

start_sequence = "\nOutput:"
restart_sequence = "\n\n Input: "

train_data = "The following is a AI agent that is capable of generating new startup ideas.\n\nInput: Telecom | Machine Learning\nOutput: Optimization of telecom networks using machine learning. Machine learning as a service, providing API - Call failure, traffic detection.\n\nInput: Fintech | Conversational AI\nOutput: AI to deliver conversational banking services that help banks redefine their digital strategy. With NLP, NLU and ML, the platform enables natural dialogues using messaging, voice and IOT devices.\n\nInput: Food | AI, Computer Vision\nOutput: World’s first dedicated computer vision platform for recognising food items.  Allows you to leverage this recognition to power your businesses and orchestrate meaningful actions.\n\nInput: Surveillance | AI, Computer Vision\nOutput: Video Analytics for surveillance for smart city - Solutions for Security, traffic management, Facial recognition.\n\nInput: Business Intelligence | AI, NLP\nOutput: Virtual business analyst that uses AI to augment existing BI tools. Through NLP and ML. Is capable of delivering the same powerful insights that you would come to expect from a data analyst in a matter of seconds.\n\nInput: Automatic Mobile App Testing | Machine Learning\nOutput: Mobile automation testing platform (address issue due to various screensizes, network - 2G, 3G, wifi, phone RAM/CPU issues etc). Platform  helps in testing all these permutations and combinations. Plus AI driven bot to analyse and test app with test results/performance insights/security testing as well.\n\nInput: Fintech | AI, Biotech\nOutput: An end to end AI Infrastructure platform built on deep-tech, machine learning technologies with in-depth analogy of genomic science, psychology & neuroscience.\n\nInput: AI powered enterprise search engine | NLP\nOutput: A natural language driven enterprise search platform named Voody collects and indexes huge amounts of structured & unstructured data from a variety of sources within the organisation and from outside to generate relevant information on dashboards based on the natural language search string input by the user.\n\nInput: Video Conferencing | AR, VR\nOutput: The hardware agnostic 3D conferencing solution that enables designers and researchers to collaborate with their peers across the world in a realistic virtual world along with their 3D data. This emulates the experience of meeting in person with a physical product. .\n\nInput: Aviation | NLP\nOutput: AI-based chatbot for airline agents & customer service representatives to perform many functions like check-in procedures, hotel booking, and complaint management from the Facebook Messenger. It has the capacity to train itself in handling new queries based on artificial intelligence (AI) and machine learning techniques.\n\n Input: "

def gpt3Response(inputs):
	vertical, tech = inputs
	prompt = train_data + vertical + " | " + tech + ".\nOutput"
	response = openai.Completion.create(
	engine="davinci",
	prompt=prompt,
	temperature=0.9,
	max_tokens=150,
	top_p=1,
	best_of=3,
	frequency_penalty=0,
	presence_penalty=0.6,
	stop=["\n", " Input:", " Output:"]
	)

	return response
  
