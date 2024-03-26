# MarketMon Online-Store

MarketMoone Store is an e-commerce project designed for convenient shopping experiences. Users can log in using their phone numbers and receive verification codes for authentication. The project incorporates various technologies such as Celery, RabbitMQ, Redis, PostgreSQL, Amazon S3 bucket, ZarinPal payment gateway, permissions, boto3, CKEditor, and caching.

## Features

- Phone number authentication with verification code.
- Custom User model implementation.
- Integration with PostgreSQL database.
- Integration with Amazon S3 bucket for storage.
- Integration with ZarinPal payment gateway for transactions.
- Usage of Celery and Celery Beat for task scheduling.
- Usage of RabbitMQ and Redis as message brokers.
- Implementation of permissions for user access control.
- Utilization of CKEditor for rich text editing.
- Implementation of caching for improved performance.

## Setup

Before running the project, make sure to configure your AWS settings for cloud storage. Also, ensure that necessary environment variables are properly set up, including those related to AWS, RabbitMQ, Redis, and ZarinPal.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/MarketMooneStore.git

   
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Configure AWS settings:

   Make sure to update your AWS settings in the project configuration files.

4. Run migrations:

   ```
   python manage.py migrate
   ```

5. Start Celery worker and beat:

   ```
   celery -A project_name worker -l info
   celery -A project_name beat -l info
   ```

6. Start the Django server:

   ```
   python manage.py runserver
   ```

## Contribution

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact us at mohammadh.khoddami@gmail.com
