# System Design

## Task 2.1

### Functional Requirements
1. Login
2. View marks and enroll
3. Admin management

### Non-Functional Requirements
- Scalability -> handle 50,000 users
- Availability -> 99.9% uptime
- Security -> authentication and RBAC

### Monolith vs Microservices
Microservices support independent deployment, better fault isolation, and independent scaling but are more complex to manage. For 50,000 concurrent users, microservices are recommended.

## Task 2.2
Presentation -> Business -> Data Access -> Database.
Use horizontal scaling with Round Robin load balancing. Elastic auto-scaling reduces servers during off-peak periods. Session problem: session affinity. Solutions: sticky sessions (trade-off: poor failover/load distribution) or shared session store (trade-off: extra cost/latency).