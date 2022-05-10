import uvicorn


def run_dev_server():
    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        workers=4,
        reload_dirs=["."],
    )


if __name__ == "__main__":
    run_dev_server()
