"""
Sample document corpus for the semantic search demo.
Each document has: id, title, content, category
"""

DOCUMENTS = [
    # ── Medical ──────────────────────────────────────────────────────────────
    {
        "id": 1,
        "title": "Heart Disease Overview",
        "content": "Heart disease refers to conditions affecting the heart including coronary "
                   "artery disease, arrhythmias, and heart failure. Symptoms include chest pain "
                   "and shortness of breath.",
        "category": "Medical"
    },
    {
        "id": 2,
        "title": "Cardiac Health Tips",
        "content": "Maintaining cardiac health involves regular exercise, balanced diet, avoiding "
                   "smoking, and monitoring blood pressure to prevent cardiovascular problems.",
        "category": "Medical"
    },
    {
        "id": 3,
        "title": "Nutrition and Diet",
        "content": "A healthy diet includes fruits, vegetables, whole grains, lean proteins, and "
                   "healthy fats. Proper nutrition supports immune function and reduces chronic "
                   "disease risk.",
        "category": "Medical"
    },
    {
        "id": 4,
        "title": "Mental Health and Wellness",
        "content": "Mental health encompasses emotional, psychological, and social wellbeing. "
                   "Therapy, mindfulness, exercise, and social connections are effective tools "
                   "for managing anxiety and depression.",
        "category": "Medical"
    },
    {
        "id": 5,
        "title": "Yoga and Mindfulness",
        "content": "Yoga combines physical postures, breathing techniques, and meditation to "
                   "improve flexibility, strength, and mental clarity. Regular practice reduces "
                   "stress and promotes overall wellbeing.",
        "category": "Medical"
    },

    # ── Technology ───────────────────────────────────────────────────────────
    {
        "id": 6,
        "title": "Introduction to Machine Learning",
        "content": "Machine learning is a subset of AI that enables systems to learn from data "
                   "without explicit programming. It includes supervised, unsupervised, and "
                   "reinforcement learning.",
        "category": "Technology"
    },
    {
        "id": 7,
        "title": "Deep Learning Neural Networks",
        "content": "Deep learning uses multi-layered neural networks to model complex patterns. "
                   "Convolutional networks excel at image recognition while transformers power "
                   "language models.",
        "category": "Technology"
    },
    {
        "id": 8,
        "title": "Python Programming Basics",
        "content": "Python is a versatile high-level programming language known for its "
                   "readability. It supports object-oriented, functional, and procedural "
                   "programming paradigms.",
        "category": "Technology"
    },
    {
        "id": 9,
        "title": "Quantum Computing Fundamentals",
        "content": "Quantum computers use qubits to perform calculations exponentially faster "
                   "than classical computers. They leverage superposition and entanglement for "
                   "complex problem solving.",
        "category": "Technology"
    },
    {
        "id": 10,
        "title": "Artificial Intelligence Ethics",
        "content": "AI ethics addresses bias, fairness, transparency, and accountability in AI "
                   "systems. Ensuring AI benefits all of humanity while minimizing harm is a "
                   "critical challenge.",
        "category": "Technology"
    },
    {
        "id": 11,
        "title": "Cybersecurity Fundamentals",
        "content": "Cybersecurity protects systems from digital attacks. Key practices include "
                   "encryption, multi-factor authentication, regular patching, and employee "
                   "training to prevent data breaches.",
        "category": "Technology"
    },
    {
        "id": 12,
        "title": "History of the Internet",
        "content": "The internet evolved from ARPANET in the 1960s. Tim Berners-Lee invented "
                   "the World Wide Web in 1989, transforming global communication, commerce, "
                   "and information sharing.",
        "category": "Technology"
    },

    # ── Environment ──────────────────────────────────────────────────────────
    {
        "id": 13,
        "title": "Climate Change Effects",
        "content": "Climate change causes rising sea levels, extreme weather events, and "
                   "biodiversity loss. Greenhouse gas emissions from fossil fuels are the "
                   "primary driver of global warming.",
        "category": "Environment"
    },
    {
        "id": 14,
        "title": "Renewable Energy Sources",
        "content": "Solar panels, wind turbines, and hydroelectric power are clean energy "
                   "alternatives to fossil fuels that reduce carbon emissions and combat "
                   "environmental degradation.",
        "category": "Environment"
    },
    {
        "id": 15,
        "title": "Ocean Biodiversity",
        "content": "Oceans cover 70% of Earth and host extraordinary biodiversity including "
                   "coral reefs, deep sea creatures, and marine mammals. Overfishing and "
                   "pollution threaten marine ecosystems.",
        "category": "Environment"
    },

    # ── Science ───────────────────────────────────────────────────────────────
    {
        "id": 16,
        "title": "Space Exploration History",
        "content": "NASA's Apollo program landed humans on the moon in 1969. Space exploration "
                   "has advanced through satellites, space stations, Mars rovers, and deep "
                   "space probes.",
        "category": "Science"
    },
    {
        "id": 17,
        "title": "Astronomy and Black Holes",
        "content": "Black holes are regions of spacetime with gravity so strong nothing can "
                   "escape. They form from collapsed massive stars and are studied through "
                   "gravitational waves and telescopes.",
        "category": "Science"
    },

    # ── Finance ───────────────────────────────────────────────────────────────
    {
        "id": 18,
        "title": "Cryptocurrency and Blockchain",
        "content": "Blockchain is a distributed ledger technology underlying cryptocurrencies "
                   "like Bitcoin and Ethereum. It enables decentralized, tamper-resistant "
                   "transactions without intermediaries.",
        "category": "Finance"
    },
    {
        "id": 19,
        "title": "Stock Market Investment",
        "content": "Investing in stocks involves buying shares of publicly traded companies. "
                   "Diversification, long-term thinking, and understanding risk tolerance are "
                   "key principles of successful investing.",
        "category": "Finance"
    },
    {
        "id": 20,
        "title": "Global Economy Trends",
        "content": "The global economy is shaped by trade policies, inflation, interest rates, "
                   "and technological disruption. Emerging markets in Asia and Africa are "
                   "driving significant growth.",
        "category": "Finance"
    },
]