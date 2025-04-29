# LLM Reflection System ( with ChatGPT )

## Overview
The LLM Reflection System is an advanced approach to enhancing AI-generated responses through multi-stage processing. This project uses a reflection technique with OpenAI's GPT models to analyze, critique, and refine responses, resulting in more comprehensive and balanced outputs.

## How It Works

### Three-Stage Processing
1. **Initial Response**: Generates a primary response acting as an expert (economist in the example case)
2. **Reflection Stage**: Analyzes the initial response, identifying missing perspectives, weaknesses, and strengths
3. **Final Refinement**: Produces a polished response with improved content and fluency

### Key Components
- **reflectionEX.py**: Contains core functions for the reflection process
  - `economist()`: Generates expert economic analysis
  - `reflection()`: Evaluates and critiques the initial response
  - `final_reflection()`: Refines content for the final output
- **main.py**: Orchestrates the workflow and handles API interactions

## Example Use Case
The system is demonstrated with an economic analysis question:
> "What is the potential impact of Chinese price war on Thailand economy?"

The workflow:
1. Initial analysis from an "expert economist" perspective
2. Reflection identifies perspectives not covered in the original response
3. Final output combines the strengths of the original analysis with the insights from reflection

## Technical Details
- Uses OpenAI's GPT models  
- Implements structured prompting with system and user roles
- Processes responses through a chain of API calls

## Benefits
- **Enhanced Perspective**: Mitigates blind spots in single-pass AI responses
- **Improved Quality**: Results in more comprehensive and balanced analyses
- **Better Fluency**: Final stage refines language for improved readability
- **Self-correction**: System can identify and address weaknesses in its own reasoning

## Setup Requirements
- OpenAI API key
- Python environment with `openai` package installed

## Getting Started
1. Clone the repository
2. Set your OpenAI API key in the environment variable
3. Modify the `QUERY` and `MODEL_NAME` variables in `main.py` as needed
4. Run `python main.py` to see the system in action

## Example Output

### Question
> "What is the potential impact of Chinese price war on Thailand economy?"

### Answer (After Reflection)
The user's input overlooks the potential effects of a Chinese price war on the Thai tourism industry. Thailand heavily relies on tourism as a major source of revenue and employment. Therefore, any significant decrease in Chinese tourists visiting Thailand, resulting from a price war initiated by China, could prove detrimental to the Thai economy.

Given that China is one of Thailand's largest sources of tourists, a decline in Chinese tourist arrivals could lead to reduced revenue for hotels, restaurants, tour operators, and other businesses in the tourism sector. This, in turn, could trigger job losses and economic hardships for individuals and communities who heavily depend on tourism.

Moreover, a Chinese price war has the potential to impact investor confidence in the Thai economy. Foreign direct investment (FDI) plays a crucial role in Thailand's economic growth. If trade tensions and uncertainty related to the price war increase, it may discourage foreign investors from channeling their investments into Thailand. This, in turn, could have long-term ramifications for the country's economic development and competitiveness.

It is also worth considering the impact of a Chinese price war on global supply chains. Thailand is deeply integrated into regional supply chains, particularly in sectors like electronics and automotive. Should Chinese manufacturers prioritize their domestic market over international markets due to the price war, it could disrupt or slow down the flow of inputs necessary for Thai industries. Consequently, this could weaken production capabilities and hinder the overall competitiveness of these industries.

In conclusion, while the user's analysis points out some significant outcomes of a Chinese price war on the Thai economy, it is important to acknowledge the potential impact on the tourism industry, investor confidence, and supply chain disruptions. These factors carry significant consequences for Thailand's economic growth and stability.
