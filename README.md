# SkyStream - Enterprise Airline Management System

A robust, multi-container Django-based web application designed to manage global flight schedules[cite: 3], process instant passenger bookings, generate professional electronic E-Tickets/Boarding Passes with client-side PDF export & print capabilities, and monitor application health using Prometheus & Grafana.

## 🚀 Features

* **Global Flight Schedule Management:** Full weekly flight schedule integration with dynamic status badges (`On Time`, `Boarding`, `Delayed`).
* **Real-Time Booking Engine:** Instant seat availability checking, passenger data recording, and automated database updates using Django ORM.
* **Professional E-Ticket & Boarding Pass:** Generates a stunning electronic boarding pass layout upon successful booking confirmation.
* **PDF Export & Print Integration:** Integrated with `html2pdf.js` for instant single-click high-resolution PDF downloads and clean physical printing layouts.
* **Containerized Deployment:** Scalable multi-container application architecture orchestrated seamlessly via Docker and Docker Compose.
* **Enterprise Monitoring:** Integrated with `django-prometheus` to track application performance metrics and system health.

## 🛠️ Tech Stack

* **Backend:** Python, Django, PostgreSQL
* **Frontend:** HTML5, Tailwind CSS, JavaScript, Font Awesome, html2pdf.js
* **DevOps & Containers:** Docker, Docker Compose, Git / GitHub
* **Monitoring & Metrics:** Prometheus, Django-Prometheus, Grafana

## ⚙️ How to Run Locally

### 1. Clone the repository:
```bash
git clone [https://github.com/holkargopal160-cmyk/Airline-Management-System.git](https://github.com/holkargopal160-cmyk/Airline-Management-System.git)
cd Multi-Container Application Deployment
