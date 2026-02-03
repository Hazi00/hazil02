from flask import Flask, render_template

app = Flask(__name__)

# Placeholder data until user provides resume
resume_data = {
    "name": "Your Name",
    "title": "Professional Title",
    "about": "Passionate and experienced professional...",
    "skills": ["Skill 1", "Skill 2", "Skill 3"],
    "experience": [],
    "education": []
}

@app.route('/')
def home():
    return render_template('index.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
