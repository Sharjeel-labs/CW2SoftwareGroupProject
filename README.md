# CW2SoftwareGroupProject

A Django web application built for the 5COSC021W Software Development Group Project.

## 👥 Team Members & Branches

| Student | Module   | Branch        |
|--------|----------|--------------|
| S1     | Teams    | s1-teams     |
| S3     | Messages | s3-messages  |
| S4     | Schedule | s4-schedule  |
| S5     | Reports  | s5-reports   |

# Installing Weasyprint on Windows:
Install Python Install Manager: https://apps.microsoft.com/detail/9nq7512cxl7t?hl=en-GB&gl=GB<br>
Install MSYS2: https://www.msys2.org/#installation<br>
Inside of the MSYS2 shell, execeute: `pacman -S mingw-w64-x86_64-pango`<br>
Launch Windows Command Prompt, and input:<br>
`python -m venv venv
venv\Scripts\activate.bat
python -m pip install weasyprint
python -m weasyprint --info`<br>

# Installing Weasyprint on MacOS:
Install Homebrew using the link here:<br> https://brew.sh/ <br>
Inside of Homebrew, Run the Command:<br> `brew install weasyprint`

# How To Run:
1. Clone the repository<br>
`git clone https://github.com/Sharjeel-labs/SoftwareGroupProjectCW2.git`

3. Install dependencies:<br>
   `pip install django`
4. Load Model Data for Reports:<br>
`py manage.py loaddata exampledata.json`

5. Run migrations:<br>
  ` python manage.py migrate`
6. Start server:
   python manage.py runserver 8080
7. Open:
   http://127.0.0.1:8080/

   ## Branching Strategy
Each team member works on feature branches (e.g. s3-messages) and merges via pull requests.
