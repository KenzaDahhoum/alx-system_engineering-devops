Web Infrastructure Overview
Our infrastructure has been significantly upgraded to include advanced security measures and robust monitoring capabilities. We've introduced three firewalls and implemented an SSL certificate for www.foobar.com, thereby bolstering data security and enhancing communication encryption. Additionally, the integration of three monitoring clients allows for comprehensive data collection through services like Sumo Logic. This setup enables proactive system health and performance monitoring, ensuring swift detection and resolution of any anomalies or issues.

Added Security and Monitoring Elements
Firewalls: By adding three firewalls, we enhance our infrastructure's security posture. These firewalls control incoming and outgoing network traffic based on predefined security rules, effectively protecting against unauthorized access and cyber threats.

SSL Certificate: Implementing an SSL certificate for www.foobar.com enables HTTPS encryption, securing data transmission between the server and users' browsers. This measure protects sensitive information from being intercepted or tampered with during transmission.

Monitoring: The integration of monitoring clients facilitates the collection of performance and health data for our services. Utilizing platforms like Sumo Logic enhances our ability to monitor system components, identify anomalies, and address issues promptly, thus improving overall system reliability and performance.

Explaining Key Components
Purpose of Firewalls: Firewalls serve as the first line of defense in network security, regulating traffic to and from the network based on established security rules. They effectively segregate trusted internal networks from untrusted external ones, mitigating the risk of cyber threats.

HTTPS for Secure Communication: Serving traffic over HTTPS ensures secure communication between clients and the server. This protocol encrypts data, safeguarding it against eavesdropping, tampering, and forgery, thus preserving the confidentiality and integrity of the transmitted information.

Role of Monitoring: Monitoring is critical for maintaining the health, performance, and availability of system components. It involves collecting, analyzing, and interpreting data from various infrastructure elements to detect and respond to potential issues before they escalate.

Data Collection by Monitoring Tools: Monitoring tools collect data through continuous polling of metrics from targeted components. This includes retrieving information on resource utilization, performance metrics, and system health indicators, which is crucial for effective system management.

Monitoring Web Server QPS: To monitor the web server's Queries Per Second (QPS), select a suitable monitoring tool (e.g., Prometheus or Datadog), install its agent on the server, and configure it to track QPS metrics. Establish alerts for traffic anomalies and utilize the tool's dashboard for real-time QPS visualization. Regular data analysis helps optimize server performance and manage traffic efficiently.

Infrastructure Challenges
SSL Termination at Load Balancer: Terminating SSL at the load balancer can introduce security risks, as decrypted traffic is transmitted in plain text within the internal network. This exposure can potentially allow sensitive information to be accessed by unauthorized parties.

Single Point of Failure in MySQL: Relying on a single MySQL server for write operations presents a risk of downtime and data loss, as any failure in this server would disrupt database services.

Homogeneity in Server Components: Uniformity in server components increases the risk of widespread failures or security breaches if a single vulnerability affects all instances of a particular component, compromising the entire infrastructure
