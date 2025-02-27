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
- **Dynamic model discovery** for both:
  - Local GGUF models (auto-detected from the `data/models/` directory)
  - Local Transformer models (loaded from `data/config/models.json`)
- Supports various AI providers:
  - **OpenAI GPT**
  - **DeepSeek AI**
  - **Gemini AI**
  - **Grok AI**
  - **Anthropic AI**
  - **Local Transformer models** (using Hugging Face)
  - **Local GGUF models** (using GPT4All)
- Supports a custom root directory using the **`DB_TALK_AI_ROOT`** environment variable

## 📞 Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/paulocoutinhox/db-talk-ai.git
cd db-talk-ai
```

### **2. Create a Virtual Environment**
```sh
python3 -m venv .venv
.source venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
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

### **1. Set API Keys (For Cloud Models)**

For setting up cloud-based models like **OpenAI GPT**, **DeepSeek AI**, **Gemini AI**, **Grok AI** and **Anthropic**, please refer to the separate guide:

📖 [Cloud Models Configuration](docs/CLOUD_MODELS.md)

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
├── app.py                  # Main entry point (Streamlit interface)
├── requirements.txt        # List of core dependencies
├── requirements-gguf.txt   # Dependencies for GGUF models
│
├── data/                   # Data storage and configurations
│   ├── config/             # Configuration files
│   │   ├── databases.json  # Database connection configurations
│   │   └── models.json     # Local AI model configurations (path, dtype, etc.)
│   ├── models/             # Local GGUF AI model files
│   │   └── Llama-3.2-3B-Instruct-Q5_K_M.gguf  # Example local GGUF model
│   ├── sample/             # Sample databases for testing
│   │   └── sample.db       # Example SQLite database
│   └── schemas/            # Generated database schema files
│       └── sample.txt      # Example schema output file
│
├── models/                 # AI model implementations
│   ├── anthropic_model.py  # Integration with Anthropic API
│   ├── base_model.py       # Abstract base class for AI models
│   ├── local_model.py      # Local model implementation using Hugging Face Transformers
│   ├── local_gguf_model.py # Local GGUF model implementation using GPT4All
│   ├── openai_model.py     # Integration with OpenAI API
│   ├── deep_seek_model.py  # Integration with DeepSeek models
│   ├── grok_model.py       # Integration with Grok AI models
│   └── gemini_model.py     # Integration with Gemini AI models
│
├── extras/                 # Additional resources (images, icons, etc.)
│
├── helpers/                # Utility functions
│   ├── chart.py            # Functions for generating charts
│   ├── db.py               # Database connection handling
│   ├── file.py             # File system helpers (e.g., loading models)
│   ├── model.py            # AI model management functions
│   ├── prompt.py           # Functions to create SQL prompts
│   ├── response.py         # Functions to process and clean AI responses
│   ├── schema.py           # Functions to generate database schemas
│   └── string.py           # String manipulation utilities
│
├── db/                     # Database connection implementations
│   ├── base_database.py    # Base class for database connections
│   └── sql_database.py     # SQL database connection implementation
│
├── charts/                 # Chart implementations for data visualization
│   ├── base_chart.py       # Base class for chart types
│   ├── bar_chart.py        # Bar chart visualization
│   ├── line_chart.py       # Line chart visualization
│   ├── pie_chart.py        # Pie chart visualization
│   ├── heatmap_chart.py    # Heatmap visualization
│   └── map_chart.py        # Geographical map chart visualization
│
├── prompts.txt             # Example prompts for generating SQL queries
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
