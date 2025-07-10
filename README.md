# Real-Time Collaborative Grammar Editor (Django + React)

-  Grammar checking with [LanguageTool API]
-  Real-time syncing via WebSocket (Django Channels)
-  JWT Authentication
- Django REST Framework (Backend)
-  React (Frontend)

--------------------------------------------
 Installation Guide (Local Setup)

 Prerequisites:
- Python 3.10+
- Node.js + npm
- Redis (for WebSocket channels)
- PostgreSQL or SQLite (default works too)

 Backend Setup (Django):
1. Clone the repository:
   git clone <your-repo-url>
   cd backend

2. Create virtual environment:
   python -m venv venv
   source venv/bin/activate   (or venv\Scripts\activate on Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Setup database:
   python manage.py makemigrations
   python manage.py migrate

5. Create superuser:
   python manage.py createsuperuser

6. Run Redis server:
   sudo service redis-server start

7. Start Django server with Daphne:
   daphne backend.asgi:application

Frontend Setup (React):
1. cd ../frontend
2. npm install
3. npm start

Authentication:
- Register: /api/register/
- Login: /api/login/
- Token saved in browser localStorage

--------------------------------------------
 Deploy to AWS EC2 (Ubuntu)
1. Launch Ubuntu EC2 (open ports 22, 80, 443, 8000)
2. SSH into EC2:
   ssh -i your-key.pem ubuntu@<your-ec2-ip>
3. Install packages:
   sudo apt update && sudo apt install python3-pip python3-venv git redis nginx -y
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt install nodejs -y
4. Clone repo & setup backend
5. Run backend:
   nohup daphne backend.asgi:application --bind 0.0.0.0 --port 8000 &
6. Build frontend:
   cd ../frontend
   npm install
   npm run build
   sudo cp -r build/* /var/www/html/

--------------------------------------------
Useful URLs:
- Django Admin: http://localhost:8000/admin
- Frontend: http://localhost:3000

 Notes:
- Public LanguageTool API used
- JWT via djangorestframework-simplejwt

 
