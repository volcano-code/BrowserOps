"""Run the BrowserOps demo SaaS locally."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("browserops_demo.app:app", host="127.0.0.1", port=3100, reload=True)
