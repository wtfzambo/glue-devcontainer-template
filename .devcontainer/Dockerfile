ARG GLUE_VERSION="4.0.0"
FROM amazon/aws-glue-libs:glue_libs_${GLUE_VERSION}_image_01

ARG USER=glue_user
USER $USER

# Poetry installation
ARG HOME="/home/$USER"
ARG POETRY_VERSION="none"

ENV PATH="${HOME}/.local/bin:$PATH"

RUN if [ "${POETRY_VERSION}" != "none" ]; then  echo "Installing poetry" \
    && curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 - ; \
    fi
