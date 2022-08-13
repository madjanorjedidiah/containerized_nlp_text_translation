FROM python:3.9-slim as python-base

RUN mkdir -p /opt/poetry


# prepend poetry and venv to path
ENV PATH="${PATH}:/root/.poetry/bin"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

RUN poetry config virtualenvs.create false

WORKDIR /opt/poetry
COPY poetry.lock pyproject.toml /opt/poetry/

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

# prerequisites for cloning model model
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs -y 

# clone model
RUN git lfs install
#RUN cd /opt/poetry
RUN git clone https://huggingface.co/t5-base 

#RUN cd ..
COPY . /opt/poetry/

#RUN flake8 --ignore=E101,W191 /opt/poetry

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]