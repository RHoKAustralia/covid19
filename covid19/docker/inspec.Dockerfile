FROM centos:7

ENV RPM=inspec-4.18.100-1.el7.x86_64.rpm
WORKDIR /root

# GET INSPEC BINARY
RUN curl -L -O https://packages.chef.io/files/stable/inspec/4.18.100/el/7/${RPM} \
    && rpm -ivh ${RPM} && mkdir -p /root/reports/

# INSPEC LICENSE
ADD ./requirements/inspec /etc/chef/accepted_licenses/inspec
 
CMD [ "bash" ]
EXPOSE 22