⚙️ Prerequisites
Before you start, make sure you have:
VS Code installed
Git installed and configured (git --version)
Node.js and npm installed (node -v and npm -v)
A GitHub account

🗂️ Folder Structure
Inside your main folder NIL-Sports-Media-Project, create this structure:
NIL-Sports-Media-Project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   ├── index.html
│   └── app.js
│
├── docs/
│   └── CI-CD-SETUP.md
│
├── package.json
└── README.md

🧩 Step 1: Initialize the Project
Open VS Code → open a new folder → name it NIL-Sports-Media-Project.
Then open the terminal inside VS Code and run:
npm init -y
This creates a package.json file.

🧱 Step 2: Create a Simple App
In the src folder, create a file index.html with:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NIL Sports Media</title>
</head>
<body>
  <h1>Welcome to NIL Sports Media DevOps Project</h1>
  <p>Task 1: CI/CD Setup is complete!</p>
</body>
</html>


Then create app.js inside src:
console.log("CI/CD setup running successfully!");

🧰 Step 3: Add Scripts to package.json
Open your package.json and modify it like this:
{
  "name": "nil-sports-media",
  "version": "1.0.0",
  "main": "src/app.js",
  "scripts": {
    "start": "node src/app.js",
    "build": "echo 'Building project...'"
  },
  "author": "Bhanu Dlng",
  "license": "ISC"
}

🧩 Step 4: Initialize Git
git init
git add .
git commit -m "Initial commit - CI/CD setup"


Then connect to your GitHub repo:
git remote add origin https://github.com/<your-username>/NIL-Sports-Media-Project.git
git branch -M main
git push -u origin main

⚙️ Step 5: Create GitHub Actions Workflow
Go to:
📁 .github/workflows/ci.yml
Paste this code:
name: CI Pipeline
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install Dependencies
        run: npm install

      - name: Build the Project
        run: npm run build

      - name: Run the App
        run: npm start

🧪 Step 6: Push Workflow to GitHub
Run these commands in VS Code terminal:
git add .
git commit -m "Added CI/CD pipeline workflow"
git push

Now open your GitHub repo → click on Actions tab → you’ll see your workflow running automatically whenever code is pushed.

🧾 Step 7: Verification
You should see green checks ✅ in your Actions tab once the pipeline completes.
If it fails, click the failed job to see detailed logs.
🚀 Outcome

Congratulations!
You’ve successfully built a CI/CD pipeline from scratch using GitHub Actions for your NIL Sports Media Project — all directly within VS Code, no GitHub secrets needed.
