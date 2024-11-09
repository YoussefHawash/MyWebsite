# Personal Portfolio Website

This is the code for my personal portfolio website, designed to showcase my projects, services, and contact information. The website includes sections about me, the services I provide, a portfolio of my projects, and achievements.
## Description

A personal portfolio website built using Django, showcasing my projects, services, and contact information. Features dynamic content, responsive design, visitor counter, and portfolio showcase. Deployed on AWS EC2 with media storage on AWS S3.Table of Contents

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Demo

You can view a live demo of the website here: [Your Website Link](https://yourwebsite.com)

## Features

- **Dynamic Content**: Uses Django to dynamically load content for `About`, `Projects`, and `Services` sections.
- **Portfolio Showcase**: Displays project thumbnails with links to view the details.
- **Responsive Design**: Optimized for various screen sizes.
- **Visitor Counter**: Tracks the number of visitors on the website.
- **Resume Download**: Includes a link to download my resume.
- **Contact Information**: Provides easy access to email and phone contacts.

## Technologies Used

- **Django**: Python-based web framework used to handle backend logic.
- **HTML/CSS**: For website structure and styling.
- **JavaScript**: For interactive features and animations.
- **Nginx**: Used as a web server (in deployment).
- **AWS EC2**: Hosting the Django application on an AWS EC2 instance.
- **AWS S3**: Used for storing static files and media files like images and PDFs.

## Setup

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YoussefHawash/MyWebsite
   cd MyWebsite
   ```

2. **Install dependencies**:
   - Ensure you have Python and Django installed, then install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Run the server**:
   ```bash
   python manage.py runserver
   ```

5. **Visit the site**: Open `http://127.0.0.1:8000/` in your browser to see the website locally.

### Environment Variables

Make sure to set environment variables required by Django and any other services in a `.env` file. Typical settings include:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
DATABASE_HOST= your_dbhost
DATABASE_NAME=your_dbname
DATABASE_USER=your_dbuser
DATABASE_PASSWORD=your_dbpassword
AWS_S3_REGION_NAME = your_s3_region
AWS_S3_CUSTOM_DOMAIN = your_s3_domain
AWS_S3_FILE_OVERWRITE = False
```

## Usage

- **Home Page**: Displays a brief introduction and links to `About`, `Services`, and `Portfolio` sections.
- **About Section**: Provides background information, including a link to my resume.
- **Portfolio Section**: Lists projects with descriptions and links to GitHub repositories or live versions.
- **Contact Section**: Includes email and phone contact information.

### Folder Structure

The following files and folders are notable in this project:

- `main/`: Contains the main Django app, including templates and static files.
- `staticfiles/main/css/`: Contains the CSS files, including `home.css` and `media.css` for styling.
- `main/templates/main/`: Contains the HTML templates.
- `main/templates/main/includes/`: Contains reusable HTML components like `socialmedia.html` and `js.html`.


## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

