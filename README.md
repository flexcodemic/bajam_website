Farmer Store E-Commerce Website
===============================

**Farmer Store** is an e-commerce platform that connects farmers and buyers, enabling farmers to list and sell farm produce while providing buyers with a marketplace to purchase farm products. The platform aims to foster sustainable agriculture by streamlining the buying and selling process for agricultural products.

Table of Contents
-----------------

- [Farmer Store E-Commerce Website](#farmer-store-e-commerce-website)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup Instructions](#setup-instructions)
  - [Usage](#usage)
  - [Screenshots](#screenshots)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
    

Project Overview
----------------

Farmer Store is designed to simplify the process of selling and purchasing farm products. Farmers can register, create profiles, and list products for sale, while buyers can browse products, search for specific items, and place orders. The platform offers a user-friendly, responsive design with modern features like authentication, cart management, and notifications.

Features
--------

*   **User Registration and Authentication**: Users can sign up, log in, and manage their accounts.
    
*   **Product Listing**: Farmers can list their farm produce for sale with product images, prices, and descriptions.
    
*   **Product Search and Browse**: Buyers can easily search and filter products by category and price.
    
*   **Shopping Cart**: Users can add items to their cart and view the total price before checkout.
    
*   **Multi-Currency Support**: The platform supports multiple currencies for users in different regions.
    
*   **Responsive Design**: The website is fully responsive, providing a seamless experience across devices.
    
*   **User Profiles**: Each user can update their profile and manage their listed products.
    
*   **Notifications**: Users are notified of new messages, sales, or relevant updates.
    

Tech Stack
----------

*   **Backend**: Django (Python)
    
*   **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
    
*   **Database**: SQLite (for development), MySQL/PostgreSQL (for production)
    
*   **Icons**: FontAwesome for icons such as cart, user, notifications
    
*   **Hosting**: Deployed on Heroku/DigitalOcean/AWS (for production)
    
*   **Version Control**: Git and GitHub for source code management
    

Installation
------------

### Prerequisites

*   Python 3.x
    
*   Django 4.x
    
*   Git
    

### Setup Instructions

1.  bashCopy codegit clone https://github.com/your-username/farmerstore\_project.gitcd farmerstore\_project
    
2.  bashCopy codepython -m venv venvsource venv/bin/activate # On Windows: venv\\Scripts\\activate
    
3.  bashCopy codepip install -r requirements.txt
    
4.  bashCopy codepython manage.py migrate
    
5.  bashCopy codepython manage.py runserver
    
6.  **Access the application**:Open your browser and go to http://127.0.0.1:8000/ to view the site.
    

Usage
-----

1.  **Register/Login**: Users can create an account and log in.
    
2.  **Browse Products**: Buyers can view available farm products.
    
3.  **Cart Management**: Add items to the shopping cart and proceed to checkout.
    
4.  **Product Listing (Farmers)**: Farmers can add new products to sell, including setting prices and uploading images.
    
5.  **Notifications**: Users will be alerted to important notifications related to their account or products.
    

Screenshots
-----------

Home PageProduct Page

Contributing
------------

We welcome contributions! Please follow these steps:

1.  Fork the repository.
    
2.  Create a new feature branch (git checkout -b feature-branch).
    
3.  Commit your changes (git commit -m 'Add feature').
    
4.  Push to the branch (git push origin feature-branch).
    
5.  Create a pull request.
    

Please ensure your code follows the project's coding standards and passes tests before submitting.

License
-------

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
-------

If you have any questions, suggestions, or issues, feel free to reach out:

*   **Project Owner**: Anthony Aruma
    
*   **Email**: anthonyaruma091@gmail.com
    
*   **GitHub**: [Tony Rumex](https://github.com/flexcodemic/bajam_website)