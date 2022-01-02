FROM docker.io/bitnami/spark:3.1.2
ENV SPARK_MASTER local[*]
ENV ZINGG_HOME /zingg-0.3.1-SNAPSHOT
WORKDIR /
USER root
WORKDIR /zingg-0.3.1-SNAPSHOT
RUN curl --location https://github.com/zinggAI/zingg/releases/download/v0.3.1/zingg-0.3.1-SNAPSHOT-spark-3.1.2.tar.gz | \
tar --extract --gzip --strip=1 
RUN chmod -R a+rwx /zingg-0.3.1-SNAPSHOT/models
RUN chown -R 1001 /zingg-0.3.1-SNAPSHOT/models
USER 1001

