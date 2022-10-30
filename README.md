### <<<<<<<<<<<<<<<<<<<< Start of Project >>>>>>>>>>>>>>>>>>>>

---

## SECTION 1 : PROJECT TITLE
## IRS-PM-2022-10-30-IS04FT-GRP-Movie Recommendation System

<img src="img/index.png"
     style="float: left; margin-right: 0px;" />

<img src="img/home.png"
     style="float: left; margin-right: 0px;" />

<img src="img/user.png"
     style="float: left; margin-right: 0px;" />

<img src="img/item.png"
	style="float: left; margin-right: 0px;" />

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
Nowadays movies have become one of the most popular and crucial entertainment mediums in people’s daily life. Also as a popular culture and art in contemporary society, the penetration, inclusiveness and coverage of movie and television art are unmatched by other arts. It affects social life by acting on people's thoughts and concepts. Movie and television appreciation can improve the aesthetic taste and artistic appreciation ability of people all around the world, and plays an important role in the quality education of people.

With the rapid development of Internet and technology, more and more companies tend to build an online movie website by purchasing movies’ copyright and provide users with paid online viewing services like Netflix, Prime Video, HBO Max, Tencent Video, etc. And every platform has its own recommendation system, which is very significant:

First, a fast recommendation system can increase user growth, increase user retention, activity, and length of stay on the web pages.

Most video streaming platforms use the membership-based profit model, Therefore, it is very important to increase the conversion rate of VIP and VIP retention. An accurate recommendation system can increase the purchase rate of VIP and attract users to continue watching movies that match their preferences.

A complete recommendation system can help save labor costs for companies. We can imagine that, with the increase of business complexity, the cost of the algorithm is basically constant, while the editing cost increases linearly. Therefore, the recommendation algorithm is widely used in extremely complex products or video companies with multiple product matrices to maintain, which can greatly reduce the Labor costs.

Using the techniques imparted to us in lectures, Our group use MySQL for building the whole database and deploy Django to build interfaces, and use python post method to resolve user preference data sent back by the frontend(Jquery+CSS3+HTML5). The collaborative filtering algorithm written by Python will give a feedback recommendation result back to the frontend.


---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Li Yuheng | A0261798L | 1. System architecture design 2. Data Acquisition 3. Data Processing 4. Django & Database development 5. User Interface development 6. Project report writing| e0983192@u.nus.edu |
| Huang Chenxi | A0261955W | 1. IMDB movies and users ratings datasets creating 2. Measuring cosine similarity 3. Reasoning by user-based and item-based collaborative filtering 4. Coding in Python for back-end recommendation  5. Joint debugging with Django front-end part 6. Deploying the web application 7. Elaborating group project report sections 3.1, 3.2, 3.3, 7| chenxihuang@u.nus.edu |
| Guo Hongxi | A0261887M | 1.Front-end design and implementation 2.Implementation of front end and back end interaction 3.Structure of database 4.Project reporting writing 5.Video making| E0983281@u.nus.edu |
| Paulson Premsingh Samson Dhansingh | A0261986M | 1. Algorithm development 2. Development of Django based web application  3. Making and editing of videos 4. Report Writing| e0983380@u.nus.edu |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Movie Recommendation System User Guide](https://res.cloudinary.com/marcomontalbano/image/upload/v1667141366/video_to_markdown/images/youtube--5vjL2sCKbPY-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=5vjL2sCKbPY "Movie Recommendation System User Guide")


---

## SECTION 5 : USER GUIDE

`Refer to appendix <Installation & User Guide> in project report at Github Folder: ProjectReport`

There are two ways to use this project.

- **Easy usage** 
- **Custom usage** - Convenient for custom development. You need to follow the packaging instruction to package manually. Unless you are familiar with Python and Django, this approach is not recommended.

### 5.1 Easy usage

#### 5.1.1 Download

Download the ZIP file and unzip it locally

#### 5.1.2 Create Database

1. Configure [MySQL](https://www.mysql.com/) connection:

   ```
   host='127.0.0.1', port=3306, user='root', password='root'
   ```

2. Import data: execute `moviedata.sql` in MySQL

#### 5.1.3 Run

1. Double click `\movieRMD\movieRMD.exe`
2. Browser access http://127.0.0.1:8000/

### 5.2 Custom usage

1. Perform **5.1.1 Download** & **5.1.2 Create Database**. Make `\source-code\movierecommend` a project file

   **NOTE: Make sure the project directory includes the static folder. If not, be sure to create a new static folder, and then create a new static_root folder under the static folder!*

2. *Optional check 1:*

   ​	\django_auth_example\urls.py includes codes:

   ```python
   from django.conf.urls import static
   from . import settings
   
   // The following code must be on a new line
   urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   ```

   ​	\django_auth_example\setting.py includes codes:

   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
   ```

3. Execute the `python manage.py collectstatic` command to collect static files into static_root

4. Execute the `pyinstaller manage.spec` command to package

5. Copy the `/static` and `/template` folders to the `/dist/manage` directory

6. Copy the `/users/static` folder to `/dist/manage/users`

7. *Optional check 2:*

   ​	Go back to the project directory. movieRMD.py should include codes:

   ```python
   import os
   os.system('manage.exe runserver 8000 --noreload')
   input()
   ```

8. Choose any of the following ways to execute

   ```shell
   // Execute with custom icon
   pyinstaller -F --icon=jieni.ico movieRMD.py
   // Execute without custom icon
   pyinstaller -F movieRMD.py
   ```

9. A movieRMD.exe will be generated in the dist folder and copy it to `dist/manage/`

10. Zip the dist folder, rename and replace the existing movieRMD folder

11. Perform **5.1.3 Run**

---
## SECTION 6 : PROJECT REPORT / PAPER

`Refer to project report at Github Folder: ProjectReport`

**Recommended Sections for Project Report / Paper:**
- Executive Summary 
- Project Description
    - Project Objective
- Knowledge Modeling
  - Reasoning From Data
  - A Modeling Dataset
  - Knowledge Reasoning
- Solution
  - System Architecture
  - System Scope
  - System Features
- Future Improvements
- Conclusion
- Appendices
  - Project Proposal
  - Mapped System Functionalities against the knowledge, techniques and skills of modular courses
  - Installation and User Guide
  - Individual Project Report


---
## SECTION 7 : MISCELLANEOUS

`Refer to Github Folder: Miscellaneous`

### MovieGenre3.csv

* The basic information list like names and types of movies
  
### users_resulttable.csv

* Users' preferences and ratings for system to deploy the algorithms
---

### <<<<<<<<<<<<<<<<<<<< End of Project >>>>>>>>>>>>>>>>>>>>

---

**This [Machine Reasoning (MR)](https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning "Machine Reasoning") course is part of the Analytics and Intelligent Systems and Graduate Certificate in [Intelligent Reasoning Systems (IRS)](https://www.iss.nus.edu.sg/stackable-certificate-programmes/intelligent-systems "Intelligent Reasoning Systems") series offered by [NUS-ISS](https://www.iss.nus.edu.sg "Institute of Systems Science, National University of Singapore").**

**Lecturer: [GU Zhan (Sam)](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan "GU Zhan (Sam)")**

[![alt text](https://www.iss.nus.edu.sg/images/default-source/About-Us/7.6.1-teaching-staff/sam-website.tmb-.png "Let's check Sam' profile page")](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan)

**zhan.gu@nus.edu.sg**
