# Redes que Cambian

**Connecting You with Organizations Making a Difference Across Mexico**

![Redes que Cambian](public/hero.jpg)

## Overview

**Redes que Cambian** is a platform designed to bridge the gap between individuals and social organizations throughout Mexico. Discover organizations, explore impactful projects, and find out how you can contribute to causes that resonate with you.

This application leverages a robust **Django REST API** back-end and a dynamic **Angular** front-end, all containerized using **Docker** for seamless deployment.

## Features

- **Discover Organizations**: Browse a comprehensive list of social organizations.
- **Explore Projects**: Dive into detailed project descriptions and updates.
- **Get Involved**: Find out how to participate and support various initiatives.
- **Responsive Design**: Enjoy a user-friendly experience on any device.

## Technologies Used

- **Back-end**: Django, Django REST Framework
- **Front-end**: Angular
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **Styling**: Bootstrap, Animate.css
- **Version Control**: Git

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:

- **Docker**: [Get Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Get Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/JavierRangel2004/oscProyect.git
   cd oscProyect
   ```

2. **Set Up Environment Variables**

   Create a `.env` file in the project root if needed. Environment variables are managed within Docker Compose, but you can customize them as per your requirements.

### Running the Application

1. **Build and Start the Docker Containers**

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker images and starts the containers for the back-end, front-end, and PostgreSQL database.

2. **Access the Application**

   - **Front-end (Angular)**: [http://localhost:4200](http://localhost:4200)
   - **Back-end API (Django)**: [http://localhost:8000](http://localhost:8000)

3. **Stop the Application**

   Press `Ctrl+C` in the terminal running `docker-compose`, or run:

   ```bash
   docker-compose down
   ```

### Importing Data

If you have initial data to import (e.g., from a SQL dump), you can use Django management commands:

1. **Run Migrations**

   ```bash
   docker-compose exec web python manage.py migrate
   ```

2. **Import Data**

   Place your SQL dump file in the appropriate directory and run:

   ```bash
   docker-compose exec web python manage.py import_data
   ```

   Ensure that the `import_data` management command is properly configured.

## API Endpoints

The Django REST API exposes the following endpoints:

### Organizations

- **List Organizations**

  ```
  GET /organizations/organizations/
  ```

- **Retrieve an Organization**

  ```
  GET /organizations/organizations/{id}/
  ```

### Projects

- **List Projects**

  ```
  GET /projects/projects/
  ```

- **Retrieve a Project**

  ```
  GET /projects/projects/{id}/
  ```

- **Projects by Organization**

  ```
  GET /projects/projects/?organization={organization_id}
  ```

### Example Responses

**Retrieve Organizations**

```json
[
  {
    "id": 1,
    "name": "Estancia Infantil Vasco de Quiroga I.A.P",
    "description": null,
    "website": "",
    "logo": null,
    "address": "Ramón López Velarde # 7 colonia Lomas de Nuevo México",
    "categories": [
      {
        "id": 2,
        "name": "Infancia"
      }
    ],
    "date_added": "2024-11-26T05:19:44.115252Z",
    "is_active": true,
    "social_media_1": "https://www.facebook.com/p/estancia-infantil-vasco-de-quiroga-iap-100064701769756/",
    "social_media_2": "None",
    "phone_number": "5552572088",
    "email": "None"
  },
  // ... more organizations
]
```

**Retrieve Projects**

```json
[
  {
    "id": 1,
    "organization": {
      "id": 1,
      "name": "Estancia Infantil Vasco de Quiroga I.A.P",
      // ... organization details
    },
    "name": "Estancia Infantil",
    "description": "",
    "objectives": "",
    "achievements": "",
    "participation_methods": "",
    "images": [],
    "categories": [],
    "date_added": "2024-11-26T05:19:44.146804Z",
    "is_active": true
  },
  // ... more projects
]
```

## Project Structure

```plaintext
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Dockerfile for Django back-end
├── requirements.txt         # Python dependencies
├── manage.py                # Django management script
├── README.md                # Project documentation
├── front/                   # Angular front-end application
│   ├── Dockerfile           # Dockerfile for Angular front-end
│   ├── package.json         # NPM dependencies
│   ├── angular.json         # Angular configuration
│   └── src/                 # Angular source code
├── organizations/           # Django app for organizations
│   ├── models.py            # Data models
│   ├── views.py             # API views
│   └── serializers.py       # Data serializers
└── projects/                # Django app for projects
    ├── models.py            # Data models
    ├── views.py             # API views
    └── serializers.py       # Data serializers
```

## Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**

   Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/redes-que-cambian.git
   cd redes-que-cambian
   ```

3. **Create a Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**

   Implement your feature or fix.

5. **Commit Your Changes**

   ```bash
   git commit -m "Add your descriptive commit message"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**

   Go to the original repository and open a pull request.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please open an issue or contact the project maintainers.

---

**Join us in making a difference!**

[![GitHub stars](https://img.shields.io/github/stars/your-username/redes-que-cambian.svg?style=social&label=Star)](https://github.com/your-username/redes-que-cambian)

---
