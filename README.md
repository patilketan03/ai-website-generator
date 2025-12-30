# 🚀 AI-Powered Website Generator | LangChain & Streamlit

An AI-powered application that converts simple text prompts into complete, production-ready HTML, CSS, and JavaScript websites using LangChain, Google Gemini, and Streamlit.

This tool enables rapid website prototyping with clean code, modern UI structure, and real-time AI generation.

---

## ✨ Features

- Generate complete websites from simple text prompts  
- AI-powered website creation using LangChain & Google Gemini  
- Clean, modern, and user-friendly Streamlit interface  
- Automatically produces structured HTML, CSS, and JavaScript  
- Fast and real-time AI responses  
- Download generated website as a ZIP file  

---

## 🖥️ Application Interface

<img width="958" height="502" alt="application-interface" src="https://github.com/user-attachments/assets/45f5fef5-efc4-4821-86e0-e4821ec076e6" />


---

## 🗂️ Project Structure

```
├── main.py                          # Streamlit application entry point
├── req.txt                          # Project dependencies
├── .env                             # Environment variables (API keys)
├── README.md                        # Project documentation
└── ai-website-generator-output.zip  # Generated website output
```

---

## ⚙️ Tech Stack

- Python – Backend logic  
- Streamlit – Interactive web interface  
- LangChain – AI workflow orchestration  
- Google Gemini – Large Language Model  
- HTML, CSS, JavaScript – Website output  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vidyasagar2405/website-generator-web-application.git
cd website-generator-web-application
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate      
```

### 3️⃣ Install Dependencies

```bash
pip install -r req.txt
```

### 4️⃣ Set Environment Variable

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🔄 How It Works

1. User enters a website description  
2. Prompt is processed using LangChain  
3. LangChain communicates with Google Gemini  
4. AI generates structured code:
   - HTML  
   - CSS  
   - JavaScript  
5. Output is displayed and saved for reuse  

---

## 📌 Example Website Generated

### Sample Prompt

```
Create a simple MobilesHub website to show phones, filter by brand,
display best deals, compare mobiles, and add a contact page.
```

### 🎥 Demo Video

Uploading AI-Powered Website Demo.mp4…

### 📸 Screenshots
<img width="960" height="510" alt="demo-website-preview-1" src="https://github.com/user-attachments/assets/7d5fb5b3-e2f8-40e7-a529-4ae720f870fd" />

<img width="960" height="504" alt="demo-website-preview-2" src="https://github.com/user-attachments/assets/3c774c59-bcb3-41e3-afec-5a780c29fcd6" />

---

## 📈 Future Enhancements

- Template-based website generation  
- User authentication and profile management  
- Cloud deployment and hosting support  

---

## 👨‍💻 Author

**Ketan Patil**  
Email: ketanspatil2003@gmail.com  
LinkedIn: https://www.linkedin.com/in/patilketan03  

---






