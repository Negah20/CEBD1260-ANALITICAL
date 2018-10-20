FROM python:3
ADD project /project
RUN pip install conda
RUN ["bash"]

