docker build -t predict .

docker run --rm -it \
	-v `pwd`/../models:/models \
	-v `pwd`:/app \
	-v `pwd`/../processed_data:/data \
	--link frontapp:app predict
