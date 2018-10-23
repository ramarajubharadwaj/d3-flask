
git clone 

craete mysql database (name='charts', user='admin', password='password') with tables


	CREATE TABLE `chart1` (
	  `uid` int(11) NOT NULL AUTO_INCREMENT,
	  `x_val` int(11) DEFAULT '0' COMMENT 'Axios X',
	  `y_val` int(11) DEFAULT '0' COMMENT 'Axios Y',
	  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update Time',
	  PRIMARY KEY (`uid`)
	) ENGINE=InnoDB AUTO_INCREMENT=14690 DEFAULT CHARSET=utf8;



	CREATE TABLE `chart2` (
	  `uid` int(11) NOT NULL AUTO_INCREMENT,
	  `x_val` int(11) DEFAULT '0' COMMENT 'Axios X',
	  `y_val` int(11) DEFAULT '0' COMMENT 'Axios Y',
	  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	  `j_arr` longtext,
	  PRIMARY KEY (`uid`)
	) ENGINE=InnoDB AUTO_INCREMENT=1006 DEFAULT CHARSET=utf8;

cd d3-flask

create and activate virtualenv

pip install -r requirements.txt

python app.py

cd vue-d3-chart

npm install

npm run dev

