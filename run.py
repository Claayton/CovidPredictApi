"""Script para rodar o programa"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="src.main.config.http_server_configs:create_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True,
        factory=True,
    )
