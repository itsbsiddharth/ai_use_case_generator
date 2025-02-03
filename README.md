graph TD
    A[User Input] --> B[Main Orchestrator Agent]
    B --> C[Industry Research Agent]
    B --> D[Market Analysis Agent]
    B --> E[Resource Collection Agent]
    
    C --> F[Web Search Tools]
    C --> G[Company/Industry Analysis]
    
    D --> H[Trend Analysis]
    D --> I[Use Case Generation]
    
    E --> J[Dataset Search]
    E --> K[Resource Compilation]
    
    F --> L[Tavily API]
    G --> M[Industry Reports]
    
    H --> N[AI/ML Trends]
    I --> O[Use Case Database]
    
    J --> P[Kaggle/HuggingFace/GitHub]
    K --> Q[Markdown Report]
    
    subgraph Output
        R[Final Report]
        S[Resource Links]
        T[Implementation Guidelines]
    end
    
    B --> Output
