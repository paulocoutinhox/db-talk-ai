<p align="center">
    <a href="https://github.com/paulocoutinhox/db-talk-ai" target="_blank" rel="noopener noreferrer">
        <img width="180" src="extras/images/logo.png" alt="Logo">
    </a>
</p>

# DB TALK - AI 🧠

**DB TALK - AI** is an interactive application built with **Python** and **Streamlit**, allowing users to query databases using **AI-generated SQL**. It supports **local AI models** or **cloud-based models** (such as **OpenAI GPT**) and provides results as **tables** and **charts**.

## 🚀 Features

- Supports **SQLite, PostgreSQL, and MySQL**
- **AI-powered SQL generation** using **cloud-based models** or **local AI models**
- **Automatic database schema extraction** with overwrite confirmation
- **Schema files saved with unique UUIDs or predefined names**
- **Chart visualization** (Bar, Pie, and Line)
- **Streamlit web interface** for easy interaction
- **Secure database connection management** using a configuration file
- **Modular database support** sql databases
- Supports a custom root directory using the **`DB_TALK_AI_ROOT`** environment variable

## 📞 Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/paulocoutinhox/db-talk-ai.git
cd db-talk-ai
```

### **2. Create a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

If you want use local GGUF models install it too:
```sh
pip install -r requirements-gguf.txt
```

### **4. Download Local AI Models (Optional)**
If you prefer to use a **local AI model** instead of a **cloud-based model** (e.g., OpenAI GPT), follow these steps:

#### **Step 1: Download a Local AI Model**
You can download **GGUF format** models from Hugging Face:
- [Hugging Face - GGUF Models](https://huggingface.co/models)

#### **Step 2: Place the Model in the `models/` Directory**

#### **Step 3: Select the Model in the Streamlit App**
The model selector will automatically list `.gguf` files in `models/`. Choose one in the UI.

#### **Step 4: Run the Application**
```sh
streamlit run app.py
```

## ⚙️ Configuration

### **1. Set API Keys (Optional)**

#### **OpenAI API Key**
If using OpenAI, set your API key as an environment variable:

- **Linux/macOS**
  ```sh
  export OPENAI_API_KEY="your-openai-api-key"
  ```

- **Windows (Command Prompt)**
  ```sh
  set OPENAI_API_KEY="your-openai-api-key"
  ```

- **Windows (PowerShell)**
  ```powershell
  $env:OPENAI_API_KEY="your-openai-api-key"
  ```

#### **DeepSeek API Key**
If using DeepSeek, set your API key as an environment variable:

- **Linux/macOS**
  ```sh
  export DEEPSEEK_API_KEY="your-deepseek-api-key"
  ```

- **Windows (Command Prompt)**
  ```sh
  set DEEPSEEK_API_KEY="your-deepseek-api-key"
  ```

- **Windows (PowerShell)**
  ```powershell
  $env:DEEPSEEK_API_KEY="your-deepseek-api-key"
  ```

### **2. Set Custom Root Directory (Optional)**
You can specify a custom root directory by setting the **`DB_TALK_AI_ROOT`** environment variable. If set, the app will look for the `data/` directory under this path instead of the default local `data/`.

#### **Linux/macOS**
```sh
export DB_TALK_AI_ROOT="/path/to/custom/root"
```

#### **Windows (Command Prompt)**
```sh
set DB_TALK_AI_ROOT="C:\path\to\custom\root"
```

#### **Windows (PowerShell)**
```powershell
$env:DB_TALK_AI_ROOT="C:\path\to\custom\root"
```

### **3. Configure Database Connections**
Configure the `data/config/databases.json` file (or `{DB_TALK_AI_ROOT}/data/config/databases.json` if using the custom root):

```json
[
  {
    "name": "Sample SQLite DB",
    "type": "sql",
    "connection_string": "sqlite:///data/sample/sample.db",
    "schema": "sample.txt"
  },
  {
    "name": "Production PostgreSQL",
    "type": "sql",
    "connection_string": "postgresql://user:password@localhost:5432/production_db"
  },
  {
    "name": "MySQL Backup",
    "type": "sql",
    "connection_string": "mysql://user:password@host:3306/dbname"
  }
]
```

### **4. Generate Database Schema**
1. Click **"Generate Database Schema"** in the UI.
2. A confirmation dialog will appear if a schema already exists.
3. The schema will be saved in the `data/schemas/` directory under the root directory.
4. The app automatically updates the `data/config/databases.json` with the new schema filename.

## 🛠️ Usage

1. **Run the Application**
   ```sh
   streamlit run app.py
   ```

2. **Steps in the Web UI**
   - **Select a database** from the configured options
   - **Generate the database schema** if needed
   - **Choose an AI model** (cloud or local)
   - **Ask questions in natural language** to generate queries
   - **View results** in tables or **charts** (Bar, Pie, Line)

## 📂 Project Structure

```
db-talk-ai/
│
├── README.md               # Project documentation
├── app.py                  # Main application entry point (runs the Streamlit interface)
├── requirements.txt        # List of required Python dependencies
├── requirements-gguf.txt   # List of required Python dependencies for GGUF models
│
├── data/                   # Data storage (or custom root if using DB_TALK_AI_ROOT)
│   ├── config/             # Database configuration files
│   │   └── databases.json  # Database connection configurations
│   ├── models/             # Local AI model files
│   │   └── AnyModel.gguf   # Example local AI model file
│   ├── sample/             # Sample databases
│   │   └── sample.db       # Example SQLite database for testing
│   └── schemas/            # Generated database schema files
│       └── sample.txt      # Example database schema file
│
├── models/                 # AI model interfaces and implementations
│   ├── base_model.py       # Base class for AI models
│   ├── local_model.py      # Local AI model implementation using Torch
│   ├── gguf_model.py       # Local AI model implementation using GGUF files
│   └── openai_model.py     # Integration with OpenAI models
│   └── deep_seek_model.py  # Integration with DeepSeek models
│   └── grok_model.py       # Integration with Grok models
│   └── gemini_model.py     # Integration with Gemini models
│
├── extras/                 # Extra resources (images, icons, etc.)
│
├── helpers/                # Utility functions and helpers
│   ├── chart.py            # Functions for generating charts
│   ├── db.py               # Functions for handling database connections
│   ├── file.py             # File manipulation utilities
│   ├── model.py            # Functions to manage AI models
│   ├── prompt.py           # Functions to create database query prompts
│   ├── response.py         # Functions to handle and clean AI responses
│   ├── schema.py           # Functions for generating and updating database schemas
│   └── string.py           # String manipulation utilities
│
├── db/                     # Modular database connection implementations
│   ├── base_database.py    # Base class for database connections
│   └── sql_database.py     # SQL database connection implementation
│
├── charts/                 # Chart implementations for data visualization
│   ├── base_chart.py       # Base class for all chart types
│   ├── bar_chart.py        # Bar chart implementation
│   ├── line_chart.py       # Line chart implementation
│   ├── pie_chart.py        # Pie chart implementation
│   ├── heatmap_chart.py    # Heatmap chart implementation
│   └── map_chart.py        # Map chart implementation
│
├── prompts.txt             # File containing example prompts for testing queries
```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a **pull request**

## 📞 Contact

For issues or contributions, open a **GitHub issue** or contact:
💎 **paulocoutinhox@gmail.com**
🔗 **[GitHub](https://github.com/paulocoutinho)**

## 🖼️ Screenshots

<img width="280" src="https://github.com/paulocoutinhox/db-talk-ai/blob/main/extras/images/screenshot.png?raw=true">

<img width="280" src="https://github.com/paulocoutinhox/db-talk-ai/blob/main/extras/images/screenshot-2.png?raw=true">

## 📜 License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2025, Paulo Coutinho
