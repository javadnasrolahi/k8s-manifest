FROM wurstmeister/kafka

ADD prom-jmx-agent-config.yml /usr/app/prom-jmx-agent-config.yml
ADD https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.15.0/jmx_prometheus_javaagent-0.15.0.jar /usr/app/jmx_prometheus_javaagent.jar
# ENV KAFKA_OPTS="-javaagent:/usr/app/jmx_prometheus_javaagent.jar=9898:/usr/app/prom-jmx-agent-config.yml"