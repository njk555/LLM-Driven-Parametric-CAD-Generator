# 🤖 LLM-Driven Parametric CAD Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![CadQuery](https://img.shields.io/badge/CadQuery-3D_Modeling-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered application that converts **natural language descriptions into parametric 3D CAD models** using **Groq LLM**, **CadQuery**, and **Streamlit**.

Users simply describe a model in plain English, and the application automatically generates a 3D CAD model, visualizes it interactively, and exports it as **STEP** and **STL** files.

---

# 📌 Features

- 🧠 Natural Language → CAD Generation
- 📦 Supports Multiple Parametric Shapes
- 🕳 Through Hole & Blind Hole Support
- 🖥 Interactive 3D Viewer
- 📄 STEP Export
- 🧩 STL Export
- 🤖 Groq LLM Integration
- ⚡ Fast Response Time
- 🐞 Optional Debug Mode

---

# 📷 Screenshots

## Home Page

> *(Add screenshot here)*

```
screenshots/home.png
```

---

## Generated CAD Model

> *(Add screenshot here)*

```
screenshots/box.png
```

---

## Interactive 3D Viewer

> *(Add screenshot here)*

```
screenshots/viewer.png
```

---

# 🚀 Supported Shapes

- Box
- Cylinder
- Sphere
- Plate
- Hollow Cylinder

---

# 🕳 Supported Hole Types

- Through Hole
- Blind Hole

---

# 🏗 Project Architecture

```
                Natural Language Prompt
                         │
                         ▼
                Groq Large Language Model
                         │
                         ▼
                  Structured JSON Output
                         │
                         ▼
                  Pydantic Validation
                         │
                         ▼
                 CadQuery CAD Generator
                         │
        ┌────────────────┴───────────────┐
        ▼                                ▼
 Interactive Plotly Viewer          STEP/STL Export
```

---

# 📂 Project Structure

```
LLM-Driven-Parametric-CAD-Generator/

│
├── app.py
├── ui.py
├── llm.py
├── cad.py
├── shapes.py
├── viewer.py
├── models.py
│
├── exports/
├── screenshots/
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .env.example
```

---

# ⚙ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Groq API | Large Language Model |
| CadQuery | Parametric CAD Modeling |
| Plotly | Interactive 3D Visualization |
| Pydantic | Data Validation |

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/LLM-Driven-Parametric-CAD-Generator.git

cd LLM-Driven-Parametric-CAD-Generator
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a file named

```
.env
```

Add your Groq API key

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 💬 Example Prompts

```
Create a box of length 100 mm width 50 mm height 30 mm
```

```
Create a cylinder of diameter 40 mm height 80 mm
```

```
Create a sphere of diameter 60 mm
```

```
Create a plate of length 120 mm width 80 mm thickness 10 mm
```

```
Create a hollow cylinder with outer diameter 60 mm inner diameter 40 mm height 100 mm
```

```
Create a box of length 100 mm width 60 mm height 30 mm with a hole of diameter 20 mm
```

```
Create a box of length 100 mm width 60 mm height 30 mm with a blind hole of diameter 20 mm depth 10 mm
```

---

# 🔄 Workflow

1. Enter a CAD description.
2. Groq converts the prompt into structured JSON.
3. Pydantic validates the generated parameters.
4. CadQuery creates the CAD model.
5. Plotly displays the model interactively.
6. STEP and STL files are exported.

---

# 📤 Output

The application generates:

- Interactive 3D Model
- STEP File (.step)
- STL File (.stl)

---

# 🎯 Future Enhancements

- Additional CAD primitives
- Multiple feature operations
- Fillets and chamfers
- Assemblies
- DXF export
- User authentication
- Cloud model storage

---

# 👨‍💻 Developer

**Noel J Kollarmalil**

B.Tech Computer Science and Engineering

Federal Institute of Science and Technology (FISAT)

---

# 📜 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository on GitHub.