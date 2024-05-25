# Pharmacy Management System

This is a pharmacy management system built with Python and MySQL. The system helps manage pharmacy operations such as inventory, sales, and customer management.

## Features

- Inventory management
- Sales tracking
- Customer management
- Secure environment configuration

## Requirements

- Python 3.7 or higher
- MySQL server

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pharmacy-system.git
    cd pharmacy-system
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:

    - Create a new MySQL database.
    - Import the provided SQL script to set up the database schema:

        ```bash
        mysql -u yourusername -p yourdatabase < pharmacy.sql
        ```

5. Configure the environment variables:

    - Create a `.env` file in the root directory of the project with the following content:

        ```
        DB_HOST=your_db_host
        DB_USER=your_db_username
        DB_PASS=your_db_password
        DB_NAME=your_db_name
        ```

    Note: The `.env` is not shared for security reasons.

## Usage

1. Run the main application:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to manage the pharmacy operations.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
