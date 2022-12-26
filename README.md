<div align=center><img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Drama%20project&fontSize=90" />	

<br/>
<div align=center>
<h3> zzanggeonui </h3>

[![GitHub Badge](https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white)](https://github.com/zzanggeonui)
[![Tistory Badge](https://img.shields.io/badge/TSTORY-555263?style=flat&logoColor=white)](https://seonggongstory.tistory.com/)
[![Gmail Badge](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=Gmail&logoColor=white)](mailto:gksrjsgml961105@gmail.com)
<br/>
<div align=center>
<h3> Languages <h3> 
<img src=https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white/>
<br/>
	
<div align=center>
<h3> Library <h3> 	
<img src=https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white />
<img src=https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/>
<img src=https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/>
<img src= https://img.shields.io/badge/matplotlib.pyplot-F7931E?style=flat&logo=matplotlib.pyplot&logoColor=white)/>
<img src=https://img.shields.io/badge/Seaborn-232F3E?style=flat&logo=Seaborn&logoColor=white />
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=Bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Google Translate-4285F4?style=flat&logo=Google Translate&logoColor=white" />
<br/>
	
<div align=center>
<h3> Tools <h3> 
<img src=https://img.shields.io/badge/Anaconda-44A833?style=flat&logo=Anaconda&logoColor=white/>
<img src=https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=flat&logo=Visual%20Studio%20Code&logoColor=white/>
<img src=https://img.shields.io/badge/Amazon%20AWS-232F3E?style=flat&logo=Amazon%20AWS&logoColor=white/>
<img src=https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=Jupyter&logoColor=white)/>
<br/>
<div align=left>

 
	
## 개요
	
드라마 및 영상물 리뷰 전문 사이트인 IMDb와 MyDramaList의 한국 드라마 데이터를 기반으로 한국드라마 흥행요인 분석 및 검색 기능을 구현한 앱입니다.


## 주소

http://ec2-43-201-85-127.ap-northeast-2.compute.amazonaws.com:8503/

## 프로젝트 설명
![image](https://github.com/zzanggeonui/drama/blob/main/data/IMG.png)
![image](https://github.com/zzanggeonui/drama/blob/main/data/img2.png)
![image](https://github.com/zzanggeonui/drama/blob/main/data/img3.png)
![image](https://github.com/zzanggeonui/drama/blob/main/data/img4.png)
	
- 검색을 통해 작품 시놉시스와 정보, 배우의 필모그래피를 확인할 수 있습니다
- 상세검색에선 Interactive select를 통한 원하는 작품을 직접 찾아볼 수 있으며
- 분석에선 드라마의 장르,태그,배우,러닝타임,에피소드 갯수등 여러 항목이 드라마 흥행에 영향이 있는지 분석하였습니다.

	
## 작업 설명

- jupyter notebook을 통해 데이터프레임 가공 및 데이터 분석을 진행하였습니다
- putty를 통해 AWS EC2 인스턴스에 연결하여 서버를 배포 및 관리하였습니다.
- github action을 활용하여 CI/CD를 구현하였습니다.


## 데이터 설명
	
- Genres = 장르  
- Tags= 태그 
- Content Rating=시청등급  
- Duration = 러닝타임 
- scored by = 리뷰참여자수  
- score = 평점  
- Watchers = 사이트 조회수 
- Popularity = 인기도  
- Episodes = 에피소드 숫자  
- actors = 배우이름  
- platforms = 현재 드라마를 볼 수있는 플랫폼


	
	
## 데이터 참고

- 메인 데이터 :https://www.kaggle.com/datasets/iphigeniebera/korean-drama-list-about-740-unique-dramas
- 스크래핑 시놉시스 및 사진 자료  : https://mydramalist.com/





	


	
	
