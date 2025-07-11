# Foodie App Mobile

A React Native mobile application for food ordering and recipe discovery.

## Features

- User authentication and profile management
- Recipe browsing and searching
- Food ordering and cart management
- Order tracking
- Favorites and saved recipes
- Push notifications

## Technologies Used

- React Native
- Expo
- Redux for state management
- React Navigation for routing
- Axios for API requests
- React Native Paper for UI components

## Project Structure

```
mobile_app/
├── assets/           # Images, fonts, etc.
├── src/              # Source code
│   ├── api/          # API services
│   ├── components/   # Reusable components
│   ├── navigation/   # Navigation configuration
│   ├── screens/      # App screens
│   ├── store/        # Redux store
│   ├── utils/        # Utility functions
│   └── App.js        # Main app component
├── .gitignore        # Git ignore file
├── app.json          # Expo configuration
├── babel.config.js   # Babel configuration
└── package.json      # Dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/foodie-app.git
cd foodie-app/mobile_app
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
expo start
```

4. Run on iOS or Android:
```bash
# iOS
expo run:ios

# Android
expo run:android
```

## API Integration

The mobile app uses the same API endpoints as the web application:

- `/api/recipes/` - List all recipes
- `/api/recipes/<id>/` - Recipe detail
- `/api/categories/` - List all categories
- `/api/users/profile/` - User profile
- `/api/orders/cart/` - Shopping cart
- `/api/orders/` - Order list

## Screenshots

- Home Screen
- Recipe List
- Recipe Detail
- Cart
- Checkout
- Profile

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request 