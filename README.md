# 23K0007 石田　琉稀

# I'm ready for review

### Update (July 20, 2026 16:45)
It has been confirmed that the application runs successfully after cloning the repository to another machine.

**Setup Instructions:**

```bash
# 1. Clone the repository
git clone [https://github.com/ryuki0007/MindMap-Editor.git](https://github.com/ryuki0007/MindMap-Editor.git)

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# For Windows:
.\venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Run the local development server
python manage.py runserver


# How to use
- Click on the map to create a new node
- Double-click a node to edit its text
- Click "New Mind Map" on the top bar to edit the map title
