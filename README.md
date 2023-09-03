# Streamlit App

Sample Source for StreamLit.

For Dockerize the App

Build App

```
docker build -t streamlit:dev .
```

Run App 

```
docker run --rm -p 8501:8501 --name streamlit streamlit:dev
```