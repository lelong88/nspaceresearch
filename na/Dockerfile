FROM python:3.12-slim

WORKDIR /app

# Install root-level dependencies
COPY requirements.txt /app/requirements-root.txt
RUN pip install --no-cache-dir -r requirements-root.txt

# Install web app dependencies
COPY app/requirements.txt /app/requirements-app.txt
RUN pip install --no-cache-dir -r requirements-app.txt

# Copy application code
COPY app/ /app/app/
COPY transcribe_meetings.py /app/
COPY summarize_meetings.py /app/
COPY glossary.md /app/
COPY summary-mac.md /app/

EXPOSE 6006

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "6006"]
