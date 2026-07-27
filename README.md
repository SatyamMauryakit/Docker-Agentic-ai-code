# Docker Agentic AI Code

An intelligent AI-powered agent system for Docker management and interaction using local LLMs. This project demonstrates the integration of LangChain with Ollama to create autonomous agents capable of understanding and executing Docker-related tasks through natural language processing.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Benefits](#benefits)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Files](#project-files)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

Docker Agentic AI Code is a Python-based application that combines the power of LangChain framework with Ollama's local LLM capabilities to create intelligent agents that can:

- Understand natural language queries about Docker
- Execute Docker commands programmatically
- Provide real-time container status and logs
- Interact conversationally with users about their Docker environments

This project showcases two different approaches to building AI agents for Docker management, offering flexibility in how you implement agentic workflows.

---

## ✨ Features

### Core Capabilities

- **🤖 Natural Language Interface**: Communicate with your Docker environment using plain English
- **🐳 Docker Integration**: Direct access to Docker container management and monitoring
- **📊 Real-time Monitoring**: View running containers and access container logs instantly
- **💬 Conversational AI**: Multi-turn conversation support with context awareness
- **🔧 Tool Integration**: Extensible tool framework for adding custom Docker operations
- **⚡ Local LLM Support**: Uses Ollama for running LLMs locally without cloud dependencies

---

## 🛠 Tech Stack

### Core Technologies

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.x | Primary programming language |
| **LangChain** | Latest | Framework for building LLM applications |
| **Ollama** | Latest | Local LLM runtime and model management |
| **LangGraph** | Latest | Advanced agent orchestration |
| **Docker** | Any | Container runtime for executing container commands |

### Key Libraries & Dependencies

```
langchain-ollama      - LangChain integration with Ollama
ollama               - Ollama Python client
langgraph            - Graph-based LLM agent orchestration
langchain            - Core LangChain framework
```

---

## 🎁 Benefits

### 1. **Privacy & Security**
   - ✅ All processing happens locally
   - ✅ No data sent to external APIs or cloud services
   - ✅ Full control over your data and queries

### 2. **Cost Efficiency**
   - ✅ No API costs or subscription fees
   - ✅ One-time model download from Ollama
   - ✅ Minimal resource requirements

### 3. **Low Latency**
   - ✅ Instant response times from local models
   - ✅ No network latency overhead
   - ✅ Real-time Docker command execution

### 4. **Flexibility & Extensibility**
   - ✅ Easy to add custom tools and commands
   - ✅ Support for multiple LLM models
   - ✅ Two implementation patterns provided

### 5. **Developer-Friendly**
   - ✅ Simple, clean Python code
   - ✅ Well-structured agent patterns
   - ✅ Easy to understand and modify

### 6. **Educational Value**
   - ✅ Learn about LLM agents and orchestration
   - ✅ Understand Docker-AI integration
   - ✅ Practical examples of LangChain usage

---

## 📁 Project Structure

```
Docker-Agentic-ai-code/
├── agent.py                 # LangChain-based agent with tools
├── pythonai_agent.py       # Ollama client-based agent
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore configuration
└── README.md               # This file
```

---

## 📦 Prerequisites

Before you start, ensure you have:

1. **Python 3.8 or higher** installed on your system
2. **Ollama** installed and running locally
3. **Docker** installed and running
4. **pip** (Python package manager)

### Installation Links

- [Python Download](https://www.python.org/downloads/)
- [Ollama Installation](https://ollama.ai)
- [Docker Installation](https://docs.docker.com/get-docker/)

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/SatyamMauryakit/Docker-Agentic-ai-code.git
cd Docker-Agentic-ai-code
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv myenv
myenv\Scripts\activate

# On macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Ensure Ollama is Running

Make sure Ollama service is running on your system:

```bash
# Check if Ollama is running
ollama --version

# Pull the required model (if not already present)
ollama pull llama3.2:1b
```

### Step 5: Verify Docker Access

```bash
# Test Docker connectivity
docker ps
```

---

## 💻 Usage

### Option 1: Using LangChain Agent (Recommended)

This implementation uses LangChain's agent framework with integrated tools:

```bash
python agent.py
```

**Features:**
- Tool-based architecture
- Better error handling
- More extensible design
- Direct tool integration

**Example Interaction:**
```
You: Show me running containers
AI: [Lists all running Docker containers with details]

You: What are the logs for container xyz?
AI: [Displays container logs]
```

### Option 2: Using Ollama Direct Client

This is a simpler, more direct approach using Ollama's Python client:

```bash
python pythonai_agent.py
```

**Features:**
- Lightweight and simple
- Direct model communication
- Minimal dependencies
- Good for prototyping

**Example Interaction:**
```
You: What Docker containers are running?
AI: [Response based on Docker knowledge]

You: exit
Goodbye!
```

### Exit the Application

Type `exit` or `quit` in either program to terminate the session.

---

## 📄 Project Files

### 1. **agent.py** (Main Implementation - 66 lines)

**Purpose:** Primary agent implementation using LangChain framework

**Key Components:**
- `ChatOllama`: Initializes the Ollama LLM model
- `show_running_containers()`: Tool to list running containers
- `show_container_logs()`: Tool to fetch container logs
- `create_agent()`: Creates the intelligent agent with tools
- Main conversation loop with user input handling

**Model Used:** llama3.2:1b (1B parameter lightweight model)

```python
Key Functions:
- show_running_containers() - Executes 'docker ps' command
- show_container_logs(container_id) - Executes 'docker logs' command
- Agent loop - Handles user input and generates responses
```

### 2. **pythonai_agent.py** (Alternative Implementation - 20 lines)

**Purpose:** Simplified agent using direct Ollama client

**Key Components:**
- System prompt definition
- Direct Ollama chat interface
- Conversation loop
- Simple message formatting

**Advantages:** Minimal code, easy to understand, lightweight

### 3. **requirements.txt** (Dependencies)

```
langchain-ollama    - Bridges LangChain with Ollama
ollama             - Python client for Ollama
langgraph          - Advanced graph-based agent orchestration
langchain          - Core LLM application framework
```

### 4. **.gitignore**

Configured to ignore:
- Python virtual environment (`myenv/`)
- Python cache files (`__pycache__/`)

---

## 🧠 How It Works

### Architecture Overview

```
User Input
    ↓
AI Agent (LangChain/Ollama)
    ↓
Tool Selection & Execution
    ├─→ show_running_containers()
    ├─→ show_container_logs()
    └─→ [Custom tools can be added]
    ↓
Response Generation
    ↓
Display to User
```

### Workflow Sequence

1. **User Input**: User provides natural language query
2. **LLM Processing**: Ollama processes input using llama3.2:1b model
3. **Tool Selection**: Agent determines which tool to use (if any)
4. **Command Execution**: Tool executes Docker command via subprocess
5. **Result Formatting**: Output is formatted and returned
6. **Response Generation**: LLM generates natural language response
7. **User Output**: Response is displayed to the user

### LLM Model Details

- **Model**: llama3.2:1b
- **Size**: ~1 GB (compact, fast inference)
- **Parameters**: 1 Billion
- **Capabilities**: General knowledge, Docker expertise, tool usage
- **Temperature**: 0.7 (balanced between creativity and consistency)

---

## 🔄 Execution Flow Example

**Scenario:** User asks about running containers

```
1. User: "Show me running containers"
   ↓
2. LLM Analysis: Recognizes query needs 'show_running_containers' tool
   ↓
3. Tool Execution: Subprocess runs: docker ps
   ↓
4. Result Processing: Captures stdout with container details
   ↓
5. LLM Response: Formats output into friendly response
   ↓
6. Output: AI displays container information to user
```

---

## 🚀 Future Enhancements

### Planned Features

- [ ] Add more Docker tools (pull image, run container, stop container, etc.)
- [ ] Implement container creation and deletion capabilities
- [ ] Add container statistics and monitoring tools
- [ ] Support for Docker Compose operations
- [ ] Web UI for agent interaction
- [ ] Database for conversation history
- [ ] Multi-model support selection
- [ ] Docker image management tools
- [ ] Network and volume management
- [ ] Advanced error handling and logging

### Extension Ideas

```python
# Potential new tools to add:
@tool
def run_container(image: str, name: str) -> str:
    """Run a new Docker container"""
    pass

@tool
def stop_container(container_id: str) -> str:
    """Stop a running container"""
    pass

@tool
def get_container_stats(container_id: str) -> str:
    """Get container resource statistics"""
    pass
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Areas

- 🐛 Bug fixes and improvements
- ✨ New Docker tools and capabilities
- 📖 Documentation enhancements
- 🧪 Additional test cases
- 🎨 UI/UX improvements

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute this code.

---

## 🔗 Quick Links

- [LangChain Documentation](https://python.langchain.com/)
- [Ollama Project](https://ollama.ai)
- [Docker Documentation](https://docs.docker.com/)
- [LangGraph Documentation](https://langgraph.ai/)

---

## 📞 Support & Questions

For issues, questions, or suggestions:

- Open an [Issue](https://github.com/SatyamMauryakit/Docker-Agentic-ai-code/issues)
- Check existing [Discussions](https://github.com/SatyamMauryakit/Docker-Agentic-ai-code/discussions)
- Contact the maintainer

---

## 🎓 Learning Resources

### Understanding Agents

- [What are AI Agents?](https://python.langchain.com/docs/modules/agents/)
- [Tool Use in LLMs](https://python.langchain.com/docs/modules/tools/)

### Getting Started with Ollama

- [Ollama GitHub](https://github.com/ollama/ollama)
- [Available Models](https://ollama.ai/library)

### Docker Mastery

- [Docker Official Guide](https://docs.docker.com/get-started/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)

---

## 📊 Project Statistics

- **Language**: Python 100%
- **Lines of Code**: ~100+
- **Dependencies**: 4 main packages
- **Models Used**: Ollama (llama3.2:1b)
- **Docker Integration**: Full CLI access

---

**Built with ❤️ for Docker and AI enthusiasts**

*Last Updated: July 2026*
