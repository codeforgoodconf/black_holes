docker build -t predict . && docker run --rm -it -v `pwd`:/app -v /Users/jfrank/blackhole_back/prediction_runtime/../prepared:/data predict
