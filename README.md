# Agent Registry

## Overview

Agent Registry is a terminal-based Python application that manages AI agents in a centralized registry.

It allows developers to register AI agents, define their roles, capabilities, supported tools, context limits, and operational status. The registry acts as a lightweight service directory for multi-agent systems.

The project demonstrates one of the core architectural components used in modern AI agent frameworks.

---

## Features

- Register AI Agents
- Unique Agent ID Generation
- Agent Role Management
- Tool Registration
- Capability Registration
- Context Window Configuration
- Active / Inactive Status
- Search Agents
- Update Agent Status
- Remove Agents
- Registry Statistics
- JSON Storage

---

## Project Structure

agent-registry/

├── agent_registry.py

├── registry_studio.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python registry_studio.py
```

---

## Menu

```
1. Register Agent

2. View All Agents

3. Search Agent

4. Update Agent Status

5. Remove Agent

6. Registry Statistics

7. Exit
```

---

## Example

Agent Name

```
Research Agent
```

Primary Role

```
Information Retrieval
```

Supported Tools

```
Web Search

Retriever

Browser
```

Capabilities

```
Research

Fact Checking

Summarization
```

Context Limit

```
32000 Tokens
```

Status

```
Active
```

---

## Output

```
Agent Registered Successfully.
```

---

## Generated File

agents.json

Example

```json
[
    {
        "agent_id": "AGENT-001",
        "name": "Research Agent",
        "role": "Information Retrieval",
        "tools": [
            "Web Search",
            "Retriever",
            "Browser"
        ],
        "capabilities": [
            "Research",
            "Fact Checking",
            "Summarization"
        ],
        "context_limit": 32000,
        "status": "Active",
        "created": "17-07-2026 16:30:41"
    }
]
```

---

## Registry Statistics

Example

```
Total Agents : 6

Active Agents : 5

Inactive Agents : 1

Registered Tools : 14

Capabilities : 18
```

---

## Applications

- Multi-Agent Systems
- AI Agent Frameworks
- AI Orchestration
- Agent Discovery
- AI Workflow Management
- Tool Registry
- Enterprise AI Platforms

---

## Future Improvements

- Agent-to-Agent Communication
- Agent Health Monitoring
- Heartbeat Tracking
- Task Assignment Engine
- Automatic Agent Discovery
- Tool Permission Management
- Agent Authentication
- Agent Load Balancing
- Priority-Based Agent Selection
- Agent Metrics Dashboard
- MCP (Model Context Protocol) Integration
- REST API Support
- Web Dashboard
- Docker Deployment

---

## License

MIT License