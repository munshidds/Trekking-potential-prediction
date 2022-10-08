Overview

Topic = Trekking potential prediction
In this project, It is predicted that whether a person will be capable of hiking or not, by analysing certain 
features such as age, gender, habits like smoking or not, fascination towards the journey ,
climate, jeep service, package price, and feedback of former hikers , with the help of some collected datas.

Motive

I have some reasons for create Trekking potential prediction, basically, i am a trekking lover, when I was in 
trekking, I could see that some one of hikers were struggling for reaching the target. The reason why they 
were struggling was that, their fitness wasn’t okay for the journey. before going fora trekking, using a web help like this will 
make them understand wether they will be capable of hiking or not

Imports



•	import numpy as np
•	import pandas as pd
•	import joblib
•	from sklearn.preprocessing import MinMaxScaler
•	 from sklearn.model_selection import train_test_split
•	from sklearn.svm import SVC
•	from sklearn.model_selection import GridSearchCV
•	from sklearn.tree import DecisionTreeClassifier
•	from sklearn.ensemble import RandomForestClassifier
•	from sklearn.neighbors import KNeighborsClassifier
•	from sklearn.linear_model import LogisticRegression

