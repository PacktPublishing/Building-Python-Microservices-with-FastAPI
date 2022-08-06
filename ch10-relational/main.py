if __name__ == "__main__":

    import uvicorn

    uvicorn.run("app:app", port=8002, reload=True)
