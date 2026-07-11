# Backend Developer Interview Questions (Medium)

## 1. What is REST and why is it widely used?

**Answer:**
REST (Representational State Transfer) is an architectural style for designing web services. It uses standard HTTP methods such as GET, POST, PUT, PATCH, and DELETE. REST APIs are stateless, scalable, and easy to integrate with different clients.

---

## 2. Explain the difference between PUT and PATCH.

**Answer:**

- PUT replaces the entire resource.
- PATCH updates only specific fields of a resource.

Example:
If a user object contains name, email, and phone:
- PUT sends the complete updated object.
- PATCH can update only the email.

---

## 3. What are the commonly used HTTP status codes?

**Answer:**

- 200 OK – Request successful
- 201 Created – Resource created
- 204 No Content – Success with no response body
- 400 Bad Request – Invalid request
- 401 Unauthorized – Authentication required
- 403 Forbidden – User lacks permission
- 404 Not Found – Resource not found
- 500 Internal Server Error – Server-side error

---

## 4. What is middleware in Express.js?

**Answer:**
Middleware is a function that executes between receiving a request and sending a response. It can modify requests, validate data, authenticate users, log requests, or handle errors.

Example:
- Authentication middleware
- Logging middleware
- CORS middleware

---

## 5. Explain the request-response lifecycle in Express.

**Answer:**
1. Client sends a request.
2. Middleware processes the request.
3. Route handler executes business logic.
4. Database interaction occurs if needed.
5. Response is sent back to the client.

---

## 6. What is JWT authentication?

**Answer:**
JWT (JSON Web Token) is a secure way to authenticate users. After login, the server generates a signed token containing user information. The client includes this token in future requests for authentication.

---

## 7. Difference between Authentication and Authorization.

**Answer:**

Authentication:
Verifies who the user is.

Authorization:
Determines what the authenticated user is allowed to access.

---

## 8. What is CORS?

**Answer:**
Cross-Origin Resource Sharing (CORS) is a browser security mechanism that controls whether a web application can access resources hosted on another domain.

---

## 9. Why should environment variables be used?

**Answer:**
Environment variables store sensitive configuration such as API keys, database credentials, and secret keys outside the source code, improving security and flexibility.

---

## 10. Explain MVC architecture.

**Answer:**

Model:
Handles database operations.

View:
Displays data to users.

Controller:
Processes requests and coordinates between Model and View.

MVC improves code organization and maintainability.

---

## 11. What is the difference between SQL and NoSQL databases?

**Answer:**

SQL:
- Relational
- Fixed schema
- Uses tables

Examples:
MySQL, PostgreSQL

NoSQL:
- Flexible schema
- Document, key-value, graph, or column storage

Examples:
MongoDB, Cassandra

---

## 12. What is database indexing?

**Answer:**
Indexes improve query performance by allowing the database to locate records quickly instead of scanning every row.

---

## 13. Why is input validation important?

**Answer:**
Input validation prevents invalid or malicious data from entering the application, reducing bugs and protecting against attacks such as SQL Injection and Cross-Site Scripting (XSS).

---

## 14. What is rate limiting?

**Answer:**
Rate limiting restricts the number of requests a client can make within a specific period to prevent abuse and protect server resources.

---

## 15. What is caching?

**Answer:**
Caching stores frequently accessed data in fast memory, reducing database load and improving response times.

Common caching tools:
- Redis
- Memcached

---

## 16. What is Docker and why is it useful?

**Answer:**
Docker packages an application along with its dependencies into a container, ensuring consistent behavior across development, testing, and production environments.

---

## 17. What are microservices?

**Answer:**
Microservices divide an application into small, independent services that communicate via APIs. Each service can be developed, deployed, and scaled independently.

---

## 18. What is API versioning?

**Answer:**
API versioning allows developers to introduce changes without breaking existing clients.

Examples:
- /api/v1/users
- /api/v2/users

---

## 19. How do you secure a REST API?

**Answer:**
Common techniques include:
- JWT or OAuth authentication
- HTTPS
- Input validation
- Rate limiting
- Password hashing
- Secure environment variables
- Proper authorization checks

---

## 20. Explain the difference between Monolithic and Microservices architecture.

**Answer:**

Monolithic:
- Single application
- Easier to develop initially
- Harder to scale independently

Microservices:
- Independent services
- Easier to scale
- Better fault isolation
- More complex deployment

---

## 21. What is dependency injection?

**Answer:**
Dependency Injection is a design pattern where dependencies are provided to a class rather than created inside it. This improves modularity, testing, and maintainability.

---

## 22. Why should passwords never be stored in plain text?

**Answer:**
Plain-text passwords can be exposed if the database is compromised. Passwords should be hashed using algorithms such as bcrypt or Argon2 before storage.

---

## 23. Explain optimistic vs pessimistic locking.

**Answer:**

Optimistic Locking:
Assumes conflicts are rare and checks for conflicts before updating.

Pessimistic Locking:
Locks data during updates to prevent simultaneous modifications.

---

## 24. What happens when a client sends an HTTP request?

**Answer:**
- DNS resolves the server address.
- The request reaches the backend server.
- Middleware executes.
- Route handler processes the request.
- Database is queried if required.
- Response is returned to the client.

---

## 25. How would you improve the performance of a backend application?

**Answer:**
Possible optimizations include:
- Database indexing
- Query optimization
- Caching with Redis
- Pagination
- Load balancing
- Asynchronous processing
- Efficient API design
- Connection pooling
- Compression
- Docker-based deployment
# Backend Developer Interview Questions (Hard / Advanced)

## 1. What makes a REST API stateless?

**Answer:**
A REST API is stateless because the server does not store any client session information between requests. Every request must contain all the information required to process it, such as authentication tokens and request parameters. This improves scalability and simplifies load balancing.

---

## 2. How would you design a scalable authentication system?

**Answer:**
A scalable authentication system typically includes:
- JWT or OAuth 2.0 authentication
- Refresh tokens
- Password hashing using bcrypt or Argon2
- Secure HTTP-only cookies or Authorization headers
- Rate limiting
- Multi-factor authentication (MFA)
- Token expiration and revocation mechanisms
- Distributed session storage if required

---

## 3. Explain the CAP Theorem.

**Answer:**
The CAP Theorem states that a distributed system can guarantee only two of the following three properties simultaneously:
- Consistency
- Availability
- Partition Tolerance

For example:
- MongoDB prioritizes Availability and Partition Tolerance.
- Traditional SQL databases prioritize Consistency.

---

## 4. What are database transactions, and why are ACID properties important?

**Answer:**
A transaction is a sequence of operations treated as a single unit of work.

ACID ensures:
- Atomicity
- Consistency
- Isolation
- Durability

These properties maintain database integrity even during failures.

---

## 5. Explain optimistic locking and pessimistic locking with use cases.

**Answer:**

Optimistic Locking:
- Assumes conflicts are rare.
- Uses version numbers.
- Better for read-heavy applications.

Pessimistic Locking:
- Locks records immediately.
- Prevents concurrent modifications.
- Suitable for banking and financial systems.

---

## 6. What causes database deadlocks, and how can they be prevented?

**Answer:**
Deadlocks occur when multiple transactions wait indefinitely for each other's resources.

Prevention techniques:
- Access resources in a fixed order
- Keep transactions short
- Use lock timeouts
- Detect and terminate deadlocked transactions

---

## 7. How does connection pooling improve backend performance?

**Answer:**
Connection pooling maintains reusable database connections instead of creating a new connection for every request. This reduces latency, improves throughput, and decreases server resource usage.

---

## 8. Explain Horizontal Scaling vs Vertical Scaling.

**Answer:**

Vertical Scaling:
- Increase CPU/RAM of one server.

Horizontal Scaling:
- Add multiple servers behind a load balancer.

Horizontal scaling provides better fault tolerance and scalability.

---

## 9. What is eventual consistency?

**Answer:**
Eventual consistency means that after updates propagate through the distributed system, all replicas will eventually contain the same data. Temporary inconsistencies are acceptable for improved availability.

---

## 10. Explain API Gateway in Microservices.

**Answer:**
An API Gateway acts as a single entry point for client requests.

Responsibilities:
- Authentication
- Rate limiting
- Routing
- Logging
- Load balancing
- Response aggregation

---

## 11. How would you secure sensitive API endpoints?

**Answer:**
Security measures include:
- JWT/OAuth authentication
- Role-Based Access Control (RBAC)
- HTTPS
- Input validation
- SQL Injection prevention
- CSRF protection
- Rate limiting
- Logging and monitoring

---

## 12. Explain the Repository Pattern.

**Answer:**
The Repository Pattern abstracts database operations from business logic, making the application easier to test, maintain, and switch database implementations.

---

## 13. What are idempotent HTTP methods?

**Answer:**
An idempotent method produces the same result regardless of how many times it is executed.

Examples:
- GET
- PUT
- DELETE

POST is generally not idempotent.

---

## 14. Explain the N+1 Query Problem.

**Answer:**
The N+1 Query Problem occurs when one query retrieves parent records and additional queries retrieve related child records individually, causing performance degradation.

Solutions:
- Eager loading
- JOIN queries
- Batch fetching

---

## 15. Why should asynchronous processing be used?

**Answer:**
Asynchronous processing improves responsiveness by handling long-running tasks in the background.

Examples:
- Email notifications
- Payment processing
- Image compression
- Report generation

---

## 16. Explain message queues.

**Answer:**
Message queues enable asynchronous communication between services.

Popular tools:
- RabbitMQ
- Apache Kafka
- Amazon SQS

Benefits:
- Reliability
- Scalability
- Fault tolerance

---

## 17. What is the Circuit Breaker Pattern?

**Answer:**
The Circuit Breaker Pattern prevents repeated calls to failing services.

States:
- Closed
- Open
- Half-Open

It improves resilience in distributed systems.

---

## 18. Explain CQRS.

**Answer:**
Command Query Responsibility Segregation separates read operations from write operations, allowing independent optimization of each.

Benefits:
- Better scalability
- Performance optimization
- Easier maintenance

---

## 19. What is Event Sourcing?

**Answer:**
Instead of storing only the latest state, Event Sourcing stores every state-changing event.

Advantages:
- Audit history
- Replay capability
- Easier debugging

---

## 20. How would you optimize a slow REST API?

**Answer:**
Possible optimizations:
- Database indexing
- Query optimization
- Redis caching
- Pagination
- Compression
- Lazy loading
- Asynchronous processing
- CDN for static content
- Connection pooling

---

## 21. Explain Docker multi-stage builds.

**Answer:**
Multi-stage builds use multiple FROM statements to separate the build environment from the runtime environment.

Advantages:
- Smaller images
- Better security
- Faster deployment

---

## 22. What happens when a Docker container starts?

**Answer:**
Docker:
- Pulls the image if necessary
- Creates a writable container layer
- Configures networking
- Mounts volumes
- Executes the ENTRYPOINT or CMD
- Starts the application process

---

## 23. Explain Zero Downtime Deployment.

**Answer:**
Zero Downtime Deployment updates applications without interrupting users.

Techniques:
- Blue-Green Deployment
- Rolling Updates
- Canary Releases

---

## 24. How do distributed caches work?

**Answer:**
Distributed caches store frequently accessed data across multiple cache nodes.

Examples:
- Redis Cluster
- Hazelcast

Benefits:
- Reduced database load
- Faster response times
- Horizontal scalability

---

## 25. Design a URL Shortener (High-Level).

**Answer:**
A scalable URL shortener includes:
- REST API
- Unique short code generator (Base62)
- Database for URL mapping
- Cache (Redis)
- Load Balancer
- Analytics service
- Database replication
- Rate limiting
- Monitoring and logging

The system should ensure uniqueness, low latency, scalability, and fault tolerance.