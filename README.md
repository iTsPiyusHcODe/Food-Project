# Foodie App

A responsive, user-friendly website and mobile app for food ordering and recipe discovery built with Django, HTML, CSS, and JavaScript.

## Features

- **Recipe Discovery**: Browse and search for recipes by category, difficulty, and ingredients
- **User Authentication**: Register, login, and manage your profile
- **Food Ordering**: Order prepared meals directly from the website
- **Shopping Cart**: Add items to cart and checkout
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **RESTful API**: Full API support for mobile applications

## Technologies Used

- **Backend**: Python, Django, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Media Handling**: Pillow for image processing
- **Deployment**: Gunicorn, Whitenoise

## Project Structure

```
foodie_app/
├── foodie_app/          # Main project settings
├── users/               # User authentication and profiles
├── recipes/             # Recipe management and display
├── orders/             # Shopping cart and order processing
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── media/              # User-uploaded media
└── requirements.txt    # Project dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/foodie-app.git
cd foodie-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://127.0.0.1:8000/`

## API Endpoints

- `/api/recipes/` - List all recipes
- `/api/recipes/<id>/` - Recipe detail
- `/api/categories/` - List all categories
- `/api/users/profile/` - User profile
- `/api/orders/cart/` - Shopping cart
- `/api/orders/` - Order list

## Mobile App

The mobile app is built using the same API endpoints and provides a native experience for iOS and Android users. The app includes:

- User authentication
- Recipe browsing and searching
- Food ordering
- Order tracking
- User profile management

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/foodie-app](https://github.com/yourusername/foodie-app) 