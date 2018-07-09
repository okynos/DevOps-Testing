FROM centos:7.5.1804

RUN echo 'root:root' | chpasswd
RUN yum update -y && yum install -y openssl openssh openssh-server openssh-clients
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN ssh-keygen -A