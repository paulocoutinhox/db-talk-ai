
# CLOUD MODELS

This document explains how to configure API keys for cloud-based models like **OpenAI GPT**, **DeepSeek AI**, **Gemini AI**, and **Grok AI**.

## 🔑 **Supported API Providers**

- **OpenAI GPT**
- **DeepSeek AI**
- **Gemini AI**
- **Grok AI**

---

## ⚙️ **How to Set API Keys**

Set the appropriate API keys for each provider as environment variables.

### 🔸 **OpenAI API Key**

#### Linux/macOS:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

#### Windows (Command Prompt):
```cmd
set OPENAI_API_KEY="your-openai-api-key"
```

#### Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your-openai-api-key"
```

---

### 🔸 **DeepSeek API Key**

#### Linux/macOS:
```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

#### Windows (Command Prompt):
```cmd
set DEEPSEEK_API_KEY="your-deepseek-api-key"
```

#### Windows (PowerShell):
```powershell
$env:DEEPSEEK_API_KEY="your-deepseek-api-key"
```

---

### 🔸 **Gemini API Key**

#### Linux/macOS:
```bash
export GEMINI_API_KEY="your-gemini-api-key"
```

#### Windows (Command Prompt):
```cmd
set GEMINI_API_KEY="your-gemini-api-key"
```

#### Windows (PowerShell):
```powershell
$env:GEMINI_API_KEY="your-gemini-api-key"
```

---

### 🔸 **Grok AI API Key**

#### Linux/macOS:
```bash
export XAI_API_KEY="your-xai-api-key"
```

#### Windows (Command Prompt):
```cmd
set XAI_API_KEY="your-xai-api-key"
```

#### Windows (PowerShell):
```powershell
$env:XAI_API_KEY="your-xai-api-key"
```

---

## 📌 **Persistent Configuration**

To make these environment variables permanent:

- **Linux/macOS:** Add the export commands to your `~/.bashrc` or `~/.zshrc` file.
- **Windows:** Set environment variables via **System Properties** > **Advanced** > **Environment Variables**.

---

## ❓ **Troubleshooting**

- Ensure your API key is valid and active.
- Restart your terminal or development environment after setting the environment variables.
- Double-check the exact spelling of the environment variable names.
