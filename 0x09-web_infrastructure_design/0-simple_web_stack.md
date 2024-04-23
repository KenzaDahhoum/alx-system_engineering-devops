Web Infrastructure Overview
This web infrastructure is designed around a single server setup that incorporates Nginx as the web server, handling HTTP requests. It features an application server that executes the logic of the application, along with the application code files themselves. A MySQL database is utilized for storing and managing the application's data. The domain name, foobar.com, is configured with a "www" record that points to the server's IP address, 8.8.8.8. However, this setup encounters potential challenges, including single points of failure, downtime required for maintenance, and scalability limitations under high traffic conditions.

Component Roles and Functions
Server: Acts as the hardware or software that provides services to other computers or users within a network. It is the backbone of this infrastructure, hosting the necessary components to serve the website.

Domain Name: Serves as a human-friendly way to access internet resources, substituting easy-to-remember names for numerical IP addresses. In this context, foobar.com facilitates user access to the website.

DNS Record for "www": The "www" in www.foobar.com is typically an A record (Address Record), mapping the domain to the server's IPv4 address, directing users to the website hosted on the server.

Web Server (Nginx): Handles HTTP requests from clients, such as web browsers, and responds by serving the requested web pages or resources.

Application Server: Manages access to the application's business logic and functionality for client applications, processing dynamic content requests.

Database (MySQL): Stores, organizes, manages, and retrieves the application's data, facilitating easy access and manipulation of structured information.

Communication Protocol: The server uses HTTP (Hypertext Transfer Protocol) to communicate with users' computers, enabling the exchange of web pages and data.

Infrastructure Challenges
Single Point of Failure (SPOF): With only one server in place, any failure (hardware, software crash, etc.) can bring the entire system down, resulting in website downtime.

Downtime During Maintenance: Maintenance activities, such as deploying new code which requires a web server restart, can cause temporary website unavailability, potentially leading to user inconvenience and business impact.

Scalability Limitations: The infrastructure's single-server setup struggles to scale under heavy traffic, risking overloads, slower performance, or crashes during peak times.
