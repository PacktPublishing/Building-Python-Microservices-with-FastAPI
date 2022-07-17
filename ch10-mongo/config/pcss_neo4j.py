from neo4j import GraphDatabase

uri = "bolt://127.0.0.1:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "admin2255"))