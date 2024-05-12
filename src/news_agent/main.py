#!/usr/bin/env python
from news_agent.crew import NewsAgentCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    NewsAgentCrew().crew().kickoff(inputs=inputs)