FROM java
WORKDIR /wekainstall
RUN wget http://prdownloads.sourceforge.net/weka/weka-3-8-1.zip
RUN unzip weka*
RUN rm *.zip
RUN mv weka* weka
WORKDIR /app
ADD predict.sh /app/predict.sh
RUN chmod +x predict.sh
