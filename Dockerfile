# LICENSE UPL 1.0
#
# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# ORACLE DOCKERFILES PROJECT
# --------------------------
# This Dockerfile extends the Oracle WebLogic image by installing the Supplemental package of WebLogic which
# includes extra samples of Java EE, Coherence applications, and Multitenant domains.
#
# REQUIRED FILES TO BUILD THIS IMAGE
# ----------------------------------
# (1) fmw_12.2.1.2.0_wls_supplemental_quick_Disk1_1of1.zip
#     Download the Developer Quick installer from http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-for-dev-1703574.html
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Put all downloaded files in the same directory as this Dockerfile
# Run:
#      $ sudo docker build -t 12212-oradb-medrec .
#

# Pull base image
# ---------------
FROM oracle/weblogic:12.2.1.4-generic

# Maintainer
# ----------
MAINTAINER Ricky Bruggemann <ricky@cedae.com.br>

USER root
COPY container-scripts/* properties/* /u01/oracle/
RUN chmod +xr /u01/oracle/createAndStartEmptyDomain.sh /u01/oracle/deployAppToDomain.sh

ENV ORACLE_HOME=/u01/oracle \
    USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom" \
    SCRIPT_FILE=/u01/oracle/createAndStartEmptyDomain.sh \
    PATH=$PATH:${JAVA_HOME}/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin

# Domain and Server environment variables
# ------------------------------------------------------------
ENV DOMAIN_NAME="${DOMAIN_NAME:-base_domain}" \
    ADMIN_LISTEN_PORT="${ADMIN_LISTEN_PORT:-7001}" \
    ADMIN_NAME="${ADMIN_NAME:-AdminServer}" \
    ADMINISTRATION_PORT_ENABLED="${ADMINISTRATION_PORT_ENABLED:-false}" \
    ADMINISTRATION_PORT="${ADMINISTRATION_PORT:-9002}"

USER oracle

WORKDIR ${ORACLE_HOME}

# Define default command to start script.
CMD ["/u01/oracle/createAndStartEmptyDomain.sh"]
