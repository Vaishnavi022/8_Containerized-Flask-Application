from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask App on AWS</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #78A2D2, #FEFFAF);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        h1 {
            margin-bottom: 10px;
        }
        p {
            font-size: 18px;
        }
        .badge {
            margin-top: 20px;
            padding: 10px;
            background: #78A2D2;
            color: white;
            border-radius: 8px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Flask App Deployed on AWS</h1>
        <p>Your containerized application is running successfully!</p>
        <div class="badge">Docker + ECR + ECS (Fargate)</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)