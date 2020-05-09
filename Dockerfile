FROM python:3.6
MAINTAINER kartik
WORKDIR /calculator
ADD . /calculator
EXPOSE 4000
CMD ["python","calc.py"]
sudo rm /var/lib/dpkg/info/linux-image-4.15.0-99-generic.postinst