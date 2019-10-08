FROM continuumio/anaconda3
RUN apt-get update
RUN apt-get install \
                vim  \
                build-essentials \
                git
RUN pip install dtw-python