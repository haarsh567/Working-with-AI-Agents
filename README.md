# Working-with-AI-Agents

This project leverages CrewAI and Google Gemini to create a collaborative agent framework that performs research and writes comprehensive articles on specified topics. The agents interact with each other and produce outputs based on given tasks. The project integrates with Streamlit to provide a GUI representation of the data.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Streamlit Integration](#streamlit-integration)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Working-with-AI-Agents.git
   cd Working-with-AI-Agents
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/MacOS:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Create a `.env` file in the root directory and add your API keys:**
   ```plaintext
   GOOGLE_API_KEY=your_google_gemini_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage

### Running the Script

To run the script and get results in the terminal, execute:
```bash
python crew.py
```

### Running the Streamlit App

To run the Streamlit app for a GUI representation, execute:
```bash
streamlit run app.py
```

## File Descriptions

- **`agents.py`**: Defines the agents using CrewAI and integrates Google Gemini for LLM capabilities.
- **`tasks.py`**: Defines the tasks that the agents will execute.
- **`tools.py`**: Contains the tools used by the agents, such as Serper for internet searching capabilities.
- **`crew.py`**: Sets up the CrewAI configuration and executes the defined tasks.
- **`app.py`**: Streamlit app to provide a GUI interface for the project.

## Streamlit Integration

The Streamlit app (`app.py`) provides a graphical interface to interact with the agents. It allows you to input a topic and view the generated research and article directly within the browser. The app also includes error handling for API quota limits and allows you to download the results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
