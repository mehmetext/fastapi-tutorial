from app.models.post import PostRead

example_posts = [
    PostRead(
        id=1,
        title="Introduction to FastAPI",
        content="FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
        author_id=1,
        created_at="2024-01-15T09:30:00Z",
        updated_at="2024-01-15T09:30:00Z",
    ),
    PostRead(
        id=2,
        title="Python Best Practices",
        content="Explore the best practices for writing clean, efficient, and maintainable Python code.",
        author_id=2,
        created_at="2024-01-20T14:45:00Z",
        updated_at="2024-01-21T10:15:00Z",
    ),
    PostRead(
        id=3,
        title="RESTful API Design",
        content="Learn the principles of designing robust and scalable RESTful APIs for your web applications.",
        author_id=1,
        created_at="2024-02-05T11:00:00Z",
        updated_at="2024-02-06T16:30:00Z",
    ),
    PostRead(
        id=4,
        title="Asynchronous Programming in Python",
        content="Dive into asynchronous programming concepts and their implementation in Python using asyncio.",
        author_id=3,
        created_at="2024-02-10T08:20:00Z",
        updated_at="2024-02-10T08:20:00Z",
    ),
    PostRead(
        id=5,
        title="Database Integration with SQLAlchemy",
        content="Explore how to integrate SQLAlchemy with FastAPI for efficient database operations in your web applications.",
        author_id=2,
        created_at="2024-02-18T13:40:00Z",
        updated_at="2024-02-19T09:10:00Z",
    ),
    PostRead(
        id=6,
        title="Authentication and Authorization in FastAPI",
        content="Learn how to implement secure authentication and authorization mechanisms in your FastAPI applications.",
        author_id=1,
        created_at="2024-02-25T10:00:00Z",
        updated_at="2024-02-25T10:00:00Z",
    ),
    PostRead(
        id=7,
        title="Testing FastAPI Applications",
        content="Discover best practices for testing FastAPI applications using pytest and other testing tools.",
        author_id=3,
        created_at="2024-03-01T15:30:00Z",
        updated_at="2024-03-02T09:45:00Z",
    ),
    PostRead(
        id=8,
        title="Dependency Injection in FastAPI",
        content="Understand the concept of dependency injection and how to use it effectively in FastAPI.",
        author_id=2,
        created_at="2024-03-10T11:20:00Z",
        updated_at="2024-03-10T11:20:00Z",
    ),
    PostRead(
        id=9,
        title="FastAPI with Docker",
        content="Learn how to containerize your FastAPI application using Docker for easier deployment and scaling.",
        author_id=1,
        created_at="2024-03-15T14:00:00Z",
        updated_at="2024-03-16T10:30:00Z",
    ),
    PostRead(
        id=10,
        title="Error Handling in FastAPI",
        content="Explore various techniques for handling errors and exceptions in FastAPI applications.",
        author_id=3,
        created_at="2024-03-20T09:15:00Z",
        updated_at="2024-03-20T09:15:00Z",
    ),
    PostRead(
        id=11,
        title="FastAPI and WebSockets",
        content="Implement real-time communication in your FastAPI applications using WebSockets.",
        author_id=2,
        created_at="2024-03-25T16:45:00Z",
        updated_at="2024-03-26T11:00:00Z",
    ),
    PostRead(
        id=12,
        title="API Documentation with Swagger UI",
        content="Learn how to automatically generate interactive API documentation for your FastAPI project using Swagger UI.",
        author_id=1,
        created_at="2024-04-01T13:30:00Z",
        updated_at="2024-04-01T13:30:00Z",
    ),
    PostRead(
        id=13,
        title="Background Tasks in FastAPI",
        content="Explore how to implement and manage background tasks in FastAPI for improved performance and user experience.",
        author_id=3,
        created_at="2024-04-05T10:20:00Z",
        updated_at="2024-04-06T14:15:00Z",
    ),
    PostRead(
        id=14,
        title="FastAPI and GraphQL",
        content="Integrate GraphQL into your FastAPI application for flexible and efficient data querying.",
        author_id=2,
        created_at="2024-04-10T09:00:00Z",
        updated_at="2024-04-10T09:00:00Z",
    ),
    PostRead(
        id=15,
        title="Caching Strategies in FastAPI",
        content="Implement various caching strategies to improve the performance of your FastAPI applications.",
        author_id=1,
        created_at="2024-04-15T11:45:00Z",
        updated_at="2024-04-16T08:30:00Z",
    ),
    PostRead(
        id=16,
        title="FastAPI Middleware",
        content="Learn how to create and use middleware in FastAPI to add custom functionality to your application.",
        author_id=3,
        created_at="2024-04-20T14:30:00Z",
        updated_at="2024-04-20T14:30:00Z",
    ),
    PostRead(
        id=17,
        title="Rate Limiting in FastAPI",
        content="Implement rate limiting in your FastAPI application to protect against abuse and ensure fair usage.",
        author_id=2,
        created_at="2024-04-25T10:15:00Z",
        updated_at="2024-04-26T09:00:00Z",
    ),
    PostRead(
        id=18,
        title="FastAPI and Celery",
        content="Integrate Celery with FastAPI for handling distributed tasks and background job processing.",
        author_id=1,
        created_at="2024-05-01T13:00:00Z",
        updated_at="2024-05-01T13:00:00Z",
    ),
    PostRead(
        id=19,
        title="Securing FastAPI Applications",
        content="Learn best practices for securing your FastAPI applications, including HTTPS, CORS, and security headers.",
        author_id=3,
        created_at="2024-05-05T11:30:00Z",
        updated_at="2024-05-06T10:45:00Z",
    ),
    PostRead(
        id=20,
        title="FastAPI Performance Optimization",
        content="Discover techniques and tools for optimizing the performance of your FastAPI applications.",
        author_id=2,
        created_at="2024-05-10T09:45:00Z",
        updated_at="2024-05-10T09:45:00Z",
    ),
    PostRead(
        id=21,
        title="FastAPI and Machine Learning",
        content="Integrate machine learning models into your FastAPI application for intelligent API endpoints.",
        author_id=1,
        created_at="2024-05-15T14:20:00Z",
        updated_at="2024-05-16T11:10:00Z",
    ),
    PostRead(
        id=22,
        title="Event-Driven Architecture with FastAPI",
        content="Implement event-driven architecture patterns in your FastAPI applications for scalable and decoupled systems.",
        author_id=3,
        created_at="2024-05-20T10:00:00Z",
        updated_at="2024-05-20T10:00:00Z",
    ),
    PostRead(
        id=23,
        title="FastAPI and Microservices",
        content="Learn how to design and implement microservices architecture using FastAPI.",
        author_id=2,
        created_at="2024-05-25T13:15:00Z",
        updated_at="2024-05-26T09:30:00Z",
    ),
    PostRead(
        id=24,
        title="Internationalization in FastAPI",
        content="Implement internationalization (i18n) in your FastAPI application to support multiple languages.",
        author_id=1,
        created_at="2024-06-01T11:45:00Z",
        updated_at="2024-06-01T11:45:00Z",
    ),
    PostRead(
        id=25,
        title="FastAPI and Serverless Computing",
        content="Explore how to deploy FastAPI applications in serverless environments for scalable and cost-effective solutions.",
        author_id=3,
        created_at="2024-06-05T09:30:00Z",
        updated_at="2024-06-06T14:00:00Z",
    ),
]
