FROM python:latest
RUN pip install --upgrade pip

RUN useradd -m myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
COPY --chown=myuser:myuser app.py app.py
COPY --chown=myuser:myuser main.py main.py
COPY --chown=myuser:myuser upload.py upload.py
COPY --chown=myuser:myuser write_to_mysql.py write_to_mysql.py
COPY --chown=myuser:myuser static static
COPY --chown=myuser:myuser templates templates
COPY --chown=myuser:myuser db_config.yaml db_config.yaml
COPY --chown=myuser:myuser create_tables.py create_tables.py
COPY --chown=myuser:myuser upload_config.yaml upload_config.yaml
COPY --chown=myuser:myuser get_videos.py get_videos.py
RUN pip install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"
ENV FLASK_APP=main
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]