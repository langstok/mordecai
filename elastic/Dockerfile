FROM elasticsearch:5.5.2
MAINTAINER Sander Puts

RUN wget https://s3.amazonaws.com/ahalterman-geo/geonames_index.tar.gz
RUN tar -xzf geonames_index.tar.gz
RUN mv geonames_index/ /usr/share/elasticsearch/data