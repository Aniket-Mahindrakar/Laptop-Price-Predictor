# lightweight python
FROM python:3.8-slim

RUN apt-get update

# Copy local code to the container image.
RUN mkdir /laptop_price_predictor && chown -R 42420:42420 /laptop_price_predictor
ENV APP_HOME /laptop_price_predictor
WORKDIR $APP_HOME
COPY . ./

RUN ls -la $APP_HOME/

# Install dependencies
RUN pip install -r requirements.txt

# Run the streamlit on container startup
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]

